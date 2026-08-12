# from fastapi import FastAPI,Query,HTTPException
# from models import *
# from data import menu
# app = FastAPI(
#     title="Chai app",
#     description= "Read the menu in the displays"
# )

# @app.get("/")
# def home():
#     return {
#         "message":"Hello welcome to chai app"
#     }

# @app.get("/menu", response_model=menu_response)
# def items(category:str | None = Query(None,description="filter by category")):
#     if category:
#         filterd = [ item for item in menu if item["category"]==category.lower()]
#         if not filterd:
#             raise HTTPException(status_code=404,detail=f"{category} not found")
#         return menu_response(count=len(filterd),items=filterd)
#     return menu_response(count=len(menu),items=menu)

# @app.get("/menu/{id}", response_model=menu_item)
# def item(id:int):
#     for item in menu:
#         if item["id"] == id:
#             return item
#     raise HTTPException(status_code=404,detail=f"item with id {id} not found")

from fastapi import FastAPI,Query,HTTPException
from models import menu_item,menu_response
from data import menu

app = FastAPI(
    title="Demo Project",
    description="This is get based project focused on pydantic, httpresponse, query etc.."
)

@app.get("/")
def home():
    return {
        "message":"Welcome to Chai Point"
    }


@app.get("/menu",response_model=menu_response,)
def items(category:str | None =Query(None) ):
    if category:
        filtered = [ item for item in menu if item["category"]==category]
        if not filtered:
            raise HTTPException (status_code=404, detail=f"category {category} not found..")
        return menu_response( count=len(filtered), items=filtered)
    return menu_response(count=len(menu),items=menu)

# @app.get("/menu/{id}", response_model=menu_item)
# def item(id:int):
#     for item in menu:
#         if item["id"] == id:
#             return item

@app.get("/menu/{name}")
def itemname(name:str):
    for item in menu:
        if item["name"].lower() == name:
            return item
    raise HTTPException(status_code=404, detail=f"no item of name {name}")