from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello():
    return "<b>First flask app </b>" #http response

# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def lol():
#     return {"message":"Hello world"} #json response