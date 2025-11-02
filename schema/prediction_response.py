# A RESPONSE MODEL DEFINES VALIDATES THE RESPONSE THAT API WILL RETURN
# IT WILL GENERATE CLEAN DOCS AND REMOVE UNNECESSARY DATA FROM RESPONSE

from pydantic import BaseModel , Field
from typing import Dict     

class PredictionResponse(BaseModel):
    prediction : str = Field(... , description = "Predicted class" , examples = ["Likely To Buy" , "Not Likely To Buy"])
    confidence : float = Field(... , ge = 0.0, le = 1.0 ,  description = "Confidence of the prediction")
    probabilities : Dict[str , float] = Field(... , description = "Probability of each class")