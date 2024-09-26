# Nomeclatura Slicing = [start:stop:step]

name = "Bro Code"
first_name = name[:3]  # [0:3]
last_name = name[4:]  # [7:len(name)]
reversed_name = name[::-1]
funky_name = name[::2]  # [0:len(name):3]


print(first_name)
print(last_name)
print(reversed_name)
print(funky_name)

# Slice function

website = "http://google.com"
website1 = "http://youtube.com"
website2 = "http://wikipedia.org"

slice = slice(7, -4, 1)

print(website[slice])
print(website1[slice])
print(website2[slice])
