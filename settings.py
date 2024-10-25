# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:18:33 2024

@author: user
"""
from flask import Flask

UPLOAD_FOLDER = 'E:/Python/CSV/upload'
UPLOAD_FILE = ''

def init():
    global app
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
    
    
    global departmentList
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