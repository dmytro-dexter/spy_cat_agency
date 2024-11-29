from fastapi import APIRouter
from fastapi import status, Depends
from src.db.session import get_db
from src.schemas.spy_cats import CreateCat, UpdateCat, ShowCat
from src.db.repository.spy_cats import create_new_cat, update_cat, delete_cat, read_all_cats, get_cat_by_id
from sqlalchemy.orm import Session
from uuid import UUID

api_router = APIRouter()


@api_router.post("/", response_model=ShowCat, status_code=status.HTTP_201_CREATED)
def create_cat(cat: CreateCat, db: Session = Depends(get_db)):
    cat = create_new_cat(cat, db)
    return cat


@api_router.get("/{cat_id}", status_code=status.HTTP_200_OK)
def read_cat_by_id(id: UUID, db: Session = Depends(get_db)):
    return get_cat_by_id(id, db)


@api_router.get("/", status_code=status.HTTP_200_OK)
def read_cats(db: Session = Depends(get_db)):
    return read_all_cats(db)


@api_router.put("/{cat_id}", status_code=status.HTTP_200_OK)
def update_cat_salary(id: UUID, cat: UpdateCat, db: Session = Depends(get_db)):
    return update_cat(id, cat, db)


@api_router.delete("/{cat_id}", status_code=status.HTTP_200_OK)
def delete_spy_cat(id: UUID, db: Session = Depends(get_db)) -> None:
    delete_cat(id, db)
