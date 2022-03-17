import json, csv
from pathlib import Path
from assesment.settings import BASE_DIR

BASE_DIR = str(BASE_DIR)

def check_type(doc_url):
    doc_url = BASE_DIR + doc_url
    suffix = Path(doc_url).suffix
    return suffix
    

def file_data(doc_url):
    doc_url = BASE_DIR + doc_url
    with open(doc_url) as file:
        data = file.read()
        return data


def csv_read(doc_url):
    doc_url = BASE_DIR + doc_url
    with open(doc_url) as file:
        reader = csv.reader(file)
        data = []
        for row in reader:  
            data.append(row)
        return data

def json_read(doc_url):
    doc_url = BASE_DIR + doc_url
    with open(doc_url) as file:
        data = json.load(file)
        return data


def check_file(prefix, doc_url):
    if prefix == '.json':
        data = json_read(doc_url)
    elif prefix == '.sql':
        data = 'sql'
    elif prefix == '.xml':
        data = 'xml'
    elif prefix == '.csv':
        data = csv_read(doc_url)

    return data