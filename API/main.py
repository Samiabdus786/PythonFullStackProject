# Frontend ---> API ---> logic ---> db ---> Response
# api/main.py

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.logic import ItemManager


# ------------------------------- App Setup -------------------------------
app = FastAPI(
    title="PyFoodGuardian - Smart Pantry & Food Expiry Tracker",
    version="1.0"
)

# Allow frontend (Streamlit / React) to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create an ItemManager instance (business logic)
item_manager = ItemManager()

# ------------------------- Data Models -------------------------
class ItemCreate(BaseModel):
    """
    Schema for creating an item
    """
    item_name: str
    category: str = None
    quantity: int
    purchase_date: str
    expiry_date: str

class ItemUpdate(BaseModel):
    """
    Schema for updating an item
    """
    updates: dict

# ------------------------- Endpoints -------------------------
@app.get("/")
def home():
    """
    Check if the API is running
    """
    return {"message": "PyFoodGuardian API is running!"}

@app.get("/items")
def get_items():
    """
    Get all items
    """
    return item_manager.get_items()

@app.get("/items/{item_id}")
def get_item(item_id: int):
    """
    Get a single item by ID
    """
    result = item_manager.get_item(item_id)
    if not result.get("Success"):
        raise HTTPException(status_code=404, detail=result.get("Message"))
    return result

@app.post("/items")
def create_item(item: ItemCreate):
    """
    Create a new item
    """
    result = item_manager.add_item(
        item.item_name,
        item.category,
        item.quantity,
        item.purchase_date,
        item.expiry_date
    )
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemUpdate):
    """
    Update fields of an item
    """
    result = item_manager.update_item(item_id, item.updates)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """
    Delete an item
    """
    result = item_manager.delete_item(item_id)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result


# --- Run ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
