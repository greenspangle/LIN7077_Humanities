# Practice serializing and deserializing JSON

# import the JSON module to serialize/deserialize python objects to JSON
import json

# create some sample data
an_int = 5
a_float = 5.0
a_str = 'abracadabra'
a_tuple = (1, 2, 3, 4, 5)
a_list = list('abracadabra')
a_set = set('abracadabra')  # sets are NOT json serializable!
a_dict = dict([
    ('an_int', an_int),
    ('a_float', a_float),
    ('a_str', a_str),
#    ('a_tuple', a_tuple),
    ('a_list', a_list),
#    ('a_set', a_set)  # a set can be in a dictionary but that would mean it was unserializable
])

# print(an_int, a_float, a_str, a_tuple, a_list, a_set, a_dict)

print(an_int)
print(a_float)
print(a_str)
print(a_tuple)
print(a_list)
print(a_set)
print(a_dict)

# Dump all that data to a json string
data_json = json.dumps(a_dict, indent=4)
print('The dictionary containing the data:\n',data_json)
# and now pull it back into python objects
data_py =json.loads(data_json)
print('The reconstituted object is:\n',data_py)

# and test that the dictionary (and hence the objects within it) are preserved
assert a_dict==data_py
