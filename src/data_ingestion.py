import pandas as pd
import os
from utils.logger import get_logger

logger = get_logger(__name__)

''' THIS FUNCTION IS DESIGNEED TO LOAD THE DATA FROM A CSV FILE
    AND TRANSFORM IT TO A PANDAS DATAFRAME '''

def ingest_data(file_path : str) -> pd.DataFrame :
    try:
        
        if os.path.exists(file_path) :
            logger.info(f"Loading data from {file_path}")
            
            df = pd.read_csv(file_path)
            logger.info(f"Data loaded Successfully. Shape : {df.shape}")
            return df
        
        else :
            logger.error(f"File not found: {file_path}")
            raise FileNotFoundError(f'File not found: {file_path}')


    except pd.errors.EmptyDataError as e:
        logger.error(f"File is empty: {file_path}")
        raise e
    
    
    except Exception as e:
        logger.exception(f"Unexpected error loading data from {file_path}")
        raise 
        
