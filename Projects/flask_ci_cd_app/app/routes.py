from app import app

@app.route("/")
def home():
    return "Welcome to CI/CD Flask App!"

@app.route("/about")
def about():
    return "This is the About page."

@app.route("/health")
def health():
    return "OK", 200
