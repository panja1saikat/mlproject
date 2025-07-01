import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join("artifact","train..csv")
    test_data_path : str=os.path.join("artifact","test.csv")
    raw_data_path : str=os.path.join("artifact","data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_cofig=DataIngestionConfig()
    
    def iniate_data_ingestion(self):
        logging.info("Enter the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_cofig.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_cofig.raw_data_path,index=True,header=False)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=45)

            train_set.to_csv(self.ingestion_cofig)


        
        except:
            pass
