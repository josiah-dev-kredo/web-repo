from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") # root path
def home():
    return render_template('content_1.html',user_name="Josiah!",my_list=["banana","pineapple","peach","cheese"])

if __name__ == "__main__":
    app.run(debug=True)