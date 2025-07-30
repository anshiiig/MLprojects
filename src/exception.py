import sys
import logging

def error_message_detail(error,error_detail:sys):   #whenever a error or exception occurs this msg will will be pushed
    _,_,exc_tb=error_detail.exc_info()  # this varia will give all the info that in which file,line no the error had occured
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))   # [{0}],[{1}]... etc--> are the place holders for displaying the values

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):    # when we print it this msg will auto. will be print
        return self.error_message
    

# if __name__=="__main__":

#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by Zero")
#         raise CustomException(e,sys)
    