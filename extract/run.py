# implement your code here
import csv

file_path = "C:\\Users\\User\PycharmProjects\codeinplace-de-main\extract\data.csv"

data = open(file_path)

reader = csv.reader(data)
lines = list(reader)

print(lines)
