# implement your code here
import csv

def extract_data():
    file_path = "C:\\Users\\User\PycharmProjects\codeinplace-de-main\extract\data.csv"

    # data = open(file_path)
    with open(file_path) as data:
        reader = csv.reader(data)
        lines = list(reader)
        print("-------------------------------")
        print(lines)
        print("-------------------------------")
        datalist = []

        for row in lines:
            name = row[0].strip().lower()
            score = int(row[1].strip())
            datalist.append([name, score])
        print(datalist)
        # data.close() // open-close를 with로 변경
    return datalist

if __name__ == "__main__":
    extract_data()
