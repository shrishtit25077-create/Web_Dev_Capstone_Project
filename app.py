import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client

# Load env
from dotenv import load_dotenv
load_dotenv()

# Flask app
app = Flask(__name__)
CORS(app)

# Supabase setup
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Default file (optional)
DEFAULT_FILE_URL = None


# ---------------- ROUTES ---------------- #

@app.route("/")
def home():
    return {"status": "Assignment API running..."}


# ================= ADMIN =================
# Get all assignments (from creation table)

@app.route("/admin/assignments", methods=["GET"])
def get_created_assignments():
    res = supabase.table("creation").select("*").execute()
    return {"assignments": res.data}


# Add new assignment (admin)

@app.route("/admin/assignments", methods=["POST"])
def add_assignment():
    data = request.get_json()

    if not data or not data.get("title"):
        return {"error": "title required"}, 400

    new_assignment = {
        "title": data["title"],
        "description": data.get("description"),
    }

    res = supabase.table("creation").insert(new_assignment).execute()
    return res.data


# ================= STUDENT =================
# Get assignments to show on assignment page

@app.route("/assignments", methods=["GET"])
def get_assignments():
    res = supabase.table("creation").select("*").execute()
    return {"assignments": res.data}


# Submit assignment (student)

@app.route("/submit", methods=["POST"])
def submit_assignment():
    data = request.get_json()

    if not data.get("title"):
        return {"error": "title required"}, 400

    new_submission = {
        "title": data["title"],
        "description": data.get("description"),
        "file_url": data.get("file_url"),
    }

    res = supabase.table("assignments").insert(new_submission).execute()
    return res.data, 201

# ---------------- RUN ---------------- #
if __name__ == "__main__":
    app.run(port=5001, debug=True)