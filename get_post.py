import pandas as pd
from flask import Flask,request,jsonify
import numpy as np 
import json
app = Flask(__name__)
@app.route('/data_frame',methods=['POST','GET'])

def data_frame():
	data=pd.read_csv('data_frame_for_flask.csv')
	ls=list(data.to_dict().values())
	return jsonify(ls)

if __name__== '__main__':
	app.run(debug=True)