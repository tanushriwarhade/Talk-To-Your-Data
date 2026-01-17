# Natural Language → SQL Reasoning System

Ask questions in plain English and get:
- Explicit reasoning
- Safe SQL queries
- Correct database results

This project does not translate text to SQL directly.  
Instead, it reasons step-by-step like a human data analyst.

---

## Why This Project?

Naïve text-to-SQL systems often fail because they:
- Hallucinate table or column names
- Guess when queries are ambiguous (for example, “recent” or “best”)
- Generate unsafe or inefficient SQL
- Provide no explanation of how the query was formed

Our solution fixes this by reasoning first, then generating SQL.

---

## Core Idea

Reason → Plan → Generate SQL → Validate → Execute

The system explicitly:
1. Detects user intent  
2. Explores the database schema  
3. Builds a reasoning plan  
4. Generates safe, read-only SQL  
5. Validates the query  
6. Executes and explains the results  

---

## Architecture

Frontend (Web UI or CLI)  
→ Intent Detection  
→ Reasoning Planner  
→ SQL Generator  
→ Safety Validator  
→ SQLite Database (Read-only)

---

## Features

- Natural language questions
- Explicit reasoning plans
- Multi-step query handling (joins and aggregations)
- Ambiguity detection and clarification
- Schema introspection (meta queries)
- Safe SQL execution (read-only, no SELECT *)
- Web interface with CLI fallback

---

## Example Queries

Try these in the system:

- How many customers are from Brazil?
- Which customers have never made a purchase?
- What tables exist in this database?
- Show me recent orders
- Show me orders from the last 30 days

---

## Installation Steps

Follow the steps below to set up and run the project locally.

---



## Installation Steps

Follow the steps below to set up and run the project on your local machine.

### 1. Install Python
Ensure that Python version 3.10 or higher is installed on your system.

Check the installed Python version by running:
```bash
python --version
```
Clone the project repository from GitHub using the following command:
```
git clone https://github.com/tanushriwarhade/Talk-To-Your-Data.git
```

Navigate into the project directory:
```
cd Talk-To-Your-Data
```
Create a virtual environment:
```
python -m venv venv
```
On Windows:
```
venv\Scripts\activate
```

On macOS or Linux:
```
source venv/bin/activate
```
Install the required Python dependency using pip:
```
pip install flask
```
Verify the database setup by running:
```
python verify_db.py
```
Start the web application using:
```
python app.py
```

Once the server starts, open your browser and navigate to:
```
http://127.0.0.1:5000
```
If you prefer using the command line or need a fallback during a demo, run:
```
python main.py
```

Talk-To-Your-Data/
│
├── core/
│   ├── intent_parser.py      # Detects user intent and ambiguity
│   ├── planner.py            # Builds the reasoning plan
│   ├── sql_generator.py      # Generates safe SQL queries
│   ├── validator.py          # Enforces SQL safety rules
│   ├── executor.py           # Executes SQL on the database
│   └── db.py                 # Database connection handler
│
├── data/
│   └── chinook.db             # SQLite database
│
├── templates/
│   └── index.html             # Web interface (frontend)
│
├── static/                    # Static files (CSS/JS if extended)
│
├── app.py                     # Flask web application entry point
├── main.py                    # CLI interface
├── verify_db.py               # Database verification script
└── README.md                  # Project documentation
