# PyFoodGuardian – Smart Pantry & Food Expiry Tracker

## Overview
PyFoodGuardian is a **Python-based CLI application** that helps you **manage your pantry** and **track food expiry dates** efficiently. It uses **Supabase (PostgreSQL)** as a backend to store data, allowing you to **add, update, remove, and monitor items** while reducing food waste.

## Features
- Add pantry items with details: name, category, quantity, purchase date, expiry date.
- Update or remove items easily.
- Check for expired or near-expiry items.
- Export pantry inventory to CSV.
- CLI-based interface, fully Python-only.   

## Project Structure

PyFoodGuardian/
│    
│
├─ src/                    # Core application logic
│   |---logic.py            # Business logic and task operations (add/update/remove/check/export)
│   └─ db.py               # Database operations (Supabase connection, queries)
│
├─ api/                    # Backend API
│   └─ main.py             # FastAPI endpoints (optional for web API access)
│
├─ frontend/               # Frontend application
│   └─ app.py              # Streamlit or CLI interface for user interaction
│
|-requriements.txt         # Python Dependencies
├─ .env                   # Environment variables (Supabase URL & KEY)
└─ README.md               # Project documentation

## Quick Start

### Prerequisites

- Python 3.8 or higher
- A Supabase account
- Git(Push,cloning)

### 1. Clone or Download the Project

# Option 1: Clone with Git
git clone <repository-url>

# Option 2: Download and extract the ZIP file

### 2. Install Dependencies

# Install all required Python packages
pip install -r requirements.txt

### 3. Set Up Supabase Database

1.Create a Supabase Project:

2.Create the Task Table:
-Go to the sql Editor in your Supabase dashboard
-Run this



```sql
CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,      -- Unique ID for each item
    item_name TEXT NOT NULL,         -- Name of the item
    category TEXT,                   -- Food category (optional)
    quantity INTEGER DEFAULT 1,      -- Number of units
    purchase_date DATE,              -- Date the item was purchased
    expiry_date DATE,                -- Expiry date of the item
    created_at TIMESTAMP DEFAULT NOW() -- Timestamp when the item was added
);

```
3. **Get Your Credentials:

## 4.Configure Environment Variables

1. Create a `.env` file in the project root

2. Add your supabase credentials to `.env`:
SUPABASE_URL=your_project_url here
SUPABASE_KEY=your_anon_key_here

**Example:**
SUPABASE_URL="https://jkilnhgnzrhfdxjmpkqm.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpraWxuaGduenJoZmR4am1wa3FtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTg2ODY0MTYsImV4cCI6MjA3NDI2MjQxNn0.tCiQirkCQODasRDJZCcwxqiltY1j_VYkjgh-XcBBuZU"

### 5. Run the Application

## Streamlit Frontend
streamlit run frontend/app.py

The app will open in your browser at `http://localhost:8501`


## FastAPI Backend

cd api
python main.py

The API will be available at `http://localhost:8000`

## How to Use

## Technical Details 

## Technologies Used

- **Frontend**: Streamlit(Python web framework)
- **Backend**: FastAPI(Python REST API framework)
- **Database**: Supabase(postgreSQL-based backend-as-a-service)
- **Language**: Python 3.8+


## Key Components

1. **`src/db.py`**: Database operations 
    -Handles all CRUD operations with Supabase

2. **`src/logic.py`**: Business logic 
    -Task validation and processing

## Troubleshooting

## Common issues

## Future Enhancements

## support

If you encounter any issues or have questions:
phone no. : +91 8125811310
Email : samiabdus9831@gmail.com


