import json

def capitalize_bool_str(json_str):
    json_str = json_str.replace("true", "True").replace("false", "False")
    return json_str

def create_new_dictionaries(id_configs, file_path, dname):

    new_dictionaries = {}

    for config_key, config_data in id_configs.items():
        for doc_type, doc_data in config_data.items():
            for side, side_data in doc_data.items():
                new_key = f"{config_key}_{doc_type}_{side}"
                new_dictionaries[new_key] = side_data

    with open(file_path, 'r', encoding='utf-8') as file:
        isAvailable = True
        for line in file:
            if dname in line:
                isAvailable = False

    if isAvailable:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f"\n{dname} = ")
            json_str = json.dumps(new_dictionaries, indent=6)
            json_str = capitalize_bool_str(json_str)
            file.write(json_str)
    else:
        print("Dictionary already exists!")

    return new_dictionaries