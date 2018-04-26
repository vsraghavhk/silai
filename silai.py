import os
from flask import Flask, request, redirect, url_for, jsonify
from werkzeug import secure_filename
from datetime import datetime
import fixed 

UPLOAD_FOLDER = '/home/silai/silai/images/'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(datetime.now().strftime("%s%f") + '.jpg')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            prediction = fixed.get_prediction(filename)
            
            with open("signnames.csv", "r") as f:
                signnames = f.read()
            id_to_name = { int(line.split(",")[0]):line.split(",")[1] for line in signnames.split("\n")[1:] if len(line) > 0}
            if prediction in id_to_name:
            #   string = id_to_name[prediction[0]]
                path = 'home/silai/silai/Database'
                idol = "{}.txt".format(prediction)
                idol = os.path.join(path, idol)
                f = open(idol, 'r')
                file_contents = f.read()
                f.close()
            return jsonify(prediction=file_contents) # jsonify(prediction=prediction)
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    """
    #<p>%s</p>
    #""" % "<br>".join(os.listdir(app.config['UPLOAD_FOLDER'],))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

