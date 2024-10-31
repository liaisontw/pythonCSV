from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask import copy_current_request_context
from viewLog import view_the_log
from testFunctions import the_new_arrival, create_sample_excel, the_department
from markupsafe import escape
from threading import Thread
from werkzeug.utils import secure_filename
import csv
import os
import glob
#import settings


ALLOWED_EXTENSIONS = set(['csv', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = 'E:/Python/CSV/upload'
UPLOAD_FILE = ''
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB


departmentList = [
    '局長室',     '副局長室',   '秘書室',     
    '火災調查科', '災害預防科', '災害搶救科', '災害管理科',  '緊急救護科', 
    '教育訓練科', '勤務指揮科', '行政科', '人事室',  '會計室', '政風室', 
    '第一大隊', 
    '竹北分隊', '光明分隊',  '豐田分隊', '新豐分隊', '山崎分隊', 
    '第二大隊', 
    '竹東分隊', '二重分隊',  '北埔分隊', '峨眉分隊', '寶山分隊', 
    '橫山分隊', '尖石分隊',  '五峰分隊', 
    '第三大隊', 
    '湖口分隊', '新工分隊', '新埔分隊',  '關西分隊', '芎林分隊'
]


@app.route('/xlsOutput', methods=['GET', 'POST'])
def sample_excel() -> 'html':
    create_sample_excel()
    return render_template('entry2.html',
                           the_title='Create sample excel')


@app.route('/viewlog', methods=['GET', 'POST'])
def view_logs():
    return view_the_log(app.config['UPLOAD_FOLDER'], departmentList)

@app.route('/newArrival', methods=['GET', 'POST'])
def new_arrival():
    return the_new_arrival(app.config['UPLOAD_FOLDER'])

@app.route('/department', methods=['GET', 'POST'])
def department():
    return the_department(app.config['UPLOAD_FOLDER'])


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
         

@app.route('/', methods=['GET', 'POST'])
#@app.route('/entry', methods=['GET', 'POST'])
def entry_page() -> 'html':
    if request.method == 'POST':
        #file = request.files['file']
        files = request.files.getlist("file") 
        for file in files: 
            app.logger.info(file)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], 
                                       filename))
        return redirect(url_for('uploaded_file',
                                        filename=filename))    
            
    return render_template('entry2.html',
                           the_title='Upload new File')

app.secret_key = 'SecretKey'

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=4444)
