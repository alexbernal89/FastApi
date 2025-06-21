Start App
1. Located in /users/alexbernal/Documents/Python/PycharmProjects/fastapi/TodoApp
2. Create the environment in /users/alexbernal/Documents/Python/PycharmProjects/fastapi/TodoApp/env_TodoApp
3. Update pip install --upgrade pip
4. Install requirements: pip install -r requirements.txt
5. Initiate the project
uvicorn main:app --reload
uvicorn TodoApp.main:app --reload
6. Validar los contratos: http://127.0.0.1:8000/docs

Users DB
alexbernal

Ejecución de test
1. pytest --disable-warnings -v     