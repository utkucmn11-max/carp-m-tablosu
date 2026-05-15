from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

score = 0
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Çarpım Tablosu Oyunu</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            background-color: #f0f8ff;
            padding-top: 50px;
        }

        .box {
            background: white;
            width: 400px;
            margin: auto;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 0 10px gray;
        }

        input {
            padding: 10px;
            font-size: 20px;
            width: 100px;
        }

        button {
            padding: 10px 20px;
            font-size: 18px;
            background: green;
            color: white;
            border: none;
            border-radius: 10px;
        }

        h1 {
            color: darkblue;
        }
    </style>
</head>
<body>

<div class="box">
    <h1>Çarpım Tablosu Öğreniyorum 🎯</h1>

    <h2>{{ num1 }} × {{ num2 }} = ?</h2>

    <form method="POST">
        <input type="number" name="answer" required>
        <br><br>
        <button type="submit">Kontrol Et</button>
    </form>

    <h3>{{ message }}</h3>
    <h3>Puan: {{ score }}</h3>
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    global num1, num2, score

    message = ""

    if request.method == "POST":
        user_answer = int(request.form["answer"])

        if user_answer == num1 * num2:
            message = "✅ Doğru!"
            score += 1
        else:
            message = f"❌ Yanlış! Doğru cevap: {num1 * num2}"

        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

    return render_template_string(
        HTML,
        num1=num1,
        num2=num2,
        message=message,
        score=score
    )

if __name__ == "__main__":
    app.run(debug=True)
