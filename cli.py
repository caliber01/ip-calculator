"""IP calculator

Usage:
  cli.py info <ip_address>
  cli.py split <net_address> <number_of_subnets> [--with-info]
  cli.py (-h | --help)
  cli.py --version

Options:
  --with-info   Print subnet info.
  -h --help     Show this screen.
  --version     Show version.
"""

from docopt import docopt
from IPCalculator import IPCalculator
from IPAddress import IPAddress

if __name__ == '__main__':
    arguments = docopt(__doc__, version='IP calculator 0.01')
    print(arguments)

    ip = IPAddress(arguments['<ip_address>'])
    if arguments['info']:
        print(ip.info())
    if arguments['split']:
        calculator = IPCalculator()
        ip = IPAddress(arguments['<net_address>'])
        number_of_subnets = int(arguments['<number_of_subnets>'])
        subnets = calculator.split_into_subnets(ip, number_of_subnets)
        for subnet in subnets:
            print('subnet: {0}'.format(subnet))
            if (arguments['--with-info']):
                print(subnet.info())
