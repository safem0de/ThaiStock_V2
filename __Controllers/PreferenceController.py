import json
from pprint import pprint
import cryptocode
import ast

class PreferenceController():
    def __init__(self) -> None:
        super().__init__()
        f = open("App_Safem0de.config", "r")
        str_decoded = cryptocode.decrypt(f.read(), 'S@fem0de')
        res = ast.literal_eval(str_decoded)
        str_j = json.dump(res)
        pprint(str_j)
        