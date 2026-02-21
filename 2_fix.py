"""2) The Fix – set user_id once, read anywhere."""
from contextvars import ContextVar

user_id: ContextVar[str] = ContextVar("user_id")


def handle_message(text):
    return validate_input(text)


def validate_input(text):
    if not text.strip():
        return f"[{user_id.get()}] empty message"
    return generate_response(text)


def generate_response(text):
    return f"[{user_id.get()}] reply to '{text}'"


user_id.set("user-42")
print(handle_message("hello"))
