from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask import copy_current_request_context
from vsearch import search4letters
from markupsafe import escape
from threading import Thread
from werkzeug.utils import secure_filename
import csv
import os
import glob


UPLOAD_FOLDER = 'E:/Python/CSV/temp'
UPLOAD_FILE = ''
ALLOWED_EXTENSIONS = set(['csv', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


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

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':

    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        with open('vsearch.log', 'a') as log:
            print(req.form, req.user_agent.string, res, file=log, sep='|')
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(letters, phrase))
    try:
        #log_request(request, results)
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as err:
        print('*****Logging failed with this error:', str(err))
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)

@app.route('/viewlog')
def view_the_log() -> 'html':
    
    contents = []
    #sourceFile = open('testList2.csv',"r",encoding="utf-8")
    file = glob.glob(os.path.join(app.config['UPLOAD_FOLDER'], "*.csv"))
    sourceFile = open(file[0], "r",encoding="utf-8")
    sourceReader = csv.reader(sourceFile)
    rCount = 0
    for row in sourceReader:
        contents.append([])
        if sourceReader.line_num == 1:
            iCount = 0;
            for item in row:
                match item:
                    case '部門':
                        field_1 = iCount
                    case '姓名':
                        field_2 = iCount
                    case '職稱':
                        field_3 = iCount
                iCount += 1
            continue    # skip first row
        contents[-1].append(row[field_1])
        contents[-1].append(row[field_3])
        contents[-1].append(row[field_2])
        rCount += 1
    
    orderedList = []
    for department in departmentList:
        for row in range(rCount):
            if row % 3 != 0:
                if department == contents[row][0]:
                    orderedList.append([])
                    orderedList[-1].append(contents[row][0])
                    orderedList[-1].append(contents[row][1])
                    orderedList[-1].append(contents[row][2])

    
    titles = ('部門', '職稱', '姓名')
    return render_template('viewlog.html',
                           the_title='View Data',
                           row_count=rCount,
                           the_row_titles=titles,
                           the_data=orderedList,)
                           #the_data=contents,)

"""


"""
            

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
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 
                                   filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))    
            
    return render_template('entry2.html',
                           the_title='Upload new File')
    #return render_template('entry.html',
    #                       the_title='Welcome to search4letters on the web!')

app.secret_key = 'SecretKey'

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=4444)
