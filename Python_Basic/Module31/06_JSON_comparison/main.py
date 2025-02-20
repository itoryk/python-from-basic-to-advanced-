import json
from typing import List, Dict

with open('json_new.json', 'r') as new_file:
    new_data = json.load(new_file)

with open('json_old.json', 'r') as old_file:
    old_data = json.load(old_file)


def dict_lookup(dict_1: Dict, dict_2: Dict, diff: List) -> Dict:
    for key, val in dict_1.items():
        if isinstance(dict_1[key], dict):
            dict_lookup(dict_1[key], dict_2[key], diff)
        elif dict_1[key] != dict_2[key] and key in diff:
            dict_of_values[key] = dict_1[key]
    return dict_of_values


dict_of_values: Dict = {}
diff_list: List[str] = ["services", "staff", "datetime"]
result: Dict = dict_lookup(new_data, old_data, diff_list)
print(result)

with open('result.json', 'w', encoding='utf8') as final:
    json.dump(result, final, indent=4, ensure_ascii=False)