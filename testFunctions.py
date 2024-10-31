# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 09:27:30 2024

@author: user
"""

from flask import Flask, render_template
import csv
import os
import glob

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