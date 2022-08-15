import json
import cryptocode

x = {
    'SET_download' : False,
    'mai_download' : True,
    'load_screen_x' : 1925,
    'load_screen_y' : 0,
    'start_screen_x' : 1925,
    'start_screen_y' : 0,
    'analyse_screen_x' : 1925,
    'analyse_screen_y' : 0,
    'BNB_API': '',
    'BNB_Secret_key': '',
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