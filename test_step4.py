from core.intent_parser import detect_intent
from core.planner import build_plan
from core.sql_generator import generate_sql
from core.validator import validate_sql
from core.executor import execute_sql

question = "Which customers have never made a purchase?"

intent = detect_intent(question)
plan = build_plan(question, intent)

print("PLAN:", plan)

sql = generate_sql(plan)
print("\nGenerated SQL:\n", sql)

if not validate_sql(sql):
    print("\nSQL validation failed!")
else:
    cols, rows = execute_sql(sql)
    print("\nResult:")
    print(cols)
    for r in rows[:5]:
        print(r)
