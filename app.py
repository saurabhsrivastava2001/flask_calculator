from flask import Flask,request,render_template,jsonify
import json


app=Flask(__name__)


@app.route('/')
def welcome():
    return "welcome to the calculator homepage"
print(__name__)

@app.route('/cal', methods=["GET"])
def math():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]
    
    
    if operation== "add":
        result=number1+number2
    elif operation=="multiply":
        result=number1*number2
    elif operation=="subs":
        result=number1-number2
    else:
        result=number1/number2
    return jsonify(result)

if __name__=='__main__':
    app.run(debug=True)