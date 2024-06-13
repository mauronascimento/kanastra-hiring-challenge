import json
import logging

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from healthcheck import HealthCheck
from app.api import receive_upload_file
from app.database.database import SessionLocal, init_db

# from sqlalchemy.orm import Session
# from models import Charge
# from database import SessionLocal, init_db
# from schemas import ChargeCreate, ChargeInDB

log = logging.getLogger()

app = FastAPI(
    title="Kanastra-Hiring-Challenge",
    description="API para teste Kanastra-Hiring-Challenge",
    openapi_url="/doc/api",
    redoc_url="/doc/redoc",
    docs_url="/doc/api.json",
    debug=True,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_api_route(
    "/health",
    lambda: HealthCheck(),
    summary="HealthCheck",
    tags=["Info"],
)
app.include_router(
    receive_upload_file.router,
    tags=["Upload de arquivo csv"],
)


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    response = {"erro": exc.detail}
    return JSONResponse(response, status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    erros = json.loads(exc.json())
    formatted_erro = list(map(formt_response_error, erros))
    response = {"erro": formatted_erro[0]}
    log.error(formatted_erro[0])
    return JSONResponse(response, status_code=422)


def formt_response_error(erro: dict) -> dict:
    return {"code": 422, "message": "=>".join(map(str, erro["loc"]))}

@app.on_event("startup")
def startup_event():
    init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
#
# @app.get("/")
# def read_root():
#     return {"API live!"}
#
# @app.get("/hello")
# def read_root():
#     return {"Hello Kanastra!"}
#
# @app.post("/charges", response_model=ChargeInDB)
# def create_charge(charge: ChargeCreate, db: Session = Depends(get_db)):
#     db_charge = Charge(
#         name=charge.name,
#         government_id=charge.government_id,
#         email=charge.email,
#         debt_amount=charge.debt_amount,
#         debt_due_date=charge.debt_due_date
#     )
#     db.add(db_charge)
#     db.commit()
#     db.refresh(db_charge)
#     return db_charge
#
# @app.get("/charges/{government_id}/total")
# def get_total_debt(government_id: str, db: Session = Depends(get_db)):
#     charges = db.query(Charge).filter(Charge.government_id == government_id).all()
#     if not charges:
#         raise HTTPException(status_code=404, detail="No charges found for this Gov. ID")
#     total_debt_amount = sum(charge.debt_amount for charge in charges)
#     return total_debt_amount

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)