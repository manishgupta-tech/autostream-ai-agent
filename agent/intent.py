def detect_intent(user_input: str) -> str:
    text = user_input.lower()

    # Greeting
    if any(x in text for x in ["hi", "hello", "hey"]):
        return "greeting"

    # High intent (VERY IMPORTANT)
    if any(x in text for x in [
        "buy", "subscribe", "want", "start", "sign up", "get started"
    ]):
        return "high_intent"

    # Inquiry
    if any(x in text for x in ["price", "plan", "cost", "pricing"]):
        return "inquiry"

    return "inquiry"