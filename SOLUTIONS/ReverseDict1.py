from collections import OrderedDict
dict = {'Delhi': 93, 'Gwalior': 355, 'Goa': 213, 'Jaipur': 376, 'Udaipur': 244,'lucknow':312}

new_dict = OrderedDict(dict.items())
for key in new_dict:
    print (key, new_dict[key])

print("\nIn reverse order:")
for key in reversed(new_dict):
    print (key, new_dict[key])
