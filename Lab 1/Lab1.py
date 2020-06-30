import sys
import csv

def calculate(dictionary, phone_number):
    calls_min = 0
    sms_num = 0

    for row in dictionary:
        if row['msisdn_origin'] == phone_number:
            calls_min += float(row['call_duration'])
            sms_num += int(row['sms_number'])
        if row['msisdn_dest'] == phone_number: calls_min += float(row['call_duration'])
    sms_num -= 5  if  sms_num >= 5 else 0 
    return calls_min + sms_num

def main():
    csv_reader = csv.DictReader(open("data.csv","r"))
    cost = calculate(csv_reader, sys.argv[1])
    print('%.2f' % cost,'руб.')

if __name__ == '__main__':
    main()