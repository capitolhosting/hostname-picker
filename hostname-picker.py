import argparse
import json
import os
import random

def main():
    parser = argparse.ArgumentParser(description='Pick a random name from a given category')
    parser.add_argument('-c', '--category', type=str, choices=['birds', 'artists',], required=True, help='The category to choose from')
    args = parser.parse_args()

    category = args.category
    data_dir = './data/'
    filename = data_dir + category + '.json'

    if os.path.exists(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        selected_item = random.choice(data)
        selected_item_with_hyphens = selected_item.replace(' ', '-')
        print(selected_item_with_hyphens)
    else:
        print(f'Error: File {filename} does not exist')
        print_usage()

def print_usage():
    print("""
    Usage: hostname-generator.py [-h] -c {category-name}
    ex:    hostname-generator.py -c birds

    Generate a random name from a given category

    optional arguments:
      -h, --help            show this help message and exit
      -c, --category        The category to choose from
                            Category is chosen by the filename in ./data/{filename}.json
    """)

if __name__ == '__main__':
    main()
