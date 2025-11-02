from pydantic import BaseModel, Field , field_validator , computed_field

from typing import List , Dict , Literal , Annotated


class UserInput(BaseModel) :
    Age: Annotated[int, Field(ge=0, le=120 , description="Age of the customer in years")]

    TypeofContact: Annotated[Literal['Self Enquiry', 'Company Invited'], Field(description="Type of contact made by the customer for enquiry")]

    CityTier: Annotated[Literal[1, 2, 3], Field(description="Tier of the city where the customer resides")]

    DurationOfPitch: Annotated[int , Field(ge=0 , description="Duration of the sales person pitch to the customer in minutes")]

    Occupation: Annotated[Literal['Salaried', 'Small Business', 'Large Business', 'Other'], Field(description="Occupation of the customer")]

    Gender: Annotated[Literal['Male', 'Female'] , Field(description="Gender of the customer")]

    NumberOfPersonVisiting: Annotated[int , Field(ge=0 , description="Total number of persons visiting including the customer")]

    NumberOfFollowups: Annotated[int , Field(ge=0 , description="Number of follow-ups made to the customer")]

    ProductPitched: Annotated[Literal['Basic', 'Deluxe', 'Standard', 'Super Deluxe' , 'King'], Field(description="Type of product pitched to the customer")]

    PreferredPropertyStar: Annotated[Literal[3, 4, 5], Field(description="Preferred star rating of the property by the customer")]

    MaritalStatus: Annotated[Literal['Married', 'Unmarried' , 'Divorced'], Field(description="Marital status of the customer")]

    NumberOfTrips: Annotated[int , Field(ge=0 , description="Number of trips made by the customer in the past")]

    Passport: Annotated[Literal['Yes', 'No'], Field(description="Whether the customer has a passport or not")]

    PitchSatisfactionScore: Annotated[int , Field(ge=1 , le=5 , description="Satisfaction score of the customer regarding the pitch")]

    OwnCar: Annotated[Literal['Yes', 'No'], Field(description="Whether the customer owns a car or not")]

    NumberOfChildrenVisiting: Annotated[int , Field(ge=0 , description="Number of children visiting with the customer")]

    Designation: Annotated[Literal['Executive' , 'Manager' , 'Senior Manager' , 'AVP' , 'VP'], Field(description="Designation of the customer in their occupation")]

    MonthlyIncome: Annotated[int , Field(ge=0 , description="Monthly income of the customer in local currency")]

    



    @field_validator('Passport')
    @classmethod
    def validate_passport(cls , value : str) -> int :
        return 1 if value == 'Yes' else 0
    
    @field_validator('OwnCar')
    @classmethod
    def validate_own_car(cls , value : str) -> Literal[0 , 1] :
        return 1 if value == 'Yes' else 0

    @computed_field
    @property
    def total_person_visiting(self) -> int :
        return self.NumberOfPersonVisiting + self.NumberOfChildrenVisiting
    
    @computed_field
    @property
    def is_children_visiting(self) -> int :
        return 1 if self.NumberOfChildrenVisiting > 0 else 0
    
    





