from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.db.models.spy_cats import SpyCatAgency
from src.schemas.spy_cats import CreateCat, UpdateCat
from uuid import UUID
from functools import wraps


# def transactional(func):
#     @wraps(func)
#     def wrapper(db_session, *args, **kwargs):
#         try:
#             result = func(*args, **kwargs)
#             db_session.commit()
#             return result
#         except Exception as e:
#             db_session.rollback()
#             raise e
#
#     return wrapper


def get_cat_by_id(cat_id: UUID, db: Session):
    db_cat = db.query(SpyCatAgency).filter(SpyCatAgency.id == cat_id).first()
    if not db_cat:
        raise HTTPException(status_code=400, detail=f"Cat ID {cat_id} not found")
    return db_cat


def create_new_cat(spy_cat: CreateCat, db: Session):
    cat = SpyCatAgency(
        name=spy_cat.name,
        years_of_experience=spy_cat.years_of_experience,
        salary=spy_cat.salary,
        is_available=spy_cat.is_available,
    )

    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat


def update_cat(id: UUID, cat: UpdateCat, db: Session):
    cat_object = get_cat_by_id(id, db)
    if not cat_object:
        return {"error": "Cat with this id doesn't exist"}
    for key, value in cat:
        setattr(cat_object, key, value)
    db.add(cat_object)
    db.commit()
    return cat_object


def delete_cat(id: UUID, db: Session):
    cat_object = get_cat_by_id(id, db)
    if not cat_object:
        return {"error": "Cat with this id doesn't exist"}
    db.delete(cat_object)
    db.commit()


def read_all_cats(db: Session):
    return db.query(SpyCatAgency).all()
