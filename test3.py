import json
import cryptocode

x = {
    "SET_download" : False,
    "mai_download" : False,
    "start_screen_x": 1925,
    "start_screen_y" : 10,
}

y = str(x)
print(y)

str_encoded = cryptocode.encrypt(y, 'S@fem0de')
print(str_encoded)

# ## And then to decode it:
str_decoded = cryptocode.decrypt(str_encoded, 'S@fem0de')
print(str_decoded)

f = open("App_Safem0de.config", "w")
f.writelines(str_encoded)