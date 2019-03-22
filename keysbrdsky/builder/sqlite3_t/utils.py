from keysbrdsky.core.adoptbranch import AdoptBranch
import argparse

def get_path(price):
    with AdoptBranch() as bd:
        bd.execute(AdoptBranch.select_path())
        return bd.fetchall()

def add_gaseline(gaseline, price, path):
    with AdoptBranch() as bd:
       bd.execute(AdoptBranch.insert_gaseline(gaseline, price, path)

def parser_argument_cmdline():
    parser = argparse.ArgumentParser(description='This is finder of min path for drivers')
    parser.add_argument('-s', '--sity', description='json file of coordinates gaseline in city',
                      default='resources/city/gasestatdb.db')
    parser.add_argument('-d', '--drivers', description='json file of coordinates and characteristics driver')
    parser.add_argument('-i', '--insert', type=str)
    args = parser.parse_args()

#    price = json.d...
    city_arr = get_path(price)
    return args.city, args.drivers
