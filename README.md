# Farmacia Lara — React + FastAPI

Aplicación académica para administrar medicamentos con operaciones CRUD:
crear, consultar, actualizar y eliminar.

## Tecnologías
- Frontend: React + Vite, Axios, React Router y Lucide React.
- Backend: Python, FastAPI y Pydantic.
- Almacenamiento: lista en memoria (no usa MongoDB ni otra base de datos).
- Importante: los registros se borran al reiniciar el backend.

## Requisitos
- Python 3.10 o superior.
- Node.js LTS y npm.
- Git (para publicar en GitHub).

## 1. Ejecutar el backend (terminal 1)
Desde la carpeta raíz `farmacia-lara`:

### Windows PowerShell
```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
uvicorn main:app --reload
```

Si PowerShell bloquea la activación del entorno, usa:
```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn main:app --reload
```
En ese caso, ejecuta los comandos usando `.\.venv\Scripts\python.exe` desde `backend`.

API: http://127.0.0.1:8000
Documentación interactiva: http://127.0.0.1:8000/docs

## 2. Ejecutar el frontend (terminal 2)
Desde la carpeta raíz `farmacia-lara`:
```powershell
cd frontend
npm install
npm run dev
```
Abre la dirección que muestre Vite, normalmente http://localhost:5173.

## Variables de entorno
Frontend: `frontend/.env` contiene `VITE_API_URL=http://127.0.0.1:8000`.
No pongas claves secretas en variables `VITE_`: se exponen al navegador.

## Funcionalidades
- Listar y buscar medicamentos.
- Crear medicamentos.
- Editar medicamentos.
- Eliminar medicamentos.
- Validaciones básicas.
- Mensajes de éxito/error.

## GitHub (cuando ya funcione)
Desde la carpeta raíz:
```powershell
git init
git add .
git commit -m "Proyecto inicial Farmacia Lara"
git branch -M main
```
Crea un repositorio vacío en https://github.com/new sin README, licencia ni `.gitignore`.
Luego copia la URL HTTPS del repositorio y ejecuta:
```powershell
git remote add origin PEGA_AQUI_LA_URL_HTTPS
git push -u origin main
```
No escribas literalmente `PEGA_AQUI_LA_URL_HTTPS`: reemplázalo por la URL real del repositorio.

## Nota académica
Esta versión NO usa MongoDB. Almacena los registros en memoria y se reinician al apagar/reiniciar el backend. Si la guía o el instructor exigen MongoDB, solicita autorización para entregar esta variante.
