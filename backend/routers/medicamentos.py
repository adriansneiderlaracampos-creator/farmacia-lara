from fastapi import APIRouter, HTTPException, status
from models import MedicamentoCrear, MedicamentoActualizar

router = APIRouter(prefix="/api/medicamentos", tags=["Medicamentos"])

# Almacenamiento temporal en memoria: no usa MongoDB.
medicamentos = []
siguiente_id = 1

@router.get("/")
def listar_medicamentos():
    return medicamentos

@router.get("/{id_medicamento}")
def consultar_medicamento(id_medicamento: int):
    for medicamento in medicamentos:
        if medicamento["id"] == id_medicamento:
            return medicamento
    raise HTTPException(status_code=404, detail="Medicamento no encontrado")

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_medicamento(datos: MedicamentoCrear):
    global siguiente_id

    for medicamento in medicamentos:
        if medicamento["nombre"].casefold() == datos.nombre.casefold():
            raise HTTPException(status_code=400, detail="Ya existe un medicamento con ese nombre")

    nuevo = {"id": siguiente_id, **datos.model_dump()}
    medicamentos.append(nuevo)
    siguiente_id += 1
    return nuevo

@router.put("/{id_medicamento}")
def actualizar_medicamento(id_medicamento: int, datos: MedicamentoActualizar):
    for indice, medicamento in enumerate(medicamentos):
        if medicamento["id"] == id_medicamento:
            cambios = datos.model_dump(exclude_unset=True, exclude_none=True)
            if not cambios:
                raise HTTPException(status_code=400, detail="Envía al menos un campo para actualizar")

            actualizado = {**medicamento, **cambios}
            for otro in medicamentos:
                if otro["id"] != id_medicamento and otro["nombre"].casefold() == actualizado["nombre"].casefold():
                    raise HTTPException(status_code=400, detail="Ya existe otro medicamento con ese nombre")

            medicamentos[indice] = actualizado
            return actualizado

    raise HTTPException(status_code=404, detail="Medicamento no encontrado")

@router.delete("/{id_medicamento}")
def eliminar_medicamento(id_medicamento: int):
    for indice, medicamento in enumerate(medicamentos):
        if medicamento["id"] == id_medicamento:
            medicamentos.pop(indice)
            return {"mensaje": "Medicamento eliminado correctamente", "id": id_medicamento}

    raise HTTPException(status_code=404, detail="Medicamento no encontrado")
