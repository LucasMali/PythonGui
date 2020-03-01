# https://stackabuse.com/saving-text-json-and-csv-to-a-file-in-python/
# https://www.programiz.com/python-programming/variables-constants-literals
# https://pythonbasics.org/read-json-file/
# https://www.w3schools.com/python/python_try_except.asp
import json
import settings


def save(url):
    try:
        with open(settings.STORGE, 'r+') as json_file:
            data = json_file.read()
    except IOError as e:
        print("File doesn't exists, we'll create it.")

    try:
        data_object = json.loads(data)
        data_object.append(url)
    except:
        data_object = [url]

    with open(settings.STORGE, 'w+') as json_file:
        json.dump(data_object, json_file)


save(
    {
        'url': 'http://test2/com',
        'name': 'test2'
    }
)
