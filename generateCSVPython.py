
import csv
import random
from faker import Faker

def datagenerate(records, headers):
    with open("GenerateFields.csv", 'w', newline='') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):           
            writer.writerow({
                    #Edit your fields or even better you can randonize them
                    "AccountNumber" : random.choice(['12345 7777','12345 8888', '12345 9999','12345 5555']),
                    "BatchDate" : random.choice(['2024-09-10', '2020-09-10']),
                    "Region": random.choice(['Atlantic', 'Pacific','Central', 'Maritimes']),
                    "Culture Code": random.choice(['French', 'English']),
                    })
    
if __name__ == '__main__':
    #select how many records you want:    
    records = 250 
    headers = ["AccountNumber","BatchDate","Region", "Culture Code"]
    datagenerate(records, headers)
    print("CSV generation complete!")
