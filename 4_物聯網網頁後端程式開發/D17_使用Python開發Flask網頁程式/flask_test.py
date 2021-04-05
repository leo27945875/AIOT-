from flask import Flask, request, redirect, url_for, send_file


app = Flask(__name__)


@app.route("/")
def Index():
    return "Hello ~"


@app.route("/getName", methods=["GET"])
def GetName():
    name = request.args.get("name")
    return f"Hello {name} ~"


@app.route("/postName", methods=["POST"])
def GetPostName():
    name = request.form.get('name')
    return f"Hello {name} ~"


@app.route("/uploadPicture", methods=["POST"])
def UploadPicture():
    pic = request.files.get("picture")
    pic.save(pic.filename)
    return redirect(url_for("SendPicture", pictureName=pic.filename))


@app.route("/sendPicture/<pictureName>")
def SendPicture(pictureName):
    return send_file(pictureName)


if __name__ == "__main__":
    app.run(port=5002)
