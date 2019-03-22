from utils import  parser_argument_cmdline
import core.graph as graph

import sys
class BaseStatistics():
    def __init__(self,BasePrices, BaseDriver):
        self.baseprice = BasePrices
        self.basedriver = BaseDriver

        #не присобачил это, и еще  бд


def main():
    all_vert = parser_argument_cmdline(sys.argv)
    base = graph.Graph(all_vert)

    print(base.dijkstra('driver', 'e'))

if __name__ == '__main__':
    main()