from fastapi import FastAPI
from exceptions import *
from models import *
from data import pincodes

app = FastAPI(
    title="Find Pincode ",
    description="This helps to find pincode"
)

app.add_exception_handler(pincodeNotFoundError, pincode_not_found_handler)
app.add_exception_handler(invalidPincode, invalid_pincode_handler)


@app.get("/")
def home():
    return {
        "message":"Welcome to know delivery pincodes"
    }


@app.get("/pincode/{pincode}", response_model=location_response)
def pincode_lookup(pincode:str):
    if len(pincode) != 6 or not pincode.isdigit():
        raise invalidPincode(pincode, "Must be exactly 6 digit")
    if pincode not in pincodes:
        raise pincodeNotFoundError(pincode)
    return pincodes[pincode]

@app.post("/pincode/bulk", response_model=bulk_response)
def bulk_lookup(req: bulk_req):
    results = []
    missing = []
    invalid = []
    for code in req.pincodes:
        if len(code)!=6 or not code.isdigit():
            invalid.append(code)
        if code in pincodes:
            results.append(pincodes[code])
        else:
            missing.append(code)

    return bulk_response(
        status=200,
        found=len(results),
        not_found=len(missing),
        invalid=len(invalid),
        results=results,
        missing=missing,
        invalid_pins=invalid
    )
