from flask import Flask  # importing Flask

app = Flask(__name__)  # initializing Flask


# if file is executed, __name__ = "__main__"
# if file is imported, __name__ = "<imported_file_name>"


@app.route('/')  # it's actually localhost:5000
def home():
    return "Home content goes here"


@app.route('/about/')
def about():
    return "About"


if __name__ == "__main__":
    app.run(debug=True)
