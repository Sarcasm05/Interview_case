import json 
import argparse
from keysbrdsky.core.graph import Graph
from keysbrdsky.package.vertex import Vertex
def get_path(path)

    with open(path, 'r') as f: arr = json.load(f)

    return ([Vertex('driver', val, arr['PathLength'][val]) for val in arr['PathLength'].keys()], ['viewbenzkm'])


def parser_argument_cmdline():

    parser = argparse.ArgumentParser(description='This is finder of min path for drivers')
    parser.add_argument('-c', '--city', description='json file of coordinates gaseline in city', default='resources/driver/driverd.json')
    parser.add_argument('-d', '--drivers', description='json file of coordinates and characteristics driver')
    args = parser.parse_args()

    pair_t = get_path(args.drivers)

    arr_vert = list([val for val in pair_t[0] if pair_t[1] < val.cost])

    all_vert = [val for val in pair_t[0]]
    graph = Graph(all_vert)



