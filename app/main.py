from fastapi import FastAPI
from .api.endpoints import claims

app = FastAPI()

# Include routers from different modules
app.include_router(claims.router, prefix="/claims", tags=["claims"])