from pathlib import Path
import csv

##annotator1 = open(Path("Annotators/Data1.csv"), 'r')
#annotator2 = open(Path("Annotators/Data2.csv"), 'r')
#annotator3 = open(Path("Annotators/Data3.csv"), 'r')
#annotator4 = open(Path("Annotators/Data4.csv"), 'r')


"""
for a1 in range (3001):
    temp1 = annotator1.readline()
    temp2 = annotator2.readline()
    temp3 = annotator3.readline()
    temp4 = annotator4.readline()
"""
"""
temp1 = annotator1.readline()
print(temp1)
temp2 = annotator1.readline()
temp3 = 
print(temp2)
"""

Data1 = []
with open(Path('Annotators/Data1.csv'), mode = 'r') as infile:
    reader = csv.reader(infile)
    for rows in reader:
        temp_dict = {'id_name':rows[0], 'name':rows[1], 'tweet':rows[2], 'score':rows[3]}
        Data1.append(temp_dict)

Data2 = []
with open(Path('Annotators/Data2.csv'), mode = 'r') as infile:
    reader = csv.reader(infile)
    for rows in reader:
        temp_dict = {'id_name':rows[0], 'name':rows[1], 'tweet':rows[2], 'score':rows[3]}
        Data2.append(temp_dict)

Data3 = []
with open(Path('Annotators/Data2.csv'), mode = 'r') as infile:
    reader = csv.reader(infile)
    for rows in reader:
        temp_dict = {'id_name':rows[0], 'name':rows[1], 'tweet':rows[2], 'score':rows[3]}
        Data3.append(temp_dict)


"""
with open(Path('Annotators/Data1.csv'),mode = 'r') as infile:
    reader = csv.reader(infile)
    mydict = {rows[0]:rows[1] for rows in reader}
    print(mydict)
    """