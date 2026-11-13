from fastapi import FastAPI, HTTPException
import sys  # <--- Этот импорт нигде не используется, из-за чего flake8 выдаст ошибку (красный билд)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "убубубубуб"}

@app.get("/status")
def get_status():
    return {"status": "ok"}

@app.get("/search")
def search(q: str = ""):
    if not q:
        raise HTTPException(status_code=400, detail="Query is missing")
    return {"query": q, "results": []}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id == 999999:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}

@app.post("/items/")
def create_item(item: dict):
    if not item:
        raise HTTPException(status_code=422, detail="Validation error")
    return {"status": "success", "item": item}