from typing import Union

from fastapi import FastAPI, Path

from typing import Annotated

users = {'1': {'username': 'Example', 'age': 18}}

app = FastAPI()

@app.get('/users/')
async def get_users() -> dict:
    '''
    запрос по маршруту '/users', который возвращает словарь users.
    '''
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: Annotated [str, Path(min_lenght = 5,
                                                  max_lenght = 20,
                                                  description = 'Имя пользователя',
                                                  example = 'Urban')],
                      age: Annotated [int, Path(le = 120,
                                               ge = 16,
                                               description = 'Возраст пользователя',
                                               example = 30)]) -> str:
    '''
    запрос который добавляет в словарь по максимальному по значению ключом значение строки "Имя: {username}, возраст: {age}". 
    И возвращает строку "User <user_id> is registered".
    '''
    user_id = int(max(next(reversed(users)))) + 1 
    users[str(user_id)] = {'username': username, 'age': age}
    return f'User {user_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated [int, Path(ge = 1)],
                    username: Annotated [str, Path(min_lenght = 5,
                                                      max_lenght = 20,
                                                      description = 'Имя пользователя',
                                                      example = 'Urban')],
                    age: Annotated [int, Path(le = 120,
                                               ge = 16,
                                               description = 'Возраст пользователя',
                                               example = 30)]) -> str:
    '''
    запрос который обновляет значение из словаря users под ключом user_id на строку "Имя: {username}, возраст: {age}". 
    И возвращает строку "The user <user_id> is updated"
    '''
    users[str(user_id)] = {'username': username, 'age': age}
    return f'The user {user_id} is updated'

@app.delete('/user/{user_id}')
async def delit_user(user_id: Annotated [int, Path(ge = 1)]) -> str:
    '''
    запрос который удаляет из словаря users по ключу user_id пару.
    И возвращает строку "The user <user_id> is delited"
    '''
    if str(user_id) in users.keys():
        users.pop(str(user_id))
        return f'The user {user_id} is delited'
    else:
        return f'The user {user_id} is not found'
    