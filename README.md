# 🧠 Natural Language → SQL Reasoning System

Ask questions in plain English and get:
-  Explicit reasoning
-  Safe SQL queries
-  Correct database results

This project **does not translate text to SQL directly**.  
Instead, it **reasons step-by-step** like a human data analyst.

---

## 🚀 Why This Project?

Naïve text-to-SQL systems often fail because they:
- Hallucinate table or column names
- Guess when queries are ambiguous (e.g., “recent”, “best”)
- Generate unsafe or inefficient SQL
- Provide no explanation of how the query was formed

 **Our solution fixes this by reasoning first, then generating SQL.**

---

## 🧠 Core Idea

> **Reason → Plan → Generate SQL → Validate → Execute**

The system explicitly:
1. Detects user intent  
2. Explores database schema  
3. Builds a reasoning plan  
4. Generates safe, read-only SQL  
5. Validates the query  
6. Executes and explains results  

---

## Architecture


---

## ✨ Features

-  Natural language questions
-  Explicit reasoning plans
-  Multi-step query handling (joins, aggregations)
-  Ambiguity detection & clarification
-  Schema introspection (meta queries)
-  Safe SQL execution (read-only, no SELECT *)
-  Web UI + CLI fallback

---

## 🧪 Example Queries

Try these in the system:

- `How many customers are from Brazil?`
- `Which customers have never made a purchase?`
- `What tables exist in this database?`
- `Show me recent orders`
- `Show me orders from the last 30 days`

---

##  Running the Project

### 📁 Step 1: Go to project directory
```bash
cd nl_sql_reasoner


##Tree
Folder PATH listing for volume OS
Volume serial number is AADA-BDED
C:.
├───core
│   └───__pycache__
├───data
├───llm
├───static
└───templates
