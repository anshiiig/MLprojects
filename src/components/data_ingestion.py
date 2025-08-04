import os
import sys # for using custom exception
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer


@dataclass # this is decorator --> use to directly define our class variable
class DataIngestionConfig:  # we have created this class so that we can store raw inputs/providing all imputs needed
    train_data_path: str=os.path.join('artifacts',"train.csv") #____ this is our input we are giving--> then data ingestion will save the train data in this particular path
    test_data_path: str=os.path.join('artifacts',"test.csv") #     |
    raw_data_path: str=os.path.join('artifacts',"data.csv") #  ____|---> this tell us where to store train ,test and raw data   

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):  #if our data is stored in some databases-->the code will read from the database
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook/data/stud.csv') 
            logging.info("Read the dataset as dataframe ")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) #--> getting the directory name wrt this path

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiating")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
        
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
