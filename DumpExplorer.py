import os
import bz2
import json

base_path = '/media/mega_disco/data_wiki_cache/'

line_count = 0
with bz2.open('/media/mega_disco/latest-all.json.bz2', 'rb') as f:
    for line in f:
        decoded_line = line.decode("UTF-8")
        if decoded_line.startswith("["):
            continue
        if decoded_line.startswith("]"):
            continue
        if decoded_line.endswith("]"):
            continue
        try:
            json_line = json.loads(decoded_line[:-2])
        except:
            print("ERROR")
            print(decoded_line[:-2])
            continue
        json_path = base_path
        for char in json_line["id"][:-1]:
            json_path = os.path.join(json_path, char)
        json_file_path = os.path.join(json_path, "{}.json".format(json_line["id"]))
        os.makedirs(json_path, exist_ok=True)
        if line_count % 100000 == 0:
            print(line_count)
            print(json_file_path)
        with open(json_file_path, 'w') as data_file:
            json.dump(json_line, data_file)
        line_count += 1

print(line_count)
print("FIN")
