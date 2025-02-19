from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
from pathlib import Path

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for security in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load full preprocessed graph data from file (or database in production)
DATA_FILE = Path("graph_data.json")
if DATA_FILE.exists():
    with open(DATA_FILE, "r") as f:
        graph_data = json.load(f)
else:
    graph_data = {"nodes": [], "edges": []}  # Empty fallback if data file is missing

@app.get("/graph")
def get_graph():
    return graph_data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
