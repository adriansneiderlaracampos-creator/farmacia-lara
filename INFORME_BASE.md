# Informe del proyecto: Farmacia Lara

## 1. Nombre del proyecto
Farmacia Lara — sistema web para la gestión de inventario de medicamentos.

## 2. Objetivo
Desarrollar una aplicación web que permita registrar, consultar, actualizar y eliminar medicamentos de una farmacia mediante una interfaz sencilla y una API REST.

## 3. Tecnologías utilizadas
- React y Vite: construcción de la interfaz.
- Axios: comunicación HTTP entre el frontend y el backend.
- React Router: navegación del frontend.
- FastAPI: creación de endpoints REST.
- Pydantic: validación de datos.
- Python: lógica del backend.

## 4. Funcionalidades
- Listado y búsqueda de medicamentos.
- Registro de medicamentos con nombre, descripción, precio, cantidad y categoría.
- Edición de medicamentos.
- Eliminación con confirmación.
- Resumen de unidades, productos con stock bajo y valor del inventario.
- Validación de campos y manejo básico de errores.

## 5. Endpoints
| Método | Ruta | Función |
|---|---|---|
| GET | `/api/medicamentos/` | Listar medicamentos |
| GET | `/api/medicamentos/{id}` | Consultar un medicamento |
| POST | `/api/medicamentos/` | Crear medicamento |
| PUT | `/api/medicamentos/{id}` | Actualizar medicamento |
| DELETE | `/api/medicamentos/{id}` | Eliminar medicamento |

## 6. Ejecución
El backend se inicia con `uvicorn main:app --reload` desde la carpeta `backend`. El frontend se inicia con `npm run dev` desde `frontend`. La API se consulta en `http://127.0.0.1:8000/docs`.

## 7. Almacenamiento y limitación
La versión entregada almacena los medicamentos en una lista de Python en memoria. No utiliza MongoDB ni otra base de datos. Los registros se pierden al reiniciar el backend. Si el requerimiento académico exige persistencia, debe adaptarse según la autorización del instructor.

## 8. Evidencias que debe agregar el estudiante
Inserte capturas reales de:
1. Pantalla principal del inventario.
2. Registro de un medicamento.
3. Medicamento visible en el listado.
4. Edición de un medicamento.
5. Confirmación de eliminación y listado actualizado.
6. Documentación interactiva de FastAPI (`/docs`).
7. Repositorio GitHub con archivos del proyecto.

## 9. Conclusión
El proyecto integra un frontend React con una API REST en FastAPI y demuestra las operaciones CRUD para administrar el inventario. Como mejora futura se recomienda incorporar una base de datos persistente si el alcance académico lo permite.
