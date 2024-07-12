# import configparser
# import argparse
#
# parser = argparse.ArgumentParser(description='Update ini file')
# parser.add_argument('--option', type= str, required=True, help='Option to update')
# parser.add_argument('--value', type=str, required=True, help='New value for the option')
# args = parser.parse_args()
#
# config = configparser.ConfigParser()
# config.read('properties.ini')
#
# config['DEFAULT'][args.option] = args.value