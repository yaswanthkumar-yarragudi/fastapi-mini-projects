from pydantic import BaseModel,field_validator
from exceptions import *

class checkRegNo(BaseModel):
    reg:str

    @field_validator("reg")
    @classmethod
    def check(cls,value):
        """ Any Business Logic """
        return value

class regResponse(BaseModel):
    reg:str
    name:str
    group:str
    grade:str
    result:str

class bulkReq(BaseModel):
    regs:list[str]

    @field_validator("regs")
    @classmethod
    def check(cls,values):
        """ Any Business Logic """
        return values


class bulkResponse(BaseModel):
    status:int
    found:list[regResponse]
    not_found:list
    invalid:list
    found_count:int
    not_found_count:int
    invalid_count:int

    


               

     