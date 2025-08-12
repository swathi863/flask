from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask!"
app.add_url_rule('/home','home',home)

if __name__ == "__main__":
    app.run(debug=True)
