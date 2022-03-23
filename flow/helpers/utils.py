import json, csv
from pathlib import Path
from assesment.settings import BASE_DIR

BASE_DIR = str(BASE_DIR)

def check_type(doc_url):
    doc_url = BASE_DIR + doc_url
    suffix = Path(doc_url).suffix
    return suffix
    

# def file_data(doc_url):
#     doc_url = BASE_DIR + doc_url
#     with open(doc_url) as file:
#         data = file.read()
#         return data


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


#save file 
def save_doc_file(prefix, doc_url, data):
    if prefix == '.json':
        # data = json_read(doc_url)
        json_save(doc_url, data)
    elif prefix == '.sql':
        data = 'sql'
    elif prefix == '.xml':
        data = 'xml'
    elif prefix == '.csv':
        return csv_save(doc_url, data)



def csv_save(doc_url, data):
    doc_url = BASE_DIR + doc_url
    with open(doc_url, 'a', newline='') as file:
        writer = csv.writer(file, dialect='excel')
        writer.writerow(data)


def json_save(doc_url, data):
    current_doc = BASE_DIR + doc_url
    keys = ["id", "first_name", "last_name", "email", "gender", "ip_address"]
    dictionary = {keys[i]: data[i] for i in range(0, len(data)) }
    data = json_read(doc_url)
    with open(current_doc, 'w') as file:
        data.append(dictionary)
        print(data)
        json.dump(data, file, indent=4)