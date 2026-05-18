from flask import Flask, request

app = Flask(__name__)

@app.route("/from-request/", methods=["GET", "POST", "PUT", "DELETE"])
def from_request():
    if (request.method == "GET"):
        return "GET"
    elif (request.method == "POST"):
        return "POST"
    else:
        return f"Other method [{request.method}]"

@app.get("/from-route/")
def from_route_get():
    return "GET from route decorator"

@app.post("/from-route/")
def from_route_post():
    return "POST from route decorator"

@app.put("/from-route/")
def from_route_put():
    return "PUT from route decorator"
