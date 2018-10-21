from collections import defaultdict
import string

# You're running a pool of servers where the servers are numbered sequentially starting from 1. Over time, any given server might explode, in which case its server number is made available for reuse. When a new server is launched, it should be given the lowest available number.

# Write a function which, given the list of currently allocated server numbers, returns the number of the next server to allocate. In addition, you should demonstrate your approach to testing that your function is correct. You may choose to use an existing testing library for your language if you choose, or you may write your own process if you prefer.

# For example, your function should behave something like the following:

#   >> next_server_number([5, 3, 1])
#   2
#   >> next_server_number([5, 4, 1, 2])
#   3
#   >> next_server_number([3, 2, 1])
#   4
#   >> next_server_number([2, 3])
#   1
#   >> next_server_number([])
#   1

def next_server_number(current_numbers):
    '''function to allocate new server numbers'''
    if not current_numbers:
        return 1
    else:
        highest_number = max(current_numbers)
        for num in range(1,highest_number):
            if num not in current_numbers:
                return num
        return highest_number + 1

# print(next_server_number([5,3,1]))
# print(next_server_number([5,4,1,2]))
# print(next_server_number([3,2,1]))
# print(next_server_number([2,3]))
# print(next_server_number([]))



# Server names consist of an alphabetic host type (e.g. "apibox") concatenated with the server number, with server numbers allocated as before (so "apibox1", "apibox2", etc. are valid hostnames).

# Write a name tracking class with two operations, allocate(host_type) and deallocate(hostname). The former should reserve and return the next available hostname, while the latter should release that hostname back into the pool.

# For example:

# >> tracker = Tracker()
# >> tracker.allocate("apibox")
# "apibox1"
# >> tracker.allocate("apibox")
# "apibox2"
# >> tracker.deallocate("apibox1")
# nil
# >> tracker.allocate("apibox")
# "apibox1"
# >> tracker.allocate("sitebox")
# "sitebox1

class Tracker:
    def __init__(self):
        self.host_types = defaultdict(list)
    
    def allocate(self, host_type):
        '''function to allocate new server numbers'''
        available = self.next_server_number(self.host_types[host_type])
        # print(self.host_types)
        self.host_types[host_type].append(available)
        return '{}{}'.format(host_type, available)
    
    def deallocate(self, hostname):
        '''function to deallocate the inputted server'''
        last_letter = 0
        for (i,char) in enumerate(hostname):
            if char in string.ascii_letters:
                last_letter = i
        
        host_num = hostname[last_letter+1:]
        host_type = hostname[:last_letter+1]

        # print(host_num)
        # print(self.host_types)
        self.host_types[host_type].remove(int(host_num))
        return None
    
    def next_server_number(self, current_numbers):
        '''function to detect lowest available server number'''
        if not current_numbers:
            return 1
        else:
            highest_number = max(current_numbers)
            for num in range(1,highest_number):
                if num not in current_numbers:
                    return num
            return highest_number + 1


tracker = Tracker()
print(tracker.allocate("apibox"))
print(tracker.allocate("apibox"))
print(tracker.deallocate("apibox1"))
print(tracker.allocate("apibox"))
print(tracker.allocate("sitebox"))

