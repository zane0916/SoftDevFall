# Team PandaBearBBT - Tania Cao Su and Zane Wang
# SoftDev1 pd8
# K17 -- Average
# 2018-10-05 F

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#searches database for students, courses the student is in, and the grade the
#student has gotten in that course
def searchGrades():
    command = "SELECT {0},{1},{2} FROM {3},{4} WHERE {5} = {6}".format("name","code","mark","peeps_info","courses_info","peeps_info.id","courses_info.id")
    c.execute(command)
    print("ALL STUDENTS WITH THE CLASSES THEY ARE TAKING AND THEIR CORRESPONDING GRADES IN THOSE CLASSES:")
    for row in c:
        print(row)
    return c

#calc avg of students, makes a list of students and their corresponding ids
def calcAvg():
    idList = []
    markList = []
    avgList = []

    #list of all ids in idList
    command = "SELECT {0} FROM {1}".format("id","peeps_info")
    c.execute(command)
    for row in c:
        idList.append(row[0])

    print("ALL THE IDS")
    for id in idList:
        print(id)

    #list of all marks per id
    command = "SELECT {0},{1} FROM {2},{3} WHERE {4} = {5}".format("peeps_info.id","mark","peeps_info","courses_info","peeps_info.id","courses_info.id")
    c.execute(command)
    print("ALL THE SELECTED ROWS IN C")
    for row in c:
        print(row)
    for id in idList:
        for row in c:
            idMark = []
            if row[0] == id:
                print(row[1])
                idMark.append(row[1])
        markList.append([idMark])

    print("ALL THE MARKS IN MARKLIST")
    for mark in markList:
        print(mark)

'''    #returns a list of ids and avgs of students
    command = "SELECT {0},{1},{2} FROM {3},{4} WHERE {5} = {6}".format("peeps_info.id","name","mark","peeps_info","courses_info","peeps_info.id","courses_info.id")
    c.execute(command)
    for id in idList:
        num = 0
        classes = 0
        for row in c:
            if row[0] == id:
                num += row[2]
                classes += 1
        avgList.append([id, num/classes])
    return avgList

# sum()/len()
#
   '''

#calcs and inputs the averages into a table consisting of a student with their corresponding average
def makeAvgTable():
    command = "CREATE TABLE if not exists {0}({1}, {2});".format("peeps_avg","id INTEGER","avg INTEGER")
    c.execute(command)
    avgList = calcAvg()
    for row in avgList:
        command = "INSERT INTO {0} VALUES({1},{2}".format(avgList[0],avgList[1])
        c.execute(command)

#selects the name, id, and avgs of all students, so that they can be displayed using the main method later
def displayAvg():
    command = "SELECT {0},{1},{2} FROM {3},{4} WHERE {5} = {6}".format("name","peeps_info.id","avg","peeps_info","peeps_avg","peeps_info.id","peeps_avg.id",)
    c.execute(command)
    return c

def main():
    searchGrades()
    calcAvg()
    makeAvgTable()
    #run display to set c as the one from displayAvg()
    displayAvg()
    for row in c:
        print(row)

main()

db.commit() #save changes
db.close() #close database
