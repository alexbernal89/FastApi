from ..routers.todos import get_db, get_current_user
#from ..main import app
from fastapi import status
#from ..models import Todos
from .utils import *


app.dependency_overrides[get_db]=override_get_db
app.dependency_overrides[get_current_user]=override_get_current_user



def test_read_all_authenticated(test_todo):
    response = client.get("/todos")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{'title': 'Learn to code!',
                                 'description': 'Need learn everyday!',
                                 'complete': False,
                                 'priority': 5,
                                 'id': 1,
                                 'owner_id': 1}]
# Con el path se identifica la función a testear
def test_read_one_authenticated(test_todo):
    response = client.get("/todos/todo/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'title': 'Learn to code!',
                                 'description': 'Need learn everyday!',
                                 'complete': False,
                                 'priority': 5,
                                 'id': 1,
                                 'owner_id': 1}

def test_read_one_authenticated_not_found(test_todo):
    response = client.get("/todos/todo/999")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Todo not found'}


def test_create_todo(test_todo):
    request_data = {'title': 'New book',
    'description': 'Book about developments',
    'priority': 5,
    'complete': False,
                    }
    response = client.post("/todos/todo", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED

def test_create_todo(test_todo):
    request_data = {'title': 'New book',
    'description': 'Book about developments',
    'priority': 5,
    'complete': False,
                    }
    response = client.post("/todos/todo", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED

    # Chequear la base de datos
    db = TestingSessionLocal()
    model =db.query(Todos).filter(Todos.id == 2).first()
    assert model.title == request_data.get('title')
    assert model.description == request_data.get('description')
    assert model.priority == request_data.get('priority')
    assert model.complete == request_data.get('complete')

def test_update_todo(test_todo):
    request_data = {'title': 'New description book',
    'description': 'Book about developments',
    'priority': 5,
    'complete': False,
                    }
    response = client.put("/todos/todo/1", json=request_data)
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Chequear la base de datos
    db = TestingSessionLocal()
    model =db.query(Todos).filter(Todos.id == 1).first()
    assert model.title == 'New description book'

def test_update_todo_not_found(test_todo):
    request_data = {'title': 'New description book',
    'description': 'Book about developments',
    'priority': 5,
    'complete': False,
                    }
    response = client.put("/todos/todo/4", json=request_data)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail':'Todo not found'}

def test_delete_todo(test_todo):
    response = client.delete('/todos/delete/todo/1')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model is None

def test_delete_todo():
    response = client.delete('/todos/delete/todo/999')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'Todo not found'}