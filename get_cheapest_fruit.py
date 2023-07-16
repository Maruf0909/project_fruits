from pprint import pprint
import csv


def get_cheapest_fruit(data: str) -> str:
    """
    This function returns the name of the cheapest fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the cheapest fruit
    """
    # your code here
    f = open(data, 'r')
    reader=csv.reader(f)
    fruits=list(reader)
    most_expensive=fruits[1]
    for fruit in fruits[2:]:
        if float(fruit[1])<float(most_expensive[1]):
            most_expensive=fruit

    f.close()


    return most_expensive[0] 
data='fruits.csv'
pprint(get_cheapest_fruit(data))


