# API de estudiantes

Implementación de la práctica de endpoints siguiendo la estructura del README de referencia: `run.py`, una app Flask y un controlador organizado dentro de `v1/app/controllers`.

## Estructura

```text
tareas-plataformas-abiertas/
├── data/
├── v1/
│   ├── run.py
│   ├── app/
│   │   ├── __init__.py
│   │   └── controllers/
│   │       ├── __init__.py
│   │       └── estudiantes.py
│   └── public/
```

## Instalación y ejecución

Abre una terminal en la carpeta raíz del proyecto y ejecuta:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install flask flask-cors
cd v1
python run.py
```

La API queda disponible en `http://127.0.0.1:5000`. Mantén abierta la terminal mientras la estés probando.

## Endpoints

| Método | URL | Respuesta |
|---|---|---|
| GET | `http://127.0.0.1:5000/estudiantes/api/v1/` | Bienvenida general. Endpoint adicional porque la guía pide tres y solo describe dos. |
| GET | `http://127.0.0.1:5000/estudiantes/api/v1/hola` | Mensaje genérico de bienvenida. |
| GET | `http://127.0.0.1:5000/estudiantes/api/v1/saludo?nombre=Leonardo` | `{"saludo":"Hola Leonardo"}` |

Si se consulta `saludo` sin nombre, responde con estado HTTP 400 y:

```json
{"mensaje":"Debe de ingresar el nombre del estudiante."}
```

El endpoint `saludo` admite el nombre como parámetro de consulta (`?nombre=...`) o como JSON en el cuerpo del GET, para facilitar su prueba con el ejemplo de Postman del README.
