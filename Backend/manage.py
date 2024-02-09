from app import create_app
from flask import Flask, request

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    

@app.route("/predict" , methods=["GET", "POST"])
# @app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST": 
            message = {
                "name" : "post"
            }
            return message
    if request.method == "GET":
            message = {
                "name" : "get"
            }
            return message