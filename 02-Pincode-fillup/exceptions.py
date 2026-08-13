from fastapi.responses import JSONResponse
from fastapi import Request


class pincodeNotFoundError(Exception):
    def __init__(self, pincode:str ):
        self.pincode = pincode

class invalidPincode(Exception):
    def __init__(self, pincode:str, reason:str = "Invalid Format"):
        self.pincode =  pincode
        self.reason = reason

async def pincode_not_found_handler(req:Request , exc:pincodeNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "error":"pincode not found",
            "message":f"no mentioned location for pincode {exc.pincode}",
            "pincode":exc.pincode
        }
    )
async def invalid_pincode_handler(req:Request , exc:invalidPincode):
    return JSONResponse(
        status_code=400 ,
        content={
            "error":"pincode is invalid",
            "message":f"mentioned {exc.pincode} is invalid",
            "reason":exc.reason,
            "pincode":exc.pincode
        }
    )

