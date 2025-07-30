import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
from sklearn.metrics import r2_score
import dill

def save_object(file_path , obj):
    '''
    This function saves the object to a file
    '''
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj,file_obj)
            
    except Exception as e:
        raise CustomException(e , sys)
    
def evaluate_model(x_train, y_train, x_test, y_test, models):
    '''
    This function evaluates the model and returns the best model based on r2 score
    '''
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.value())[i]
            model.fit(x_train, y_train)
            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)
            report[list(model.key())[i]] =  test_model_score
            
        return report           
        
    except Exception as e:
        raise CustomException(e , sys)