from fastapi import FastAPI, status, Depends, HTTPException
from src.db.session import engine, Base
from src.db.session import get_db
from src.schemas.spy_cats import CreateCat, UpdateCat, ShowCat
from src.db.repository.spy_cats import create_new_cat, update_cat, delete_cat, read_all_cats
from src.db.models.spy_cats import SpyCatAgency
from sqlalchemy.orm import Session
from uuid import UUID
from src.api.routers import api_router

Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(
        title="Spy Cat Agency",
        version="0.0.1",
        contact=dict(
            name="Dmytro Boiko the Amazing Programmer",
            url="https://github.com/dmytro-dexter",
            email="dmytroboiko007@gmail.com",
        )
    )
    include_router(app)
    return app


app = start_application()
