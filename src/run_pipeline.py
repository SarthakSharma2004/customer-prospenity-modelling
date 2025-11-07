import os
import pandas as pd
from utils.logger import get_logger
from src.data_ingestion import DataIngestion
from src.preprocessing import DataPreprocessor
from src.model_training import ModelTrainer

logger = get_logger(__name__)

def run_pipeline():
    try:
        logger.info("ML Pipeline started")

        # 1️⃣ Data Ingestion
        ingestion = DataIngestion()

        df = ingestion.load_from_s3()

        ingestion.save_sample(df)

        # 2️⃣ Data Preprocessing
        preprocessor = DataPreprocessor(df)
        cleaned_df = preprocessor.preprocess()

        # 3️⃣ Save cleaned data
        cleaned_path = "data/cleaned/cleaned_travel.csv"
        os.makedirs(os.path.dirname(cleaned_path), exist_ok=True)
        preprocessor.save_cleaned_data(cleaned_path)

        # 4️⃣ Model Training
        trainer = ModelTrainer(cleaned_df)
        trainer.transform_data().train()

        logger.info("ML Pipeline executed successfully")

    except Exception as e:
        logger.exception("Pipeline failed due to an unexpected error")
        raise e


if __name__ == "__main__":
    run_pipeline()















# from src.data_ingestion import ingest_data
# from src.preprocessing import preprocess_data

# from src.model_training import transform_data , train_model
# from utils.logger import get_logger


# logger = get_logger(__name__)   


# def run_pipeline(file_path : str , save_path : str = 'artifacts/best_model_pipeline.pkl') :

#     try :  
#         logger.info("Starting the pipeline")

#         df = ingest_data(file_path)
#         logger.info(f"Data Ingestion completed. Shape : {df.shape}")


#         df_clean = preprocess_data(df)
#         logger.info(f"Data Preprocessing completed. Shape : {df_clean.shape}")

#         X_train, X_test, y_train, y_test , preprocessor = transform_data(df_clean)
#         logger.info("Data Transformed and ready for training.")



#         model_pipeline, metrics = train_model(
#             X_train, X_test, y_train, y_test, preprocessor, save_path=save_path
#         )

#         logger.info("Pipeline completed successfully")

        
#         return model_pipeline, metrics
    
#     except Exception as e:
#         logger.exception(f"Pipeline failed ")
#         raise

# if __name__ == "__main__" :
#     file_path = "/Users/sarthaksharna/Prospenity_Modelling/Data/raw/Travel.csv"
#     save_path = "artifacts/best_model_pipeline.pkl"
#     run_pipeline(file_path)

