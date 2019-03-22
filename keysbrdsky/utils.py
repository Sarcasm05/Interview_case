

try:
    from keysbrdsky.package.vertex import Vertex
    from keysbrdsky.module.prices import BasePrices
    from keysbrdsky.module.driver import BaseDriver
except:
    from package.vertex import Vertex
    from module.prices import BasePrices
    from module.driver import BaseDriver
finally:

    import json
    import argparse

def get_path(path, priotitykeys='viewbenzkm'):

    with open(path, 'r') as f:
        arr = json.load(f)

    return ([Vertex('driver', val, arr['PathLength'][val]) for val in arr['PathLength'].keys()], arr[priotitykeys])


def get_all_vert(path):
    with open(path, 'r') as f:
        arr = json.load(f)

    return  ([Vertex(key, val, arr[key]['PathLength'][val]) for key in arr.keys() for val in arr[key]['PathLength']])



def parser_argument_cmdline(priotitykeys='viewbenzkm'):

    parser = argparse.ArgumentParser(description='This is finder of min path for drivers')
    parser.add_argument('-c', '--city', help='json file of coordinates gaseline in city', default='resources//maps//test.json')
    parser.add_argument('-d', '--drivers', help='json file of coordinates and characteristics driver',default='resources//driver//driverd.json')
    args = parser.parse_args()

    pair_t = get_path(args.drivers)

    all_vert = get_all_vert(args.city)
    path_driv = get_path(args.drivers)
    for x in path_driv[0]:
        all_vert.append(x)

    return (all_vert)


import sys
#parser_argument_cmdline()


