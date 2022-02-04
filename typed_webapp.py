from textwrap import dedent
from typing import Literal, TypedDict, cast

from flask import Flask

UserDetails = TypedDict(
    "UserDetails",
    {
        "age": int,
        "gender": Literal["male", "female"],
    },
)
User = TypedDict(
    "User",
    {
        "userid": int,
        "username": str,
        "details": UserDetails,
    },
)

ErrorMsg = TypedDict("ErrorMsg", {"error": str})

app = Flask(__name__)

LOGGED_IN = False


@app.get("/")
def hello() -> str:
    return "Hello, flask!"


def get_user_from_db() -> User:
    # Assume we did a database call here
    return {
        "username": "tusharsadhwani",
        "userid": 123456,
        "details": {
            "age": 21,
            "gender": "male",
        },
    }


def get_user() -> User | ErrorMsg:
    if not LOGGED_IN:
        return {"error": "not_logged_in"}

    user = get_user_from_db()
    return user


@app.get("/api")
def api() -> User | ErrorMsg:
    return get_user()


@app.get("/login/<password>")
def login(password: str) -> str:
    if password != "123456":
        return "Wrong password"

    global LOGGED_IN
    LOGGED_IN = True

    return "Logged in successfully!"


@app.get("/logout")
def logout() -> str:
    global LOGGED_IN
    LOGGED_IN = False

    return "Logged out successfully!"


@app.get("/user")
def user() -> str:
    user = get_user()
    if "error" in user:
        return "Please log in"

    # Workaround: https://github.com/python/mypy/issues/9953
    user = cast(User, user)

    return dedent(
        f"""\
        Username: {user['username']}
        <br>
        User details:
        <ol>
        <li> Age: {user['details']['age']} </li>
        <li> Gender: {user['details']['gender']} </li>
        """
    )


if __name__ == "__main__":
    app.run(port=8000)
