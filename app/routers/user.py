from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["user"])


# Главная
@router.get("/")
async def all_users():
    pass


# Информация
@router.get("/user_id")
async def user_by_id():
    pass


# Добавление
@router.post("/create")
async def create_user():
    pass


# Изменение
@router.put("/update")
async def update_user():
    pass


# Удаление
@router.delete("/delete")
async def delete_user():
    pass
