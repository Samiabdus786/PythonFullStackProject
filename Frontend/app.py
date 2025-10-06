import streamlit as st
import requests
from datetime import datetime, timedelta

# ------------------------------
# 1. SESSION STATE (Login)
# ------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

def login_page():
    st.title("🔐 Login to PyFoodGuardian")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Example users; you can add more
        USERS = {"admin": "1234", "user1": "abcd", "user2": "5678"}
        if username in USERS and password == USERS[username]:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Login Successful! Welcome {username}")
            st.rerun()
        else:
            st.error("Invalid credentials. Try again.")

# ------------------------------
# 2. CONFIG & ITEM IMAGES
# ------------------------------
BASE_URL = "https://pythonfullstackproject.onrender.com"

st.set_page_config(page_title="PyFoodGuardian", layout="wide")

ITEM_IMAGES = {
    "Milk": "https://wallpapers.com/images/hd/milk-background-nn4uqvyma4v02ltr.jpg",
    "paneer": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDQOQx9rWEWmfWDdfW25amMIRmVXwqTcxLJw&s",
    "Eggs": "https://static.vecteezy.com/system/resources/previews/030/666/664/large_2x/eggs-with-white-background-high-quality-ultra-hd-free-photo.jpg",
    "Butter": "https://images.unsplash.com/photo-1615484474828-1c3f81473c14",
    "Cheese": "https://images.unsplash.com/photo-1617196034413-447cf69c7aef",
    "Bread": "https://images.unsplash.com/photo-1608198093007-1d46ce1a7ff0",
    "Rice": "https://images.unsplash.com/photo-1574333757994-66e2431cfb7b",
    "Wheat Flour": "https://images.unsplash.com/photo-1628870901905-d70f0c6fffcf",
    "Sugar": "https://images.unsplash.com/photo-1587316745621-3757a4d3c1a2",
    "Salt": "https://images.unsplash.com/photo-1564518098551-c7a08c43f8e0",
    "Tea": "https://images.unsplash.com/photo-1571689937454-c75f278b3c04",
    "Coffee": "https://images.unsplash.com/photo-1541167760496-1628856ab772",
    "Tomato": "https://images.unsplash.com/photo-1617196033863-df7b3a13d67f",
    "Onion": "https://images.unsplash.com/photo-1617196034410-2c7c5a1e7d87",
    "Potato": "https://images.unsplash.com/photo-1617196033845-8d2b1c0dbf9c",
    "Carrot": "https://images.unsplash.com/photo-1582515073490-399813b8c24d",
    "Apple": "https://images.unsplash.com/photo-1567306226416-28f0efdc88ce",
    "Banana": "https://images.unsplash.com/photo-1574226516831-e1dff420e42e",
    "Orange": "https://images.unsplash.com/photo-1570197786301-5f50d5f0c72a",
    "Yogurt": "https://images.unsplash.com/photo-1601004890684-d8cbf643f5f2",
}

# ------------------------------
# 3. HELPER FUNCTIONS
# ------------------------------
def fetch_items():
    try:
        response = requests.get(f"{BASE_URL}/items")
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, dict) and data.get("Success"):
                return data.get("Data", [])
            elif isinstance(data, list):
                return data
            else:
                return []
        else:
            st.error("Error fetching items!")
            return []
    except Exception as e:
        st.error(f"Error: {e}")
        return []

def add_item(item_name, category, quantity, purchase_date, expiry_date):
    payload = {
        "item_name": item_name,
        "category": category,
        "quantity": quantity,
        "purchase_date": purchase_date,
        "expiry_date": expiry_date
    }
    try:
        response = requests.post(f"{BASE_URL}/items", json=payload)
        if response.status_code == 200:
            st.success("Item added successfully!")
        else:
            st.error(response.json().get("detail", "Failed to add item"))
    except Exception as e:
        st.error(f"Error: {e}")

def update_item(item_id, updates):
    payload = {"updates": updates}
    try:
        response = requests.put(f"{BASE_URL}/items/{item_id}", json=payload)
        if response.status_code == 200:
            st.success("Item updated successfully!")
        else:
            st.error(response.json().get("detail", "Failed to update item"))
    except Exception as e:
        st.error(f"Error: {e}")

def delete_item(item_id):
    try:
        response = requests.delete(f"{BASE_URL}/items/{item_id}")
        if response.status_code == 200:
            st.success("Item deleted successfully!")
        else:
            st.error(response.json().get("detail", "Failed to delete item"))
    except Exception as e:
        st.error(f"Error: {e}")

def get_expiry_status(expiry_date):
    today = datetime.today().date()
    try:
        expiry = datetime.strptime(expiry_date, "%Y-%m-%d").date()
        if expiry < today:
            return "Expired", "❌", "red"
        elif expiry <= today + timedelta(days=3):
            return "Expiring Soon", "⚠️", "yellow"
        else:
            return "Fresh", "✅", "green"
    except:
        return "Unknown", "❓", "gray"

# ------------------------------
# 4. MAIN APP
# ------------------------------
def main_app():
    st.title(f"🍽️ PyFoodGuardian - Smart Pantry ({st.session_state.username})")

    st.sidebar.title("Actions")
    action = st.sidebar.radio("Select Action:", ["View Items", "Add Item", "Update Item", "Delete Item", "Logout"])

    if action == "View Items":
        st.subheader("📋 Pantry Items")
        items = fetch_items()
        if items:
            for i, item in enumerate(items):
                status_text, status_icon, color = get_expiry_status(item['expiry_date'])
                cols = st.columns([1, 1, 3, 2, 2, 2, 2])
                img_url = ITEM_IMAGES.get(item['item_name'], "https://via.placeholder.com/80")
                cols[0].image(img_url, width=80)
                cols[1].markdown(f"**ID:** {item['item_id']}")
                cols[2].markdown(f"**{item['item_name']}**\nCategory: {item.get('category','N/A')}")
                cols[3].markdown(f"Quantity: {item['quantity']}")
                cols[4].markdown(f"Purchase: {item['purchase_date']}")
                cols[5].markdown(f"Expiry: {item['expiry_date']}")
                cols[6].markdown(f"{status_icon} {status_text}")
                st.markdown("---")
        else:
            st.info("No items found!")

    elif action == "Add Item":
        st.subheader("➕ Add New Item")
        item_name = st.text_input("Item Name")
        category = st.text_input("Category")
        quantity = st.number_input("Quantity", min_value=1, step=1)
        purchase_date = st.date_input("Purchase Date")
        expiry_date = st.date_input("Expiry Date")
        if st.button("Add Item"):
            add_item(item_name, category, quantity, str(purchase_date), str(expiry_date))

    elif action == "Update Item":
        st.subheader("✏️ Update Item")
        item_id = st.number_input("Item ID to Update", min_value=1, step=1)
        field = st.text_input("Field to Update (item_name, category, quantity, purchase_date, expiry_date)")
        value = st.text_input("New Value")
        if st.button("Update Item"):
            if field and value:
                updates = {field: value}
                update_item(item_id, updates)
            else:
                st.error("Field and Value are required!")

    elif action == "Delete Item":
        st.subheader("🗑️ Delete Item")
        item_id = st.number_input("Item ID to Delete", min_value=1, step=1)
        if st.button("Delete Item"):
            delete_item(item_id)

    elif action == "Logout":
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.success("Logged out successfully!")
        st.rerun()

# ------------------------------
# 5. APP FLOW
# ------------------------------
if not st.session_state.logged_in:
    login_page()
else:
    main_app()
