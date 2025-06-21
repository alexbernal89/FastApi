from sqlalchemy import create_engine, text
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from ..database import Base
from fastapi.testclient import TestClient
import pytest
from ..models import Todos, Users
from ..main import app
from ..routers.auth import bcrypt_context

# Validacion from ..routers.auth import get_current_user

SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass= StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Crea la metadata, validar si es así
#La Base que creas con declarative_base() es el mecanismo de registro. Las definiciones de las tablas (
# __tablename__, Column, etc.) residen en tus clases modelo que heredan de esa Base. Cuando llamas a
# Base.metadata.create_all(), estás actuando sobre la colección de todas esas definiciones de t
# ablas que se han ido acumulando en Base.metadata a medida que se definían tus
# modelos.
# Por eso, aunque el fragmento Base = declarative_base() no muestre tablas, la llamada Base.metadata.create_all()
# funciona porque tus clases modelo (como
# Todo), definidas en otro lugar e importadas,
#  ya registraron sus estructuras de tabla en esa Base.metadata.

Base.metadata.create_all(bind=engine)
# Crea la conexión a la base de datos
def override_get_db():
    db = TestingSessionLocal()
    try:
#En Python, la palabra clave yield se usa para crear generadores. A diferencia de return,
# que termina la ejecución de una función y devuelve un valor, yield pausa la ejecución de una función,
# devuelve un valor, y guarda el estado de la función para que pueda ser
# reanudada más tarde desde donde se quedó.
        yield db #PAUSA la función y devuelve el objeto 'db'
    finally:
        db.close()

# Se crea el usuario
def override_get_current_user():
    return {'user_name':'Alex', 'id':1, 'user_role':'admin'}

client= TestClient(app)
#Inserta las dependecias y las sobreescribe con las de prueba, estas están en todos
#Se definen los datos para las pruebas con fixture
# Yiel sirve para que se ejecute la funcion pricipal y luego ya se ejecuta el delete
@pytest.fixture
def test_todo():
    todo = Todos(
        title= "Learn to code!",
        description="Need learn everyday!",
        priority=5,
        complete=False,
        owner_id=1,
    )
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()

# Creación del usuario
@pytest.fixture
def test_user():
    user = Users(
    email = "alexbernal@alexbernal",
    user_name = "alexbernal",
    first_name = "Alex",
    last_name = "Bernal",
    hashed_password = bcrypt_context.hash("1234535454"),
    is_active = True,
    role = "Admin",
    phone_number = "12345",
    )
    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.commit()