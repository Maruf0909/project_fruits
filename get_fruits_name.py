import csv
import pprint


def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    f=open(data, 'r')
    reader=csv.reader(f)
    s=[]
    for row in list(reader)[1:]:
        name=row[0]
        s.append(name)
    return s

x='fruits.csv'
s=get_frutis_name(x)
print(s)
pprint.pprint(s)

    