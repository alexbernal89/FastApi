from .utils import *
from ..routers.admin import get_db, get_current_user
from fastapi import status
from ..models import Todos


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_admin_read_all_authenticsted(test_todo):
    response = client.get("/admin/todo")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{'title': 'Learn to code!',
                                 'description': 'Need learn everyday!',
                                 'complete': False,
                                 'priority': 5,
                                 'id': 1,
                                 'owner_id': 1}]
def test_admin_delete(test_todo):
    response = client.delete("/admin/delete/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id==1).first()
    assert model is None

def test_admin_delete_not_found():
    response = client.delete("/admin/delete/9999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert  response.json() == {'detail':'Todo not found'}