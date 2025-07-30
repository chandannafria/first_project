import pandas as pd
import os
import sys
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from src.utils import save_object

@dataclass
class DataTransformationconfig:
    preprocessor_obj_file_path: str = os.path.join("artifacts" , "preprocessor.pkl")
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationconfig()
    
    def get_data_transformation_object(self):
        '''
        This function is responsible for data transformation
        '''
        try:
            numerical_features  = ["writing_score", "reading_score"]
            categorical_features = [
                "gender",
                "race_ethnicity",
                "parental_leval_of_education",
                "lunch",
                "test_preparation_course"
            ]
             
            numerical_transformer = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())])
                
            categorical_transformer = Pipeline(steps=[
                ("imputer" , SimpleImputer(strategy="most_frequent")),
                ("onehotencoder" , OneHotEncoder()),
                ("sclaer" , StandardScaler)
            ])
            
            logging.info(f"numerical columns: {numerical_features}")
            logging.info(f"categorical columns: {categorical_features} ")
            
            preprocessor = ColumnTransformer(
                [
                    ("numerical_transformer"  , numerical_transformer, numerical_features),
                    ("categorical_transformer", categorical_transformer, categorical_features)
                ]
            )
            
            return preprocessor
            
        except Exception as e:
            raise CustomException(e , sys)
        
        
    def initiate_data_transformation(self, train_path , test_path):
        try:
           
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("entered the data transformation method")
            logging.info("Obtaining preprocessing object")
            
            preprocessing_obj = self.get_data_transformation_object()
            target_column_name = "math_score"
            numerical_column_name = ["writing_score" , "reading_score"]
            
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]
            
            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]
            
            logging.info("Applying preprocessing object on training and testing dataframes")
            
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)
            
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr , np.array(target_feature_test_df)]

            logging.info("saved preprocessing object")
            
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )
            
            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
            
        except Exception as e:
            raise CustomException(e, sys)
            