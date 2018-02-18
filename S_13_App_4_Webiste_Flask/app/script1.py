from flask import Flask, render_template

app = Flask(__name__)  # initializing Flask


# if file is executed, __name__ = "__main__"
# if file is imported, __name__ = "<imported_file_name>"


@app.route('/')  # it's actually localhost:5000
def home():
    # return "Home content goes here"
    return render_template("home.html")


@app.route('/about/')
def about():
    # return "About"
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
