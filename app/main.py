from fastapi import FastAPI

from app.db import Base, engine
from app.routers import warehouses, packages

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Warehouse & Package Management API")

app.include_router(warehouses.router)
app.include_router(packages.router)

