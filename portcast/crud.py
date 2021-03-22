from sqlalchemy.orm import Session

from . import models, schemas

def get_container(db: Session, container_id: str):
    return db.query(models.Container).filter(models.Container.id == container_id).first()


def get_containers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Container).offset(skip).limit(limit).all()


def create_container(db: Session, container: schemas.ContainerCreate):
    db_container = models.Container(**container.dict())
    db.add(db_container)
    db.commit()
    db.refresh(db_container)
    return db_container


def get_transshipments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Transshipment).offset(skip).limit(limit).all()


def create_container_transshipment(db: Session, transshipment: schemas.TransshipmentCreate, container_id: str):
    db_transshipment = models.Transshipment(**transshipment.dict(), container_id=container_id)
    db.add(db_transshipment)
    db.commit()
    db.refresh(db_transshipment)
    return db_transshipment


def update_transshipment(db: Session, transshipment: schemas.TransshipmentCreate, transshipment_id: int):
    new_transshipment = models.Transshipment(**transshipment.dict())
    old_transshipment = db.query(models.Transshipment).filter(
        models.Transshipment.id == transshipment_id).first()
    old_transshipment.is_discharged = new_transshipment.is_discharged
    old_transshipment.is_loaded = new_transshipment.is_discharged
    old_transshipment.discharge_date= new_transshipment.discharge_date
    old_transshipment.loaded_date= new_transshipment.loaded_date
    old_transshipment.discharge_location = new_transshipment.discharge_location
    old_transshipment.loaded_location = new_transshipment.loaded_location
    old_transshipment.vessel = new_transshipment.vessel
    db.commit()
    return old_transshipment
