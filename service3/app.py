from flask import Flask, request, Response
import requests 
import random

app = Flask(__name__)

@app.route('/get_float/', methods=["GET"])
def get_float():
    randomfloat=str(random.uniform(0,10))
    return Response(randomfloat[0:4], mimetype='text/plain')

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)
