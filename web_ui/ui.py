from flask import Flask, render_template
test_image_data = ""
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", image_list=test_image_data)

if __name__ == "__main__":
    app.run(debug=True)