from pydantic import BaseModel,field_validator

class pincode_req(BaseModel):
    pincode: str

    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls, value):
        if len(value) != 6 or not value.isdigit():
            raise ValueError("The pincode must be number of length 6")
        return value

class location_response(BaseModel):
    pincode :str
    city: str
    district: str
    state: str

class bulk_req(BaseModel):
    pincodes: list[str]
    @field_validator("pincodes")
    @classmethod
    def validate_pincode(cls, values):

        if len(values) == 0:
            raise ValueError("atleast one pincode needed")
        if len(values) == 0:
            raise ValueError("Max 20 pincodes only allowed")

        return values

class bulk_response(BaseModel):
    status:int
    found:int
    not_found:int
    invalid:int
    results:list[location_response]
    missing:list[str]
    invalid_pins:list[str]