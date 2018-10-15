# using the orderedDict lib
from collections import OrderedDict
dict = {'Abuja': 93, 'Abia': 355, 'Akwaibom': 213, 'Anambara': 376, 'Alaska': 244}
new_dict = OrderedDict(dict.items())

print("\nIn normal order:")
for key in new_dict:
    print (key, new_dict[key])

print("\nIn reverse order:")
for key in reversed(new_dict):
    print (key, new_dict[key])