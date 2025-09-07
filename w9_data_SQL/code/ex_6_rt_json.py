# example_5 - writing and reading JSON files

import json


# first create some data
py_data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}


json_str = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""


# dump python object to a json file
filename = "ex_6_data.json"
with open(filename+'1',
          "w") as f:
    json.dump(py_data, f, indent=4)

# convert JSON string to a python object then dump() to JSON file
py_obj = json.loads(json_str)
with open(filename+'2',
          "a") as f:
    json.dump(py_obj, f, indent=4)
