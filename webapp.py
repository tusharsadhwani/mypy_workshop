from textwrap import dedent

from flask import Flask

app = Flask(__name__)

LOGGED_IN = False


@app.get("/")
def hello():
    return "Hello, flask!"


def get_user_from_db():
    # Assume we did a database call here
    return {
        "username": "tusharsadhwani",
        "userid": 123456,
        "details": {
            "age": 21,
            "gender": "male",
        },
    }


def get_user():
    if not LOGGED_IN:
        return {"error": "not_logged_in"}

    user = get_user_from_db()
    return user


@app.get("/api")
def api():
    return get_user()


@app.get("/login/<password>")
def login(password):
    if password != "123456":
        return "Wrong password"

    global LOGGED_IN
    LOGGED_IN = True

    return "Logged in successfully!"


@app.get("/logout")
def logout():
    global LOGGED_IN
    LOGGED_IN = False

    return "Logged out successfully!"


@app.get("/user")
def user():
    user = get_user()

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
