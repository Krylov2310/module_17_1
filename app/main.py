from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from routers import task, user

app = FastAPI()
info_ed = ('Домашнее задание по теме "Структура проекта. Маршруты и модели Pydantic.".<br>'
           'Цель: усвоить основные правила структурирования проекта с использованием FastAPI. Начать написание '
           'небольшого "API" для менеджмента задач пользователей.<br>'
           'Задача "Основные маршруты":<br>'
           'Студент Крылов Эдуард Васильевич<br>'
           'Дата: 30.11.2024г.')


# python -m uvicorn main:app
# Get
@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


@app.get("/info", response_class=HTMLResponse)
async def info():
    return info_ed


app.include_router(task.router)
app.include_router(user.router)
