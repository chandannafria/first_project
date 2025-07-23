import sys

class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = self.get_detailed_error(error_message, error_detail)

    def get_detailed_error(self, error_message, error_detail):
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        return f"Error in {file_name}, line {exc_tb.tb_lineno}: {error_message}"

    def __str__(self):
        return self.error_message
