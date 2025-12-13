import pandas as pd
import os
import boto3
import io
from dotenv import load_dotenv
from utils.logger import get_logger

logger = get_logger(__name__)



class DataIngestion :

    """"
    Handles loading of raw CSV data from AWS S3
    and returns it as a pandas DataFrame.
    """
    def __init__(self) :
        
        load_dotenv()

        self.bucket_name = os.getenv("AWS_BUCKET_NAME")
        self.file_key = os.getenv("AWS_FILE_KEY")

        # Create S3 client using credentials from .env
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION")
        )

    def load_from_s3(self) -> pd.DataFrame:

        try:
            logger.info(f"Loading data from S3: s3://{self.bucket_name}/{self.file_key}")

            obj = self.s3.get_object(Bucket=self.bucket_name, Key=self.file_key)

            df = pd.read_csv(io.BytesIO(obj["Body"].read()))

            logger.info(f"Data loaded successfully. Shape: {df.shape}")

            return df
        
        except Exception as e:
            logger.exception("Failed to load data from S3")
            raise e
            

      
    def save_sample(self, df : pd.DataFrame , save_path : str = 'data/raw/sample_travel.csv' , sample_size : int = 1000) :
        """ 
        Saves a small sample of the dataset locally.
        """

        try : 
            dir_name = os.path.dirname(save_path)
            if dir_name :
                os.makedirs(dir_name , exist_ok = True)
            sample_df = df.sample(min(sample_size, len(df)))
            sample_df.to_csv(save_path, index=False)

            logger.info(f"Saved sample ({sample_df.shape[0]} rows) to {(save_path)}")

        except Exception as e:
            logger.exception("Error saving sample locally")
            raise e
        
    
