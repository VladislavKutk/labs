import csv
import sys

def calculate(dump, ip):
    traffic = 0
    for elem in dump:
        if elem[1].find(ip) != -1: traffic_str = elem[3]
        elif elem[2].find(ip) != -1: traffic_str = elem[4]
        if traffic_str.find('M') == -1: traffic += int(traffic_str)
        else: traffic += float(traffic_str[:traffic_str.find('M')]) * 1024 * 1024
    traffic -= 1000 if traffic >= 1000 else 0
    return '%.2f' % (traffic / 1024 / 1024)
        
def main():
    with open('dump.csv','r') as csv_dump:
        print(calculate(csv.reader(csv_dump),sys.argv[1]))

if __name__ == '__main__':
    main()