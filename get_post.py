import pandas as pd
from flask import Flask,request,jsonify
import numpy as np 
import json
app = Flask(__name__)

@app.route('/get',methods=['GET'])
def data_frame():
	data=pd.read_csv('data_frame_for_flask.csv')
	ls=list(data.to_dict('index').values())
	return jsonify(ls)

@app.route('/add',methods=['POST'])
def post_func():

	data1=request.get_json()
	df = pd.read_csv('data_frame_for_flask.csv')
	new_dict=df.to_dict("index")
	list_of_df=list(new_dict.values())
	created ={}
	created['index']=(list_of_df[-1]['index']+1)
	combine_data={**created,**data1}
	df=df.append(combine_data,ignore_index=True)
	print (df)
	df.to_csv('data_frame_for_flask.csv',index= None,header=True)
	return jsonify({"index": created["index"]})
@app.route("/delete",methods=['DELETE'])
def del_data():
	data1 = request.get_json()
	df = pd.read_csv(r"data_frame_for_flask.csv")
	# new_dict=df.to_dict("index")
	# list_of_df=list(new_dict.values())
	df = df[df['index'] != data1['index']]
	df.to_csv(r'data_frame_for_flask.csv',index = None, header=True)
	return jsonify({"index ":data1["index"]})

@app.route("/update", methods=["PUT"])
def update_data():
	data1 = request.get_json()
	df = pd.read_csv(r"dataframe_post.csv")
	df.loc[df['index'] == data1['index'],["nalme","roll_num","class"]] = data["name"],data["roll_num"],data["class"]
	df.to_csv(r'dataframe_post.csv',index = None, header=True)
	return jsonify({"index ":data1["index"]})
if __name__== '__main__':
	app.run(debug=True)