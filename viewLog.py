# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:11:17 2024

@author: user
"""
from flask import Flask, render_template
import csv
import os
import glob

#app = Flask(__name__)
testFirst = '1120515'
testSecond = '1121021'

FAILED_FIRST = set(['丁敬祐', '王凱薇', '巫慧萍', '曾俊凱', '呂丞棋', '陳羽眉'])
FAILED_SECOND = set(['王美琴', '陳聖妮', '廖耿徽', '賴冠龍'])
def failedOne(name, failedSet):
    return name in failedSet

def view_the_log(path, dList) -> 'html':    
    contents = []
    contents_new = []
    files = glob.glob(os.path.join(path, "*.csv"))
    file_name = ''
    rCount = 0
    rCount_new = 0
    
    new_arrival = set()
    for file in files: 
        file_name = os.path.basename(file)
        sourceFile = open(file, "r",encoding="utf-8")
        sourceReader = csv.reader(sourceFile)
        if file_name == "newArrival.csv":
            for row in sourceReader:
                if sourceReader.line_num > 2:
                    contents_new.append([])
                    contents_new[-1].append(row[1])
                    contents_new[-1].append(row[5])
                    contents_new[-1].append(row[2])
                    new_arrival.add(row[2])
                    rCount_new += 1
    
    for file in files: 
        file_name = os.path.basename(file)
        sourceFile = open(file, "r",encoding="utf-8")
        sourceReader = csv.reader(sourceFile)
        if file_name == "testList2.csv":
            for row in sourceReader:
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
                else:
                    contents.append([])
                    contents[-1].append(row[field_1])
                    contents[-1].append(row[field_3])
                    contents[-1].append(row[field_2])
                    rCount += 1
          
    orderedList = []
    for row in contents:
        name = row[2]
        arrivalDate = '1120101'
        update = False
        credit = 0
        if failedOne(name, FAILED_FIRST):
            credit -= 3
        if failedOne(name, FAILED_SECOND):
            credit -= 3
        for row_new in contents_new:
            if name == row_new[1]:
                arrivalDate = row_new[2]
                update = True
                if (credit == 0):
                    if (arrivalDate < testFirst):
                        credit += 1              
                else:
                    rCount -= 1
        if  (update == False and credit == 0):           
            credit += 1  
        if (credit != 0):                          
            for department in dList:   
                if department == row[0]:
                    orderedList.append([])
                    orderedList[-1].append(row[0])
                    orderedList[-1].append(row[1])
                    orderedList[-1].append(name)
                    orderedList[-1].append(arrivalDate)
                    orderedList[-1].append(update)
                    orderedList[-1].append(credit) 

    
    titles = ('部門', '職稱', '姓名', '報到日', '新人', '積分')
    return render_template('viewlog.html',
                           the_title='View Data',
                           the_file=file_name,
                           row_count=rCount,
                           the_row_titles=titles,
                           the_data=orderedList,)
