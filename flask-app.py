from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def home():
    return """
    <html>
    <head><title>This is my flask app</title></head>
    <body><h1> Hello from Flask </h1></body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
