#import csv file of LRF dis values
import csv

rows = []
def load_csv(path):
    with open(path, 'r') as f:
        record = csv.reader(f)
        header = next(record)
        for row in record:
            rows.append(row)
    f.close()

def get_dis(time):
    dis = rows[time][1]
    print("LRF dis:", dis)
    return dis