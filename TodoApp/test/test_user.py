from .utils import *
from ..routers.users import get_db, get_current_user
from fastapi import status


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

# El usuario no esta la base de datos, corresponde al usuario en Mock
def test_return_user(test_user):
    response = client.get("/users/user_description")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['email'] == 'alexbernal@alexbernal'
    assert response.json()['user_name'] == 'alexbernal'
    assert response.json()['first_name'] == 'Alex'
    assert response.json()['last_name'] == 'Bernal'
    assert response.json()['role'] == 'Admin'
    assert response.json()['phone_number'] == '12345'



def test_password_change_success(test_user):
    response = client.put("/users/", json={"password":"newpassword",
                                           "old_password":"1234535454", "role": "Admin"}
                          )
    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_password_change_invalid_current_password(test_user):
    response = client.put("/users/", json={"password":"wronwpassword",
                                           "old_password":"newpassword", "role": "Admin"}
                          )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Error on password change'}


def test_update_phone_number_success(test_user):
    response = client.put("/users/update_phone", json={'phone_number':'12345'})

    assert response.status_code == status.HTTP_204_NO_CONTENT
