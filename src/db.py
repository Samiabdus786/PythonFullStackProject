import os
from supabase import create_client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

# Create item
def create_item(item_name, category, quantity, purchase_date, expiry_date):
    response = supabase.table("items").insert({
        "item_name": item_name,
        "category": category,
        "quantity": quantity,
        "purchase_date": purchase_date,
        "expiry_date": expiry_date
    }).execute()
    return response.data


# Read (Fetch all items, latest first)
def get_items():
    response = supabase.table("items").select("*").order("created_at", desc=True).execute()
    return response.data

# Read (Fetch a single item by its ID)
def get_item_by_id(item_id: int):
    response = supabase.table("items").select("*").eq("item_id", item_id).execute()
    return response.data

# Update (Modify item details by ID)
def update_item(item_id: int, updates: dict):
    response = supabase.table("items").update(updates).eq("item_id", item_id).execute()
    return response.data

# Delete (Remove an item by ID)
def delete_item(item_id: int):
    response = supabase.table("items").delete().eq("item_id", item_id).execute()
    return response.data
