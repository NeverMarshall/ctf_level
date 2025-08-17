from flask import Flask, request, redirect, render_template_string, session
import sqlite3

app = Flask(__name__)
app.secret_key = "supersecret"

def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    c.execute("DELETE FROM users")
    c.execute("INSERT INTO users VALUES ('admin', 'supersecure')")
    conn.commit()
    conn.close()

init_db()

login_page = """
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
  <h2>Login</h2>
  <form method="POST">
    Username: <input type="text" name="username"><br>
    Password: <input type="password" name="password"><br>
    <input type="submit" value="Login">
  </form>
  {% if error %}<p style="color:red">{{ error }}</p>{% endif %}
</body>
</html>
"""

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        user = request.form["username"]
        pw = request.form["password"]

        conn = sqlite3.connect("users.db")
        c = conn.cursor()

        query = f"SELECT * FROM users WHERE username='{user}' AND password='{pw}'"
        c.execute(query)
        result = c.fetchone()
        conn.close()

        if result:
            return "flag{blind_sql_injection_master}"
        else:
            error = "Invalid credentials"
    return render_template_string(login_page, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8006)
