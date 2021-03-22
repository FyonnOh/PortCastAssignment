from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#post container
@app.post("/containers/", response_model=schemas.Container)
def create_container(container: schemas.ContainerCreate, db: Session = Depends(get_db)):
    db_container = crud.get_container(db, container_id=container.id)
    if db_container:
        raise HTTPException(status_code=400, detail="Container already registered")
    return crud.create_container(db=db, container=container)

#get containers
@app.get("/containers/", response_model=List[schemas.Container])
def read_containers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    containers = crud.get_containers(db, skip=skip, limit=limit)
    return containers

#get container
@app.get("/containers/{container_id}", response_model=schemas.Container)
def read_container(container_id: str, db: Session = Depends(get_db)):
    db_container = crud.get_container(db, container_id=container_id)
    if db_container is None:
        raise HTTPException(status_code=404, detail="container not found")
    return db_container

#get containers' transshipment
@app.post("/containers/{container_id}/transshipments/", response_model=schemas.Transshipment)
def create_transshipment_for_container(
    container_id: str, transshipment: schemas.TransshipmentCreate, db: Session = Depends(get_db)
):
    return crud.create_container_transshipment(db=db, transshipment=transshipment, container_id=container_id)

#get transshipments
@app.get("/transshipments/", response_model=List[schemas.Transshipment])
def read_transshipments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    transshipments = crud.get_transshipments(db=db, skip=skip, limit=limit)
    return transshipments


@app.put("/transshipments/{transshipment_id}/", response_model=schemas.Transshipment)
def update_transshipment(transshipment_id: int, transshipment: schemas.TransshipmentCreate, db: Session = Depends(get_db)):
    transshipment = crud.update_transshipment(db=db, transshipment_id=transshipment_id, transshipment=transshipment)
    return transshipment
