from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Container(Base):
    __tablename__ = "containers"

    id = Column(String, primary_key=True)
    final_pod = Column(String)
    final_pod_eta = Column(String)

    transshipment = relationship("Transshipment", back_populates="container")


class Transshipment(Base):
    __tablename__ = "transshipments"

    id = Column(Integer, primary_key=True, index=True)
    is_loaded = Column(Boolean, default=True)
    is_discharged = Column(Boolean, default=False)
    discharge_date= Column(String)
    loaded_date= Column(String)
    discharge_location= Column(String)
    loaded_location= Column(String)
    vessel= Column(String)
    container_id = Column(String, ForeignKey("containers.id"))
    container = relationship("Container", back_populates="transshipment")
