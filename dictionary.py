# unordered collection of key-value pairs (but python updated that with 3.6 and now the order matters)
# no indexes, only keys

# can create empty dict with {}
# {'key': value} is a "dictionary literal"

me = {
    "first": "Karis",
    "last": "Courey",
    "occ": "badass",
}

karl = {
    "occ": "cool dude",
    "first": "Karl",
    "last": "Preisner",
}

print(me["first"])
print(karl["first"])

print(me.get("first"))

# .get() for key that doesn't exist returns None ... won't crash, so a lil safer
print(me.get('firstname'))
# dict['key'] for key that doesn't exist raises a KeyError
# print(me['firstname'])

# Gives list of all keys in dict
print(me.keys())

# Gives list of all values
print(me.values())

# Can loop through a list with for
# By default, this gives keys
for key in me:
    print(key)

# This is like enumerate but for dicts, gives keys and values
print(me.items())

# BOTH KEY AND VALUE can unpack key and value with .items()
for k, v in me.items():
    print(k,v)
