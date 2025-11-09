import csv

def get_test_data(file_path):
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

data = get_test_data(r"C:\Users\saite\OneDrive\Documents\SeleniumProject\Data\test_data.csv")
print(data)

