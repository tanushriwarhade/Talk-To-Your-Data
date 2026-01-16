from core.intent_parser import detect_intent, handle_ambiguity
from core.planner import build_plan
from core.sql_generator import generate_sql
from core.validator import validate_sql
from core.executor import execute_sql


def run_query(question: str):
    print("\n🧠 Question:", question)

    intent = detect_intent(question)
    print("🔍 Detected intent:", intent.value)

    if intent.value == "ambiguous":
        print("\n⚠️ Ambiguity detected:")
        print(handle_ambiguity(question))
        return

    plan = build_plan(question, intent)
    print("\n📋 Reasoning plan:")
    for k, v in plan.items():
        print(f"  {k}: {v}")

    sql = generate_sql(plan)
    print("\n🧾 Generated SQL:")
    print(sql)

    if not validate_sql(sql):
        print("\n❌ SQL validation failed. Query blocked for safety.")
        return

    cols, rows = execute_sql(sql)

    print("\n📊 Result:")
    if not rows:
        print("No rows returned. (This is a valid result.)")
        return

    print(cols)
    for r in rows[:10]:
        print(r)


if __name__ == "__main__":
    print("🔹 Natural Language → SQL Reasoning System 🔹")
    print("Type a question or 'exit'\n")

    while True:
        q = input(">> ")
        if q.lower() in ["exit", "quit"]:
            break
        run_query(q)
