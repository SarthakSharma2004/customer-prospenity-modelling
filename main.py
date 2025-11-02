from fastapi import FastAPI
from fastapi.responses import JSONResponse
import joblib

from schema.user_input import UserInput
from predict import predict_output , MODEL_VERSION , model_pipeline
from schema.prediction_response import PredictionResponse


app = FastAPI()


@app.get("/")
def read_root() :
    return {"Customer Prosperity_Modelling" : "Welcome to the Customer Prosperity Modelling API"}


@app.get("/health")
def health_check() :
    return {"status" :"ok" , "version" : MODEL_VERSION , "model_loaded" : model_pipeline is not None}



@app.post("/predict" , response_model = PredictionResponse)
def predict_prospenity(data : UserInput) :

    input_data = {

        'Age': data.Age,
        'TypeofContact': data.TypeofContact,
        'CityTier': data.CityTier,
        'DurationOfPitch': data.DurationOfPitch,
        'Occupation': data.Occupation,
        'Gender' : data.Gender,
        'NumberOfFollowups' : data.NumberOfFollowups,
        'ProductPitched' : data.ProductPitched,
        'PreferredPropertyStar' : data.PreferredPropertyStar,
        'MaritalStatus' : data.MaritalStatus,
        'NumberOfTrips' : data.NumberOfTrips,
        'Passport' : data.Passport,
        'PitchSatisfactionScore' : data.PitchSatisfactionScore,
        'OwnCar' : data.OwnCar,
        'Designation' : data.Designation,
        'MonthlyIncome' : data.MonthlyIncome,
        'TotalPersonVisiting' : data.total_person_visiting,
        'isChildrenVisiting' : data.is_children_visiting

    }

    try :
        prediction = predict_output(input_data)

        return JSONResponse(status_code = 200 , content = prediction)
    
    except Exception as e :
        return JSONResponse(status_code=500, content={"error": str(e)})


