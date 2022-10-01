main_title: Python Libraries Cheatsheet
lang: python

#---------------------------------------------------------------------------------------------------
title: argparse
    # Argument expecting one argument
    parser.add_argument('--indice', '-i', default='CAC 40', action='store', dest='indices', help='Process indices')
    # python argparse_sample.py -i CAC\ 40
    # Namespace(auto_create=False, equities=None, indices='CAC 40')

    # Arguments can be repeated
    parser.add_argument('--equity', '-e', action='append', dest='equities', help='Process equities')
    # python argparse_sample.py -i CAC\ 40 -e 'GLE.PA' -e 'SGOB.PA'
    # Namespace(auto_create=False, equities=['GLE.PA', 'SGOB.PA'], indices='CAC 40')

    # Argument without a value (boolean value)
    parser.add_argument('--auto-create', default=False, action='store_true', dest='auto_create', help='Automatically create equity')
    # python argparse_sample.py -i CAC\ 40 -e 'GLE.PA' -e 'SGOB.PA' --auto-create
    # Namespace(auto_create=True, equities=['GLE.PA', 'SGOB.PA'], indices='CAC 40')

    # Argument without a typed value
    parser.add_argument('--interval', default=30, action='store', dest='interval', help='Interval time')
    # python argparse_sample.py
    # Namespace(auto_create=False, equities=None, indices='CAC 40', interval=30)
    # python argparse_sample.py --interval=22
    # Namespace(auto_create=False, equities=None, indices='CAC 40', interval='22')
    # python argparse_sample.py --interval 32
    # Namespace(auto_create=False, equities=None, indices='CAC 40', interval='32')

#---------------------------------------------------------------------------------------------------