
import sentry_sdk
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.admin.sql_admin import app as a_router
from src.api.bot_controller.base import router as bot_router
from src.api.controllers.base import router as base_router

app = FastAPI(default_response_class=ORJSONResponse)

sentry_sdk.init(
    dsn="https://4e9750c0af51f5f7a6b26ed2d4c21456@o4507315900383232.ingest.de.sentry.io/4507315902808144",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)


@app.get('/')
def get_work():
    return {"hello": "world"}


app.include_router(base_router)
app.include_router(bot_router)
app.mount("/", a_router)
