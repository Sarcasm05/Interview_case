import argparse


def main():
    """
    Run the keysbrdsky setup script
    """

    parser = argparse.ArgumentParser(description='install depends and compile test')
    parser.add_argument('-r', '--path',  default='requirements.txt',type=str)
    parser.add_argument('-b', '--builder',type=str,help='mode of build')
    args = parser.parse_args()

    import os
    import sys
    import urllib.request
    import getpass
    import subprocess

    try:
        pip_path = subprocess.check_output('where pip' if os.name == 'nt' else 'which pip', shell=True).strip().rstrip()
    except Exception as e:
        print("Error in pip package installer: {}".format(str(e)))


    if not bool('pip' in locals() and os.path.exists(pip_path)):
        try:
            exec(urllib.request.urlopen("https://bootstrap.pypa.io/get-pip.py").read(), globals())
        except Exception as e:
            print("Error installing pip: {}".format(str(e)))

        os.execv(sys.executable, ['python'] + [os.path.abspath(sys.argv[0])] + sys.argv[1:])

    requirements = args.path

    # install requirements
    sudo_passwd = getpass.getpass('Enter your sudo password (to install python dependencies): ') if os.name == 'posix' else ''
    with open(requirements, 'r') as file_obj:
        requirements = file_obj.readlines()
    print(requirements)
    for i, _ in enumerate(requirements):
        try:
            print("Installing {}...".format(_.rstrip()))
            print('pip install')
            locals()['pip_install_%d' % i] = subprocess.Popen('{} install {}'.format(pip_path if os.name == 'nt' else 'sudo {}'.format(pip_path), _.rstrip()), 0, None, subprocess.PIPE, subprocess.PIPE, subprocess.PIPE, shell=True)
            if i == 0:
                locals()['pip_install_%d' % i].communicate(sudo_passwd + '\n')
        except Exception as e:
            print("Error installing package: {}".format(_))


    for x in range(20):
        if 'pip_install_%d' % x in locals():
            locals()['pip_install_%d' % x].wait()


    if args.builder:
        from keysbrdsky.builder import template
        runner = template.Executor(args.path,args.persist, args.mode)

        if  'mysqldb' in args.builder:
            runner.compile_test_mysql_client()
            runner.compile_test_mysql_serv()
        elif  'json' in args.builder:
            runner.compile_test_json()
        elif 'sqlite' in args.builder:
            runner.compile_test_sqlite()


if __name__ == '__main__':
    main()