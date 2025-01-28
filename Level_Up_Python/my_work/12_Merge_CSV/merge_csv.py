from typing import List
import csv

def merge_csv(input_files: List, output: str) -> None:
    columns = []

    for file in input_files:
        with open(file, 'r') as file_in:
            field = csv.DictReader(file_in).fieldnames
            for f in field:
                if f not in columns:
                    columns.append(f)

    with open(output, 'w') as file:
        writer = csv.DictWriter(f=file, fieldnames=columns)
        writer.writeheader()
        for f in input_files:
            with open(f) as in_file:
                reader = csv.DictReader(in_file)
                for row in reader:
                    writer.writerow(row)

merge_csv(['class1.csv', 'class2.csv'], 'all_students.csv')
