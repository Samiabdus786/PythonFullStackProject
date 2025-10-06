from src.db import DatabaseManager

class ItemManager:
    """
    Acts as a bridge between frontend (Streamlit / FastAPI) and the database.
    Handles all business logic before calling database operations for items.
    """

    def __init__(self):
        # Create a database manager instance
        self.db = DatabaseManager()

    # --- CREATE ---
    def add_item(self, item_name, category, quantity, purchase_date, expiry_date):
        """
        Add a new item to the database.
        Return the success message if the item is added.
        """
        if not item_name or not quantity:
            return {"Success": False, "Message": "Item Name and Quantity are required"}

        result = self.db.create_item(item_name, category, quantity, purchase_date, expiry_date)

        if result.get("Success", True):
            return {"Success": True, "Message": "Item added successfully!"}
        else:
            return {"Success": False, "Message": f"Error: {result.get('Message', 'Unknown error')}"}

    # --- READ ---
    def get_items(self):
        """
        Get all the items from the database.
        """
        return self.db.get_all_items()

    def get_item(self, item_id):
        """
        Get a single item by ID.
        """
        if not item_id:
            return {"Success": False, "Message": "Item ID is required"}

        result = self.db.get_item_by_id(item_id)
        if result:
            return {"Success": True, "Data": result}
        else:
            return {"Success": False, "Message": "Item not found"}

    # --- UPDATE ---
    def update_item(self, item_id, updates: dict):
        """
        Update fields of an item by ID.
        """
        if not item_id or not updates:
            return {"Success": False, "Message": "Item ID and updates are required"}

        result = self.db.update_item(item_id, updates)
        if result.get("Success", True):
            return {"Success": True, "Message": "Item updated successfully!"}
        else:
            return {"Success": False, "Message": f"Error: {result.get('Message', 'Unknown error')}"}

    # --- DELETE ---
    def delete_item(self, item_id):
        """
        Delete the item from the database.
        """
        result = self.db.delete_item(item_id)
        if result.get("Success", True):
            return {"Success": True, "Message": "Item deleted successfully"}
        else:
            return {"Success": False, "Message": f"Error: {result.get('Message', 'Unknown error')}"}
