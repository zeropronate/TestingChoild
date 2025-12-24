from typing import Optional, List

from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session



router = APIRouter(prefix="/warehouses", tags=["warehouses"])


def _serialize_warehouse(warehouse: models.Warehouse) -> dict:
    return {
        "id": warehouse.id,
        "name": warehouse.name,
        "city": warehouse.city,
        "handling_fee": warehouse.handling_fee,
    }


@router.post("/")
def create_warehouse():
    warehouse = warehouse_service.create_warehouse()
    return _serialize_warehouse(warehouse)


@router.get("/")
def list_warehouses():
    warehouses = warehouse_service.list_warehouses()
    return [_serialize_warehouse(w) for w in warehouses]


@router.put("")
def update_warehouse():
    warehouse = warehouse_service.update_warehouse()
    return _serialize_warehouse(warehouse)


@router.delete("/")
def delete_warehouse():
    warehouse_service.delete_warehouse()
    return {"detail": "deleted"}
