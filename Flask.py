from flask import Flask, jsonify,request
app=Flask(__name__)
arr=[
    {
        'name':'anish',
        'height':'10'
    },
    {
        'name':'Ranju',
        'height':'1'
    }
]
# @app.route("/user")
# def home():
#     return "Hi"

# @app.route("/name/<username>")
# def names(username):
#     arr.append(username)
#     return "user added successfully" +username
@app.route("/users",methods=["GET"])
def get_users():
    return jsonify(arr)

@app.route("/users",methods=["POST"])
def create_user():
    new_user=request.get_json()
    arr.append(new_user)
    return jsonify(arr)

@app.route("/users/<name>",methods=["PUT"])
def Update_user(name):
    data=request.get_json()
    for record in arr:
        if record["name"]==name:
            record["heights"]=data["heights"]
        print(arr)
        return ("record udpated successfully")


# @app.route("/name")
# def name():
#     return "This is Anish"
if __name__=="__main__":
    app.run(debug=True)