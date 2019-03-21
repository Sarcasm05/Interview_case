from keysbrdsky.package.vertex import Vertex
from keysbrdsky.module.prices import BasePrices
from keysbrdsky.core.graph import Graph


import json
import argparse


def pars_req_json(mapjson):




def main():
    parser = argparse.ArgumentParser(description='This is finder of min path for drivers')
    parser.add_argument('-s', '--sity', description='json file of coordinates gaseline in city', default='resources/driver/driverd.json')
    parser.add_argument('-d', '--drivers', description='json file of coordinates and characteristics driver')
    parser.add_argument('-m', '--mode', description='use MySQLdb for testing || json || sqllite3')
    args = parser.parse_args()







#создаем бд, выгружаем город. Подрузомеваем, что потом, нам нужно будет реализовать свой веб сервер и клиент
#Базу данных берем MysSQLDB,для обеспечения параллельных к ней запросов.










