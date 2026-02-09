import csv
with open("D:\\DS_AI_Internship\\src\\Day7\\student.csv","r")as file:
    reader=csv.DictReader(file)
    print("Students who passed:")
    for row in reader:
        if row["status"] == "Pass":
            print(row["Name"])