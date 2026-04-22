from agent.intent import detect_intent
from tools.lead_capture import mock_lead_capture
from rag.qa import get_rag_answer


def handle_input(state, user_input):
    state.messages.append(user_input)

    # 🔥 IMPORTANT: If already in lead flow → continue
    if state.stage != "start":
        return lead_flow(state, user_input)

    # Detect intent ONLY at start
    state.intent = detect_intent(user_input)

    # Greeting
    if state.intent == "greeting":
        return "Hey! 👋 How can I help you today?"

    # Inquiry
    if state.intent == "inquiry":
        return get_rag_answer(user_input)

    # High Intent → start lead flow
    if state.intent == "high_intent":
        state.stage = "collect_name"
        return "Great! Let's get you started 😊 What's your name?"

    return "I didn’t understand that."

def is_valid_email(text):
    return "@" in text and "." in text


def lead_flow(state, user_input):

    # STEP 1: NAME
    if state.stage == "collect_name":

        # ❌ Reject invalid name (email or sentence)
        if "@" in user_input or len(user_input.split()) > 3:
            return "Please enter your name (not email or sentence)."

        state.name = user_input
        state.stage = "collect_email"
        return "Nice to meet you! What's your email?"

    # STEP 2: EMAIL
    elif state.stage == "collect_email":

        if not is_valid_email(user_input):
            return "Please enter a valid email address."

        state.email = user_input
        state.stage = "collect_platform"
        return "Which platform do you create content on? (YouTube, Instagram, etc.)"

    # STEP 3: PLATFORM
    elif state.stage == "collect_platform":

        state.platform = user_input

        mock_lead_capture(state.name, state.email, state.platform)

        state.stage = "completed"

        return "🎉 You're all set! Our team will reach out shortly."

    return "Let's continue."