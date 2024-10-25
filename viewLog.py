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

def the_new_arrival(path) -> 'html':    
    contents_new = []
    files = glob.glob(os.path.join(path, "*.csv"))
    file_name = ''
    rCount_new = 0
    for file in files: 
        file_name = os.path.basename(file)
        if file_name == "newArrival.csv":
            sourceFile = open(file, "r",encoding="utf-8")
            sourceReader = csv.reader(sourceFile)
            for row in sourceReader:
                contents_new.append([])
                if sourceReader.line_num > 2:
                    contents_new[-1].append(row[1])
                    contents_new[-1].append(row[7])
                    contents_new[-1].append(row[5])
                    contents_new[-1].append(row[2])
                    rCount_new += 1
       
    titles = ('部門', '職稱', '姓名', '報到日')
    return render_template('viewlog.html',
                           the_title='New Arrival',
                           the_file=file_name,
                           row_count=rCount_new,
                           the_row_titles=titles,
                           the_data=contents_new,)


def view_the_log(path, dList) -> 'html':    
    contents = []
    contents_new = []
    files = glob.glob(os.path.join(path, "*.csv"))
    file_name = ''
    rCount = 0
    rCount_new = 0
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
                
        if file_name == "newArrival.csv":
            for row in sourceReader:
                if sourceReader.line_num > 2:
                    contents_new.append([])
                    contents_new[-1].append(row[1])
                    contents_new[-1].append(row[5])
                    contents_new[-1].append(row[2])
                    rCount_new += 1
          
            
    orderedList = []
    for department in dList:
        for index in range(rCount):
            row = index
            if department == contents[row][0]:
                orderedList.append([])
                orderedList[-1].append(contents[row][0])
                orderedList[-1].append(contents[row][1])
                orderedList[-1].append(contents[row][2])
                update = False
                for row_new in range(rCount_new):
                    if contents[row][2] == contents_new[row_new][1]:
                        orderedList[-1].append(contents_new[row_new][2])
                        orderedList[-1].append('YES')
                        update = True
                if  update == False:
                    orderedList[-1].append('1120101')
                    orderedList[-1].append('NO')
                            
    
    titles = ('部門', '職稱', '姓名', '報到日', '新人')
    return render_template('viewlog.html',
                           the_title='View Data',
                           the_file=file_name,
                           row_count=rCount,
                           the_row_titles=titles,
                           the_data=orderedList,)


