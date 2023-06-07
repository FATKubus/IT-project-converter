import os
import json
import yaml
import xmltodict
from dicttoxml import dicttoxml
import argparse

parser = argparse.ArgumentParser(description="Konwerter plików [.xml], [.json], oraz [.yml]")
parser.add_argument('source_file', help='ścieżka pliku źródłowego (wraz z jego rozszerzeniem)')
parser.add_argument('destination_file', help='ścieżka pliku docelowego (wraz z jego rozszerzeniem)')

args = parser.parse_args()

x = args.source_file
y = args.destination_file

file_name, file_extension = os.path.splitext(x)
file_name_new, file_extension_new = os.path.splitext(y)

