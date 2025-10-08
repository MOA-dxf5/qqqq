from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API", description="Simple API")

class Item(BaseModel):
    id: int
    name: str
    description: str = None

items = []

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/api/items", response_model=List[Item])
async def get_items():
    return items

@app.post("/api/items", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    return item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
