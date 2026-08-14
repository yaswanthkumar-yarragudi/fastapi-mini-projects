from fastapi.responses import JSONResponse
from fastapi import Request

class regInvalid(Exception):
    def __init__(self,reg:str, reason:str):
        self.reg = reg
        self.reason = reason

class regNotFound(Exception):
    def __init__(self,reg):
        self.reg = reg

async def regInvalidHandler(req:Request, exc:regInvalid):
    return JSONResponse(
        status_code=400,
        content={
            "error":"Reg.No is invalid",
            "message":f"Invalid Reg.No {exc.reg} provided",
            "reason":exc.reason,
            "reg":exc.reg
        }
    )
        
async def regNotFoundHandler(req:Request, exc:regNotFound):
    return JSONResponse(
        status_code=404,
        content={
            "error":"Reg.No not found",
            "message":f"Provided Reg.no {exc.reg} not found in DB",
            "reg":exc.reg
        }
    )