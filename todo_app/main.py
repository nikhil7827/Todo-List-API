from fastapi import FastAPI
from todo_app.routes import user_routes, todo_routes
from .database import Base

app = FastAPI(title="Todo List API")
app.include_router(user_routes.router, prefix="/api", tags=["User"])
app.include_router(user_routes.router, prefix="/api")
app.include_router(todo_routes.router, prefix="/api")
app.include_router(user_routes.router, prefix="/api", tags=["User"])
app.include_router(todo_routes.router, prefix="/api", tags=["Todo"])

from todo_app.database import Base, engine
from todo_app import models

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Todo List API is running"}

#if __name__ == "__main__":
#   app.run(debug=True)
