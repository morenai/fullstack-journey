# Fullstack Journey

Learning Full Stack Development — Python, FastAPI, Vue.js 3, GCP, CI/CD

## Stack
- Backend: Python 3.14 + FastAPI
- Database: SQLite (SQLAlchemy)
- Frontend: Vue.js 3 (coming Week 3)
- Cloud: GCP Cloud Run (coming Week 6)
- CI/CD: GitHub Actions (coming Week 7)

## Project Structure
fullstack-journey/
├── src/
│ ├── main.py → FastAPI app + endpoints
│ ├── database.py → SQLAlchemy models + DB connection
│ ├── day01.py → Python basics
│ ├── day02.py → Loops and error handling
│ ├── day03.py → Classes and OOP
│ └── day04.py → Files and JSON
├── data/
│ ├── guest.json
│ └── guests.json
├── .env → Environment variables (not in Git)
├── .gitignore
├── COMMANDS.md → Terminal commands reference
└── requirements.txt


## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Health check |
| GET | /guests | Get all guests |
| GET | /guests/{id} | Get guest by ID |
| POST | /guests | Create a guest |
| DELETE | /guests/{id} | Delete a guest |

## How to Run
```bash
cd src
source ../venv/bin/activate
uvicorn main:app --reload
```

API docs available at: http://127.0.0.1:8000/docs

## Progress
### Week 1 — Python Foundations ✅
- Day 01: Variables, functions
- Day 02: Loops, conditions, error handling
- Day 03: Classes and OOP
- Day 04: Files and JSON
- Day 05: Project structure

### Week 2 — FastAPI ✅
- Day 06: First endpoints
- Day 07: POST requests and Pydantic validation
- Day 08: SQLAlchemy database
- Day 09: GET by ID, DELETE, 404 errors
- Day 10: Swagger docs (in progress)