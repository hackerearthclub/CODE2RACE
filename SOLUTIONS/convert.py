n = input()
sec, rest = n[:-2].split(":") , n[-2:]
if rest == "PM" and sec[0] != "12":
    sec[0] = str(int(sec[0]) + 12)
elif rest == "AM" and sec[0] == "12":
    sec[0] = str(int(sec[0]) - 12)

print(":".join(sec))
