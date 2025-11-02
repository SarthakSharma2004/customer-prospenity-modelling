import joblib
import pandas as pd
import numpy as np

PIPELINE_PATH = "artifacts/best_model_pipeline.pkl"
model_pipeline = joblib.load(PIPELINE_PATH)

MODEL_VERSION = "1.0.0"



def predict_output(user_input: dict):

    """
    Takes user input as a dictionary and returns:
    - predicted class as 'Will Buy' or 'Will Not Buy'
    - probability of the predicted class
    - full probability distribution
    """
    # Convert input to DataFrame
    df = pd.DataFrame([user_input])

    # Predict using the pipeline
    pred_class = model_pipeline.predict(df)[0]
    pred_proba = model_pipeline.predict_proba(df)[0]  # returns [prob_class_0, prob_class_1]

    # Human-readable prediction
    pred_label = "Likely To Buy" if pred_class == 1 else "Not Likely To Buy"

    # Confidence of the predicted class
    confidence = pred_proba[pred_class]

    # Return dictionary with all info
    
    return {
        "prediction": pred_label,
        "confidence": float(confidence),
        "probabilities": {
            "Will Not Buy": float(pred_proba[0]),
            "Will Buy": float(pred_proba[1])
        }
    }