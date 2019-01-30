from flask import Flask,request
import json
app = Flask(__name__)
@app.route('/home')

def hello():
	return "hello i m from ludhiana"

@app.route('/login',methods=['POST','GET'])
def login():
	data=request.get_json()
	name=data['id']
	print(name)
	return name

if __name__== '__main__':
	app.run(debug=True)