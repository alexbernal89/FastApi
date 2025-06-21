from .utils import *
from  ..routers.auth import SECRET_KEY,ALGORITHM, CreateUserRequest, Token, get_db,authenticate_user,create_access_token,get_current_user
from jose import jwt
from datetime import timedelta
import pytest
from fastapi import HTTPException


app.dependency_overrides[get_db]= override_get_db

def test_authenticate_user(test_user):
    db = TestingSessionLocal()

    authenticated_user = authenticate_user(test_user.user_name, "1234535454", db)
    assert authenticated_user is not None
    assert authenticated_user.user_name == test_user.user_name

    non_existent_user = authenticate_user('wrong_user', "1234535454", db)
    assert non_existent_user is False

    wrong_password = authenticate_user(test_user.user_name, "wronpassword", db)
    assert wrong_password is False

def test_create_access_token():
    user_name = 'testuser'
    user_id = 1
    role = 'user'
    expire_delta = timedelta(days=1)
    token = create_access_token(user_name, user_id, role, expire_delta)
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM],
                               options={'verify_signature': False})

    assert decoded_token['sub'] == user_name
    assert decoded_token['id'] == user_id
    assert decoded_token['role'] == role


@pytest.mark.asyncio
async def test_get_current_user_valid_token():
    encode = {'sub':'test_user', 'id':1, 'role': 'Admin'}
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
# Cuando se prueba una función asincronica necesitamos usar await
    user = await get_current_user(token =token)

    assert user == {'username':'test_user', 'id':1, 'user_role': 'Admin'}

@pytest.mark.asyncio
async def test_get_current_user_missing_payload():
    encode = {'role': 'Admin'}
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
# Cuando se prueba una función asincronica necesitamos usar await
    with pytest.raises(HTTPException) as exinfo:
        await get_current_user(token =token)

    assert exinfo.value.status_code == 401
    assert exinfo.value.detail == 'Could not validate user.'






