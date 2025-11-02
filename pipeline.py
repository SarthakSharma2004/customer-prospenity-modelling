from src.data_ingestion import ingest_data
from src.preprocessing import preprocess_data

from src.model_training import transform_data , train_model
from utils.logger import get_logger


logger = get_logger(__name__)   


def run_pipeline(file_path : str , save_path : str = 'artifacts/best_model_pipeline.pkl') :

    try :  
        logger.info("Starting the pipeline")

        df = ingest_data(file_path)
        logger.info(f"Data Ingestion completed. Shape : {df.shape}")


        df_clean = preprocess_data(df)
        logger.info(f"Data Preprocessing completed. Shape : {df_clean.shape}")

        X_train, X_test, y_train, y_test , preprocessor = transform_data(df_clean)
        logger.info("Data Transformed and ready for training.")



        model_pipeline, metrics = train_model(
            X_train, X_test, y_train, y_test, preprocessor, save_path=save_path
        )

        logger.info("Pipeline completed successfully")

        
        return model_pipeline, metrics
    
    except Exception as e:
        logger.exception(f"Pipeline failed ")
        raise

if __name__ == "__main__" :
    file_path = "/Users/sarthaksharna/Prospenity_Modelling/Data/raw/Travel.csv"
    save_path = "artifacts/best_model_pipeline.pkl"
    run_pipeline(file_path)

