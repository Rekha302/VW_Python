
from functools import wraps
from flask import session, redirect


def role_required(roles):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            if "role" not in session:
                return redirect("/login")

            if session["role"] not in roles:
                return "Access Denied"

            return func(*args, **kwargs)

        return wrapper

    return decorator