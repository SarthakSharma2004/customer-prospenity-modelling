import os
import pandas as pd
import joblib
from utils.logger import get_logger
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from xgboost import XGBClassifier

logger = get_logger(__name__)


class ModelTrainer:
    """
    Handles data transformation, model training, evaluation, and saving the final model pipeline.
    """

    def __init__(self , df : pd.DataFrame , target_col : str = 'ProdTaken') :
        self.df = df
        self.target_col = target_col
        self.X_train = self.X_test = self.y_train = self.y_test = None
        self.preprocessor = None
        self.pipe = None
        self.metrics = {}

    def transform_data(self, test_size : float = 0.2, random_state: int = 42):
         """Split data and create preprocessing pipeline."""
        
         try:
            logger.info("Data Transformation started")

            # Split into features and target
            X = self.df.drop(self.target_col, axis=1)
            y = self.df[self.target_col]

            logger.info("Defined dependent and independent variables")

            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state
            )

            logger.info("Split data into train and test sets")

            num_cols = self.X_train.select_dtypes(include=["int", "float"]).columns.tolist()

            cat_cols = self.X_train.select_dtypes(include=["object"]).columns.tolist()

            logger.info(f"Numeric columns: {num_cols}")
            logger.info(f"Categorical columns: {cat_cols}")

            # Define transformers
            num_transformer = StandardScaler()

            cat_transformer = OneHotEncoder(handle_unknown="ignore", drop="first")

             # Create preprocessor
            self.preprocessor = ColumnTransformer(
                transformers=[
                    ("cat", cat_transformer, cat_cols),
                    ("num", num_transformer, num_cols),
                ],
                remainder="passthrough",
            )
            logger.info("Defined ColumnTransformer for preprocessing")

            return self 
        
         except Exception as e:
            logger.exception("Error in data transformation")
            raise e
        

    def train(self, save_path: str = "artifacts/best_model_pipeline.pkl") :

        """Train model, evaluate performance, and save pipeline."""

        try :
            if self.X_train is None or self.preprocessor is None:
                raise ValueError("Data not transformed. Run transform_data() before training.")

            logger.info("Training model started")

            scale_pos = self.y_train.value_counts()[0] / self.y_train.value_counts()[1]
            logger.info(f"⚖️ Calculated class imbalance ratio: {scale_pos:.2f}")

            # Initialize model
            model = XGBClassifier(
                reg_alpha=0.1,
                reg_lambda=5,
                random_state=42,
                use_label_encoder=False,
                eval_metric="logloss",
                scale_pos_weight=scale_pos,
            )

            logger.info(f"Model initialized with params: {model.get_params()}")

            # Create pipeline
            
            self.pipe = Pipeline(steps = [("preprocessor", self.preprocessor), ("model", model)])
            logger.info("Pipeline created")

            # Train model
            self.pipe.fit(self.X_train, self.y_train)
            logger.info("Model trained successfully")

            # Predictions
            y_pred = self.pipe.predict(self.X_test)

            # Evaluation metrics
            self.metrics = {
                "accuracy": accuracy_score(self.y_test, y_pred),
                "precision": precision_score(self.y_test, y_pred),
                "recall": recall_score(self.y_test, y_pred),
                "f1": f1_score(self.y_test, y_pred),
                "confusion_matrix": confusion_matrix(self.y_test, y_pred)
            }
            logger.info(f"Model Evaluation Metrics: {self.metrics}")

            # Save model
            dir_name = os.path.dirname(save_path)
            if dir_name :
                os.makedirs(dir_name , exist_ok = True)
            joblib.dump(self.pipe, save_path)
            logger.info(f"Model pipeline saved to {save_path}")

            return self.pipe, self.metrics
        
        except Exception as e:
            logger.exception("Error in model training")
            raise e


        













# import pandas as pd
# import joblib
# import os
# from utils.logger import get_logger


# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler , OneHotEncoder
# from sklearn.compose import ColumnTransformer
# from xgboost import XGBClassifier
# from sklearn.pipeline import Pipeline
# from sklearn.metrics import accuracy_score , precision_score , recall_score , f1_score , roc_auc_score , confusion_matrix

# logger = get_logger(__name__)

# ''' THIS FUNCTION IS DESIGNED TO SPLIT THE DATA INTO TRAIN AND TEST SETS
#     AND CREATE A PREPROCESSOR THAT TRANSFORM CATEGORICAL AND NUMERICAL VARIABLES '''

# def transform_data(df : pd.DataFrame , test_data : float = 0.2 , random_state : int = 42) :

#     try :
#         logger.info("Data Transformation started..")

#         # SPLITTING INTO X AND Y
        
#         X = df.drop('ProdTaken' , axis = 1)
#         y = df['ProdTaken']
#         logger.info('Defined dependent and independent variables')

#         X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_data , random_state = random_state)
#         logger.info("Splitted into train and test")


#         # TRANSFORMING CATEGORICAL AND NUMERICAL VARIABLES
#         num_cols = X_train.select_dtypes(include = ['int']).columns.tolist()
#         cat_cols = X_train.select_dtypes(include = ['object']).columns.tolist()

#         num_transformer = StandardScaler()
#         cat_transformer = OneHotEncoder(handle_unknown = 'ignore' , drop = 'first')

#         logger.info(f"Columns before transformation : {num_cols} , {cat_cols}")

#         preprocessor = ColumnTransformer(

#             transformers = [

#             ('OneHotEncoder', cat_transformer, cat_cols) , 
#             ('standardScaler' , num_transformer, num_cols)

#             ], remainder='passthrough'
#         )

#         logger.info("Defined column transformer")

#         return X_train , X_test , y_train , y_test , preprocessor
    
#     except Exception as e :
#         logger.error(f"Error in data transformation : {e}")
#         raise

       
    
    
# def train_model(X_train, X_test , y_train, y_test , preprocessor ,  save_path = 'artifacts/best_model_pipeline.pkl') :
        
#         try :
#             scale_pos = y_train.value_counts()[0] / y_train.value_counts()[1]

            
#             model = {"XGBClassifier" : XGBClassifier(reg_alpha = 0.1, reg_lambda = 5, random_state = 42 , use_label_encoder = False , eval_metric = 'logloss' , scale_pos_weight = scale_pos)
#             }

#             for name , model in model.items() :
#                 logger.info(f"Model : {name} , Parameters : {model.get_params()}")
                
#                 pipe = Pipeline(steps = [('preprocessor' , preprocessor) , ('model' , model)])
#                 pipe.fit(X_train , y_train)

#                 logger.info("Pipeline trained successfully")
#                 y_pred = pipe.predict(X_test)

#                 # Evaluation metrics
#                 metrics = {
#                 'accuracy': accuracy_score(y_test, y_pred),
#                 'precision': precision_score(y_test, y_pred),
#                 'recall': recall_score(y_test, y_pred),
#                 'f1': f1_score(y_test, y_pred)
#                 }

#                 logger.info(f"Metrics: {metrics}")

#                 # SAVE THE PIPELINE
#                 if os.path.dirname(save_path):
#                     os.makedirs(os.path.dirname(save_path), exist_ok=True)

#                 joblib.dump(pipe , save_path)
#                 logger.info(f"Pipeline saved to {save_path}")

#             return pipe , metrics

#         except Exception as e:
#             logger.exception("Error in model training")
#             raise







       