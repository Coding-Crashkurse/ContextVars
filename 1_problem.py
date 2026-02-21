"""1) The Problem – user_id through every signature."""


def handle_message(text, user_id):
    return validate_input(text, user_id)


def validate_input(text, user_id):
    if not text.strip():
        return f"[{user_id}] empty message"
    return generate_response(text, user_id)


def generate_response(text, user_id):
    return f"[{user_id}] reply to '{text}'"


print(handle_message("hello", "user-42"))
