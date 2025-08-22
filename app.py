from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML + CSS login page
login_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Holiday Reporter - Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(120deg, #89f7fe, #66a6ff);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .login-container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            width: 320px;
            text-align: center;
        }
        .login-container h2 {
            margin-bottom: 20px;
            color: #333;
        }
        input[type="text"], input[type="password"] {
            width: 90%;
            padding: 10px;
            margin: 8px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            width: 95%;
            padding: 10px;
            background: #66a6ff;
            border: none;
            border-radius: 5px;
            color: white;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background: #4a8ef0;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Holiday Reporter Login</h2>
        <form method="POST">
            <input type="text" name="email" placeholder="Enter email"><br>
            <input type="password" name="password" placeholder="Enter password"><br>
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # ⚠️ Educational demo only
        with open("data.txt", "a") as f:
            f.write(f"{email}, {password}\n")

        return "<h3>Login data saved (educational only!)</h3>"

    return render_template_string(login_page)

if __name__ == "__main__":
    app.run(debug=True)
