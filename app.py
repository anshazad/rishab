import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    name1=jsonObj['name1']
    name2=jsonObj['name2']
    response+="<b> Welcome " + name1 + " " + name2 + " to the IC100 course.</b><br>"
        
    	    
    return response
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
