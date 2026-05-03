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


# Get all assignments
@app.route("/assignments", methods=["GET"])
def get_assignments():
    res = supabase.table("assignments").select("*").execute()
    return {"assignments": res.data}


# Create new assignment
@app.route("/assignments", methods=["POST"])
def create_assignment():

    data = request.get_json()

    if not data or not data.get("title"):
        return {"error": "title is required"}, 400

    if not data.get("description"):
        return {"error": "description is required"}, 400

    new_assignment = {
        "title": data["title"],
        "description": data["description"],
        "file_url": data.get("file_url", DEFAULT_FILE_URL),
    }

    res = supabase.table("assignments").insert(new_assignment).execute()

    return res.data, 201


# ---------------- RUN ---------------- #
if __name__ == "__main__":
    app.run(port=5001, debug=True)