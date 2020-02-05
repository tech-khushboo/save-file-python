import flask
import werkzeug

app = flask.Flask(__name__)

@app.route('/upload', methods = ['GET', 'POST'])
def handle_request():
    images = flask.request.files.to_dict(flat=False)['image']
    for image in images:
        print(image)
        filename = werkzeug.utils.secure_filename(image.filename)
        print("\nReceived image File name : " + image.filename)
        image.save("./images/"+filename)
    return "Image Uploaded Successfully"

app.run(host="0.0.0.0", port=5000, debug=True)