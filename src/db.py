import os
from supabase import create_client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

class DatabaseManager:
    """
    Handles all database operations with Supabase.
    """

    # CREATE
    def create_item(self, item_name, category, quantity, purchase_date, expiry_date):
        try:
            response = supabase.table("items").insert({
                "item_name": item_name,
                "category": category,
                "quantity": quantity,
                "purchase_date": purchase_date,
                "expiry_date": expiry_date
            }).execute()
            return {"Success": True, "Data": response.data}
        except Exception as e:
            return {"Success": False, "Message": str(e)}

    # READ ALL
    def get_all_items(self):
        try:
            response = supabase.table("items").select("*").order("created_at", desc=True).execute()
            return response.data
        except Exception as e:
            return {"Success": False, "Message": str(e)}

    # READ ONE
    def get_item_by_id(self, item_id: int):
        try:
            response = supabase.table("items").select("*").eq("item_id", item_id).execute()
            return response.data
        except Exception as e:
            return {"Success": False, "Message": str(e)}

    # UPDATE
    def update_item(self, item_id: int, updates: dict):
        try:
            response = supabase.table("items").update(updates).eq("item_id", item_id).execute()
            return {"Success": True, "Data": response.data}
        except Exception as e:
            return {"Success": False, "Message": str(e)}

    # DELETE
    def delete_item(self, item_id: int):
        try:
            response = supabase.table("items").delete().eq("item_id", item_id).execute()
            return {"Success": True, "Data": response.data}
        except Exception as e:
            return {"Success": False, "Message": str(e)}
