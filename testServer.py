from flask import Flask,request,jsonify
import numpy as np 
import pickle

app= Flask(__name__)

@app.route('/',methods=['POST','GET'])
def testVals():
    serverValues= request.get_data()
    ##print (serverValues)
    ##serverValues2= dict(serverValues)
    ##video = serverValues2['video']
    print(serverValues)
    with open('/home/animesh/Desktop/videoPick3','wb') as f:
        pickle.dump(serverValues,f)
    return 'success'

app.run(host='0.0.0.0',port=8080,debug=True)