# example_5 - writing and reading JSON strings

import json

# first create sone data
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


# dump python object to a string using the dumps() method
j_str = json.dumps(py_data)
print('JSON string is:\n', j_str,'\n')

# read python object from a JSON string using the loads() method
py_obj_1= json.loads(j_str)
print('python object is:\n', py_obj_1,'\n')

# and another JSON string
py_obj_2= json.loads(json_str)
print('and another pyton object from JSON is:\n', py_obj_2)

