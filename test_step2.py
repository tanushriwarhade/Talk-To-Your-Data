from core.intent_parser import detect_intent, handle_ambiguity

questions = [
    "How many customers are from Brazil?",
    "Show me recent orders",
    "Which customers have never made a purchase?",
    "What tables exist in this database?"
]

for q in questions:
    intent = detect_intent(q)
    print(f"\nQ: {q}")
    print("Detected Intent:", intent.value)

    if intent.value == "ambiguous":
        print("Ambiguity Message:")
        print(handle_ambiguity(q))
