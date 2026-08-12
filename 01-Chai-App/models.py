from pydantic import BaseModel

class menu_item(BaseModel):
    id:int
    name:str
    category:str
    price:int
    description:str 
    available:bool 

class menu_response(BaseModel):
    status:str="success"
    count:int
    items:list[menu_item]
