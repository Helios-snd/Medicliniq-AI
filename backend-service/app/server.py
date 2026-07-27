from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import v1_routes as routes
app = FastAPI(
    titile="MediCliniq AI",
    description="Intelligent Patient Intelligence Platform",
    version = "1.0.0",

)


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

for route in routes:
    app.include_router(route)

    