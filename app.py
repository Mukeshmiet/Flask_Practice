from flask import Flask, request
import uuid

app = Flask(__name__)

db= [
  {
    "categories": ["dev"],
    "created_at": "2020-01-05 13:42:19.324003",
    "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
    "id": "elgv2wkvt8ioag6xywykbq",
    "updated_at": "2020-01-05 13:42:19.324003",
    "url": "https://api.chucknorris.io/jokes/elgv2wkvt8ioag6xywykbq",
    "value": "Chuck Norris's keyboard doesn't have a Ctrl key because nothing controls Chuck Norris."
  },
  {
    "categories": ["dev"],
    "created_at": "2020-01-05 13:42:19.324003",
    "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
    "id": "ae-78cogr-cb6x9hluwqtw",
    "updated_at": "2020-01-05 13:42:19.324003",
    "url": "https://api.chucknorris.io/jokes/ae-78cogr-cb6x9hluwqtw",
    "value": "There is no Esc key on Chuck Norris' keyboard, because no one escapes Chuck Norris."
  }
]

user_jock = {"jock": "", "url": "", "id": ""}

@app.get("/jock1")
def get_jock1():
    return {"jock_1": db[0]["value"], "url": db[0]["url"]}, 200

@app.get("/jock2")
def get_jock2():
    return {"jock_2": db[1]["value"], "url": db[1]["url"]}, 200

@app.post("/postjock")
def post_jock():
    data = request.get_json()
    new_jock = {"jock": data["jock"],"url": data["url"],"id": str(uuid.uuid4().hex)}
    db.append(new_jock)
    return {"message": "jock_created"}, 201

@app.post("/jock_url/<string:url>")
def post_url(url):
    user_jock["url"] = request.get_json()["url"]
    db.append(user_jock)
    return {"message": "jock added see all jocks here http://127.0.0.1:5000/jocks"}, 201

@app.post("/jock/<string:jock>")
def post_jock_only(jock):
    user_jock["jock"] = request.get_json()["jock"]
    user_jock["id"]= str(uuid.uuid4().hex)
    return {"message": "jock_url requires http://127.0.0.1:5000/jock_url/<string:url>"}, 201


@app.get("/jocks")
def get_jocks():
    return {"jocks": db}, 200

@app.get("/")
def get_alljocks():
    return {"jocks": db}, 200
