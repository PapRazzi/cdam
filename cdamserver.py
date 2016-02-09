import os
from flask import Flask, request, redirect, url_for,jsonify
from werkzeug import secure_filename
from cdam import Cdam

filename =''
UPLOAD_FOLDER = '/home/ubuntu/workspace/working_test_wav'
ALLOWED_EXTENSIONS = set(['wav'])

model = Cdam("wavs", {'dry_1.wav':'dry', 'dry_2.wav':'dry', 'dry_3.wav':'dry', 'dry_4.wav':'dry','dry_5.wav':'dry', 'dry_6.wav':'dry', 'dry_7.wav':'dry', 'dry_8.wav':'dry','dry_9.wav':'dry', 'dry_10.wav':'dry','dry_11.wav':'dry', 'dry_12.wav':'dry', 'dry_13.wav':'dry', 'dry_14.wav':'dry','dry_15.wav':'dry', 'dry_16.wav':'dry', 'dry_17.wav':'dry', 'dry_18.wav':'dry','dry_19.wav':'dry', 'dry_20.wav':'dry','dry_21.wav':'dry', 'dry_22.wav':'dry', 'dry_23.wav':'dry', 'dry_24.wav':'dry','dry_25.wav':'dry', 'dry_26.wav':'dry', 'dry_27.wav':'dry', 'dry_28.wav':'dry','dry_29.wav':'dry', 'dry_30.wav':'dry','dry_31.wav':'dry', 'dry_32.wav':'dry', 'dry_33.wav':'dry', 'dry_34.wav':'dry','dry_35.wav':'dry', 'dry_36.wav':'dry', 'dry_37.wav':'dry', 'dry_38.wav':'dry','dry_39.wav':'dry', 'dry_40.wav':'dry','dry_41.wav':'dry', 'dry_42.wav':'dry', 'dry_43.wav':'dry', 'dry_44.wav':'dry','dry_45.wav':'dry', 'dry_46.wav':'dry', 'dry_47.wav':'dry', 'dry_48.wav':'dry','dry_49.wav':'dry', 'dry_50.wav':'dry', 'wet_1.wav':'wet', 'wet_2.wav':'wet', 'wet_3.wav':'wet', 'wet_4.wav':'wet', 'wet_5.wav':'wet', 'wet_6.wav':'wet', 'wet_7.wav':'wet', 'wet_8.wav':'wet', 'wet_9.wav':'wet', 'wet_10.wav':'wet','wet_11.wav':'wet', 'wet_12.wav':'wet', 'wet_13.wav':'wet', 'wet_14.wav':'wet', 'wet_15.wav':'wet', 'wet_16.wav':'wet', 'wet_17.wav':'wet', 'wet_18.wav':'wet', 'wet_19.wav':'wet', 'wet_20.wav':'wet', 'wet_21.wav':'wet', 'wet_22.wav':'wet', 'wet_23.wav':'wet', 'wet_24.wav':'wet', 'wet_25.wav':'wet', 'wet_26.wav':'wet', 'wet_27.wav':'wet', 'wet_28.wav':'wet', 'wet_29.wav':'wet', 'wet_30.wav':'wet','wet_31.wav':'wet', 'wet_32.wav':'wet', 'wet_33.wav':'wet', 'wet_34.wav':'wet', 'wet_35.wav':'wet', 'wet_36.wav':'wet', 'wet_37.wav':'wet', 'wet_38.wav':'wet', 'wet_39.wav':'wet', 'wet_40.wav':'wet', 'wet_41.wav':'wet', 'wet_42.wav':'wet', 'wet_43.wav':'wet', 'wet_44.wav':'wet', 'wet_45.wav':'wet', 'wet_46.wav':'wet', 'wet_47.wav':'wet', 'wet_48.wav':'wet', 'wet_49.wav':'wet', 'wet_50.wav':'wet','mid_1.wav':'mid', 'mid_2.wav':'mid', 'mid_3.wav':'mid', 'mid_4.wav':'mid', 'mid_5.wav':'mid', 'mid_6.wav':'mid', 'mid_7.wav':'mid', 'mid_8.wav':'mid', 'mid_9.wav':'mid', 'mid_10.wav':'mid','mid_11.wav':'mid', 'mid_12.wav':'mid', 'mid_13.wav':'mid', 'mid_14.wav':'mid', 'mid_15.wav':'mid', 'mid_16.wav':'mid', 'mid_17.wav':'mid', 'mid_18.wav':'mid', 'mid_19.wav':'mid', 'mid_20.wav':'mid','mid_21.wav':'mid', 'mid_22.wav':'mid', 'mid_23.wav':'mid', 'mid_24.wav':'mid', 'mid_25.wav':'mid', 'mid_26.wav':'mid', 'mid_27.wav':'mid', 'mid_28.wav':'mid', 'mid_29.wav':'mid', 'mid_30.wav':'mid','mid_31.wav':'mid', 'mid_32.wav':'mid', 'mid_33.wav':'mid', 'mid_34.wav':'mid', 'mid_35.wav':'mid', 'mid_36.wav':'mid', 'mid_37.wav':'mid', 'mid_38.wav':'mid', 'mid_39.wav':'mid', 'mid_40.wav':'mid','mid_41.wav':'mid', 'mid_42.wav':'mid', 'mid_43.wav':'mid', 'mid_44.wav':'mid', 'mid_45.wav':'mid', 'mid_46.wav':'mid', 'mid_47.wav':'mid', 'mid_48.wav':'mid', 'mid_49.wav':'mid', 'mid_50.wav':'mid'})


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
           
           
def classify(fileclassify):
    
        result = ''
        result = model.classify('working_test_wav/'+ fileclassify)
        return result
        
  

@app.route("/classify_file", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            level = classify(filename)
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            #data = {
            #    'filename'  : filename,
            #    'level' : level
            #}
            #js = json.dumps(data)

            #resp = Response(js, status=200, mimetype='application/json')
            #resp.headers['Link'] = 'https://server-cdam-paprazzi.c9users.io'

            #return js
            
            return jsonify(filename=filename,
                   level=level)
            
            #return filename + " : "+ level
        else:
            return "failure POST"
            
    elif request.method == 'GET':
         return "Success Get"
        
   
    return "total failure" 
   
            
   
if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
    app.debug(True)
