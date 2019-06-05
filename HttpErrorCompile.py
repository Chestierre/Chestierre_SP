from pathlib import Path
import csv


Data = []
with open(Path('Annotators/httpErrorData.csv'), mode = 'r') as infile:
    reader = csv.reader(infile)
    for rows in reader:
        temp_dict = {'tweet_number':rows[0], 'Anno_data':rows[1], 'Pers_man':rows[2], 'Pers_auto':rows[3]}
        if temp_dict['Pers_auto'] != 'HttpError':
            Data.append(temp_dict)

with open(Path('Annotators/httpErrorResult.csv'), 'w', newline = '\n') as f:
    writer = csv.writer(f)


print(Data)
for i in range (len(Data)):
    with open(Path('Annotators/httpErrorResult.csv'), 'a', newline = '\n') as f:
            writer = csv.writer(f)
            writer.writerow([Data[i]['tweet_number'], Data[i]['Anno_data'], Data[i]['Pers_man'], Data[i]['Pers_auto']])
