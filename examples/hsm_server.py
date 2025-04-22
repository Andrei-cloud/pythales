#!/usr/bin/env python

import getopt
import sys

# Ensure local pythales module is used before any global installation
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pythales.hsm import HSM

def show_help(name):
    """
    Show help and basic usage
    """
    print('Usage: python3 {} [OPTIONS]... '.format(name))
    print('Thales HSM command simulator')
    print('  -p, --port=[PORT]\t\tTCP port to listen, 1500 by default')
    print('  -k, --key=[KEY]\t\tTCP port to listen, 1500 by default')
    print('  -d, --debug\t\t\tEnable debug mode (show CVV/PVV mismatch etc)')
    print('  -s, --skip-parity\t\t\tSkip key parity checks')
    print('  -a, --approve-all\t\t\tApprove all requests')


if __name__ == '__main__':
    port = None
    header = ''
    key = None
    debug = False
    skip_parity = None
    approve_all = None

    optlist, args = getopt.getopt(sys.argv[1:], 'h:p:k:dsa', ['header=', 'port=', 'key=', 'debug', 'skip-parity', 'approve-all', 'help'])
    for opt, arg in optlist:
        if opt in ('-p', '--port'):
            try:
                port = int(arg)
            except ValueError:
                print('Invalid TCP port: {}'.format(arg))
                sys.exit()
        elif opt in ('-k', '--key'):
            key = arg
        elif opt in ('-d', '--debug'):
            debug = True
        elif opt in ('-s', '--skip-parity'):
            skip_parity = True
        elif opt in ('-a', '--approve-all'):
            approve_all = True
        elif opt in ( '--help'):
            show_help(sys.argv[0])
            sys.exit()

    hsm = HSM(port=port, key=key, debug=debug, skip_parity=skip_parity, approve_all=approve_all)
    try:
        hsm.run()
    except KeyboardInterrupt:
        print("\nServer shutdown requested, exiting...")
        sys.exit(0)
