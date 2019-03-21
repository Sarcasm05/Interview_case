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
    sys.exit(1)

class Executor(object):
    def __init__(self,filename, persist, mode):
        self.persist = persist
        self.mode = mode
        self.persist = persist
        self.filename = filename

    def compile_test_mysql_serv(self, path):
        path = os.path.abspath(path)

        build_path = os.path.join(self.tmp_dir, 'build')


    def compile_test_mysql_client(self, path):
        path = os.path.abspath(path)

        build_path = os.path.join(self.tmp_dir, 'build')

    def compile_test_json(self, path):
        path = os.path.abspath(path)

        cmd = 'pyinstaller -y -F -w {}'.format(shlex.quote(path))

    def compile_test_sqlite(self,path):
        path = os.path.abspath(path)

