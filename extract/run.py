# implement your code here
import csv

def extract_data():
    file_path = "C:\\Users\\User\PycharmProjects\codeinplace-de-main\extract\data.csv"

    data = open(file_path)

    reader = csv.reader(data)
    lines = list(reader)
    print("-------------------------------")
    print(lines)
    print("-------------------------------")
    datalist = []

    for row in lines:
        name = row[0].strip().lower()
        number = int(row[1].strip())
        datalist.append([name, number])
    print(datalist)
    data.close()
    return datalist


if __name__ == "__main__":
    extract_data()





# assert result == [
#     ["lionel messi", 97],
#     ["jisung park", 99],
#     ["heungmin son", 102],
# ]