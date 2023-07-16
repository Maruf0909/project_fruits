from pprint import pprint
import csv


def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """
    total = 0

    f = open(data, 'r')
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        total += float(row[1])
    f.close()
    return round(total, 2)
pprint(get_total_price('fruits.csv'))
    