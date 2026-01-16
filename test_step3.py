from core.intent_parser import detect_intent
from core.planner import build_plan

questions = [
    "Which customers have never made a purchase?",
    "How many customers are from Brazil?",
    "What tables exist in this database?"
]

for q in questions:
    intent = detect_intent(q)
    plan = build_plan(q, intent)

    print("\nQuestion:", q)
    print("Plan:")
    for k, v in plan.items():
        print(f"  {k}: {v}")
