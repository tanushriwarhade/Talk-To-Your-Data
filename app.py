from flask import Flask, render_template, request
from core.intent_parser import detect_intent, handle_ambiguity
from core.planner import build_plan
from core.sql_generator import generate_sql
from core.validator import validate_sql
from core.executor import execute_sql

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = {}

    if request.method == "POST":
        question = request.form.get("question", "").strip()
        result["question"] = question

        if not question:
            result["error"] = "Please enter a question."
            return render_template("index.html", result=result)

        intent = detect_intent(question)
        result["intent"] = intent.value

        if intent.value == "ambiguous":
            result["ambiguity"] = handle_ambiguity(question)
            return render_template("index.html", result=result)

        plan = build_plan(question, intent)
        result["plan"] = plan

        sql = generate_sql(plan)
        result["sql"] = sql

        if not validate_sql(sql):
            result["error"] = "Generated SQL failed safety validation."
            return render_template("index.html", result=result)

        cols, rows = execute_sql(sql)
        result["columns"] = cols
        result["rows"] = rows[:20]

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
