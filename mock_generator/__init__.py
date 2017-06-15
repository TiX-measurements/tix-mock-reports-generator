import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('ip', action='store',
                            help='Ip of the report')
    parser.add_argument('user_id', type=int, action='store',
                        help='Account\'s id where data wil be generated')
    parser.add_argument('username', action='store',
                        help='Account\'s Username where data will be generated')
    parser.add_argument('password', action='store',
                        help='Account\'s Password where data will be generated')
    parser.add_argument('installation_id', type=int, action='store',
                        help='Account\'s installation id where data will be generated')
    parser.add_argument('provider_id', type=int, action='store',
                        help='Dummy provider from which all the packets will be')
    parser.add_argument('from_time', action='store',
                        help='Date since when to generate data')
    parser.add_argument('to_time', action='store',
                        help='Date until when to generate data')
    parser.add_argument('-s', '--server', dest='server', action='store',
                        help='Server URL where to hit', default='https://tix.innova-red.net')
    return parser.parse_args()
