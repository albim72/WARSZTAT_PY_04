import csv

with open("firma.csv",encoding="utf-8") as pc:
    csv_reader = csv.reader(pc,delimiter=",")
    line_count = 0
    empty_line = 0
    for row in csv_reader:
        if line_count==0:
            print(f'Nazwy kolumn -> {" -> ".join(row)}')
            line_count += 1
        else:
            if len(row)<2:
                line_count += 1
                empty_line += 1
            else:
                print(f'\t{row[0]} pracuje na stanowisku: {row[1]} i ma urodziny w miesiącu: {row[2]}'
                      f', otrzymuje nagrodę finansową: {row[3]} zł')
                line_count += 1
    print(f"dodano {line_count} linii")
    print(f"dodano {line_count-1-empty_line} osób")
    print(f"pustych linii {empty_line}")
