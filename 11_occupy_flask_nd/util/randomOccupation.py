# Team KraZyCodes - Kendrick Liang and Zane Wang
# SoftDev1 pd8
# K10 -- Jinja Tuning
# 2018-09-13

import csv, random
import data

dict = {}
with open('occupations.csv') as csvfile:
    reader = csv.DictReader(csvfile) #using dictreader instead of reader allows us to be able to pass parameters from the 1st row to create dict
    for row in reader:
        dict[row['Job Class']] = float(row['Percentage'])
    del dict['Total']
print(dict)

def randomOccupation():
    randomselect = random.uniform(0,99.9)
    print (randomselect)
    for x in dict:
        randomselect = randomselect - dict[x]
        if (randomselect <= 0):
            return x

    
