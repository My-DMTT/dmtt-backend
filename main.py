
import sentry_sdk
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.admin.sql_admin import app as a_router
from src.api.bot_controller.base import router as bot_router
from src.api.controllers.base import router as base_router

app = FastAPI(default_response_class=ORJSONResponse)


@app.get('/')
def get_work():
    return {"hello": "world"}


app.include_router(base_router)
app.include_router(bot_router)
app.mount("/", a_router)
