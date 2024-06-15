import json
import logging

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from healthcheck import HealthCheck
from app.api import receive_upload_file
from app.api import list_status_file
from app.database.database import init_db


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
    "/health", lambda: HealthCheck(), summary="HealthCheck", tags=["Info"]
)
app.include_router(receive_upload_file.router, tags=["Upload of the files .csv"])

app.include_router(list_status_file.router, tags=["List status of sent files"])


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


db = init_db(app)


@app.on_event("startup")
async def startup():
    # TODO se der tempo colocar um schedule para envido de email/boleto
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
