from fastapi import FastAPI
from models import *
from exceptions import *
from data import students


app = FastAPI(
    title="student manager",
    description="This allows user to access the info of the student with reg.no",
    version="1.2.1"
)

@app.get("/")
def home():
    return {
        "message":"Welcome to check progress report of your child"
    }

app.add_exception_handler(regInvalid,regInvalidHandler)
app.add_exception_handler(regNotFound,regNotFoundHandler)


@app.get("/reg/{reg}",response_model=regResponse)
def search_reg(reg:str):
    if len(reg) != 5 or not reg.isdigit():
        raise regInvalid(reg, "Reg.No need to have 5 digits")
    if reg not in students:
        raise regNotFound(reg)
    return students[reg]

@app.post("/reg/bulk",response_model=bulkResponse)
def bulk(req:bulkReq):
    found = []
    missing = []
    invalid = []
    for num in req.regs:
        if len(num) != 5 or not num.isdigit():
            invalid.append(num)
        if num in students:
            found.append(students[num])
        else:
            missing.append(num)
    return bulkResponse(
        status=200,
        found=found,
        not_found=missing,
        invalid=invalid,
        found_count=len(found),
        not_found_count=len(missing),
        invalid_count=len(invalid)
    )