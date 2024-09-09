# implement your code here
import csv

file_path = "/extract/data.csv"

data = open(file_path)

reader = csv.reader(data)
lines = list(reader)

print(lines)
