from pydantic import BaseModel, Field
from typing import Optional

class MedicamentoCrear(BaseModel):
    nombre: str = Field(min_length=2, max_length=100)
    descripcion: str = Field(min_length=2, max_length=250)
    precio: float = Field(gt=0)
    cantidad: int = Field(ge=0)
    categoria: str = Field(min_length=2, max_length=60)

class MedicamentoActualizar(BaseModel):
    nombre: Optional[str] = Field(default=None, min_length=2, max_length=100)
    descripcion: Optional[str] = Field(default=None, min_length=2, max_length=250)
    precio: Optional[float] = Field(default=None, gt=0)
    cantidad: Optional[int] = Field(default=None, ge=0)
    categoria: Optional[str] = Field(default=None, min_length=2, max_length=60)
