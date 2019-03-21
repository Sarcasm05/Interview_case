__all__ = ['vertex']

__version__ = '0.1'
__license__ = 'GPLv3'
__author__ =  'Ramazanov Rustam'
__github__ =  'https://github.com/Sarcasm05/keybrdsky'

def main():
    for module in __all__:
        exec("import {}".format(module))

main()