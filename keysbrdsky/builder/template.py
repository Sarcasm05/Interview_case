# Description: Execute creator

import os
import sys
import zlib
import shlex
import shutil


try:
    from PyInstaller import __main__ as pyi, is_win
except:
    print('Please install Pyinstaller: pip install pyinstaller')



# создаем бд, выгружаем город. Подрузомеваем, что потом, нам нужно будет реализовать свой веб сервер и клиент
# Базу данных берем MysSQLDB,для обеспечения параллельных к ней запросов.


class Executor(object):
    def __init__(self,filename, persist, mode):

        self.filename = filename

    def compile_test_mysql_serv(self, path):
        path = os.path.abspath(path)

        build_path = os.path.join(self.tmp_dir, 'build')


    def compile_test_mysql_client(self, path):
        path = os.path.abspath(path)

        build_path = os.path.join(self.tmp_dir, 'build')

    @staticmethod
    def compile_test_json():
        #path = os.path.abspath()
        out = "%s\n%s\n\n%s\n%s\n\n%s\n\n%s\n%s\n%s\n%s\n%s\n" % (
            "import json ",
            "import argparse",
            "def get_path()",
            "    return '' ",
            "def parser_argument_cmdline():",
            "    parser = argparse.ArgumentParser(description='This is finder of min path for drivers')",
            "    parser.add_argument('-s', '--sity', description='json file of coordinates gaseline in city', default='resources/driver/driverd.json')",
            "    parser.add_argument('-d', '--drivers', description='json file of coordinates and characteristics driver')",
            "    args = parser.parse_args()",
            "    return args.city, args.drivers")

        with open('builder/json_t/utils.py', 'w') as file_obj:
            file_obj.write(str(out))

        print("paste of utils test json!")



    @staticmethod
    def compile_test_sqlite():
        out = "%s\n%s\n\n%s\n%s\n%s\n%s\n\n%s\n%s\n%s\n\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n" % (
            "from keysbrdsky.core.adoptbranch import AdoptBranch",
            "import argparse",
            "def get_path(price):",
            "    with AdoptBranch() as bd:",
            "        bd.execute(AdoptBranch.select_path())",
            "        return bd.fetchall()",
            "def add_gaseline(gaseline, price, path):",
            "    with AdoptBranch() as bd:",
            "       bd.execute(AdoptBranch.insert_gaseline(gaseline, price, path)",
            "def parser_argument_cmdline():",
            "    parser = argparse.ArgumentParser(description='This is finder of min path for drivers')",
            "    parser.add_argument('-s', '--sity', description='json file of coordinates gaseline in city',",
            "                      default='resources/city/gasestatdb.db')",
            "    parser.add_argument('-d', '--drivers', description='json file of coordinates and characteristics driver')",
            "    parser.add_argument('-i', '--insert', type=str)",
            "    args = parser.parse_args()",
            "    return args.city, args.drivers")

        with open('builder/sqlite3_t/utils.py', 'w') as file_obj:
            file_obj.write(out)


        print("paste of utils test sqlite!")

