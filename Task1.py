import os
import json
import yaml
import xmltodict

import argparse


parser = argparse.ArgumentParser(description='Konwertuj pliki między formatami .xml, .json i .yml.')
parser.add_argument('--source', type=str, help='Ścieżka pliku źródłowego (w tym jego rozszerzenie).')
parser.add_argument('--dest', type=str, help='Ścieżka pliku docelowego i rozszerzenie, w którym chcesz go zapisać
.')
args = parser.parse_args()

a = args.source
b = args.dest

