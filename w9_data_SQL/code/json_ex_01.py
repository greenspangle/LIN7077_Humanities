# Object serialization converts a complex python object structure to into a
# linear JSON formatted string. Deserialization does the reverse.

# import the JSON module to serialize/deserialize python objects to JSON
import json

# create a dictionary containing some sample data
data = dict(president={
    "name": "Zaphod Beeblebrox",
    "species": "Betelgeusian"
})

# SERIALIZATION

# write the dictionary to the json file 'data_file.json'
with open(r'..\data\data_file.json', 'w') as write_file:
    json.dump(data, write_file)

# write the dictionary to a JSON string and display it in the console
json_string = json.dumps(data)
print(json_string)


# DESERIALIZATION

# read the JSON file 'data_file.json' and recreate the python object
with open(r"..\data\data_file.json", "r") as read_file:
    data_reconstituted = json.load(read_file)

assert data == data_reconstituted  # hopefully this is True and nothing happens!

# if we have a json structure in a string we can deserialize that
# with json.loads() method
json_string = """
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
# deserialize json_string and print to console
new_data = json.loads(json_string)
print(new_data)