from typing import List, Optional

from pydantic import BaseModel


class TransshipmentBase(BaseModel):
    is_loaded: bool
    is_discharged: bool
    discharge_date: str
    loaded_date: str
    discharge_location: str
    loaded_location: str
    vessel: str


class TransshipmentCreate(TransshipmentBase):
    pass


class Transshipment(TransshipmentBase):
    id: int
    container_id: str

    is_loaded: bool
    is_discharged: bool
    discharge_date: str
    loaded_date: str
    discharge_location: str
    loaded_location: str
    vessel: str

    class Config:
        orm_mode = True

class ContainerBase(BaseModel):
    id: str
    final_pod: str
    final_pod_eta: str

class ContainerCreate(ContainerBase):
    pass

class Container(ContainerBase):
    id: str
    final_pod: str
    final_pod_eta: str
    transshipments: List[Transshipment] = []

    class Config:
        orm_mode = True

