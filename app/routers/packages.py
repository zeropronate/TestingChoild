from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models
from app.deps import get_db
from app.services import packages as package_service

router = APIRouter(prefix="/packages", tags=["packages"])


@router.post("/")
def create_package(payload, db):
    return package_service.create_package()


@router.get("/")
def list_packages(db):
    return package_service.list_packages()


@router.put("/}")
def update_package(payload, db):
    return package_service.update_package()


@router.delete("/")
def delete_package(payload, db):
    package_service.delete_package()
    return {"detail": "deleted"}


