from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome() -> str:
    return "Главная страница"

@app.get("/user")
async def user_3(username=str, age=int) -> str:
        return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

@app.get("/user/admin")
async def user_1() -> str:
        return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def user_2(user_id=int) -> str:
        return f"Вы вошли как пользователь № {user_id}"
