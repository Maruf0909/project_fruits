from pprint import pprint
import csv


def get_cheapest_fruit_id(data: str) -> int:
    """
    This function returns the index of the cheapest fruit

    args:
        data (str): CSV file with the fruits data
    returns:
        int: id of the cheapest fruit
    """
    # your code here
    f = open(data, 'r')
    reader = csv.reader(f)
    fruits=list(reader)
    cheapest=fruits[1]
    for fruit in fruits[2:]:
        if float(fruit[1])<float(cheapest[1]):
            cheapest=fruit
    f.close()
    return fruits.index(cheapest)
data='fruits.csv'
pprint(get_cheapest_fruit_id(data))



    