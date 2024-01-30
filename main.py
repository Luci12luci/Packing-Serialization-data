# import pickle
#
# class Student():
#     def __init__(self, name, age, country):
#        self.name = name
#        self.age = age
#        self.country = country
#
#     def __str__(self):
#         return f"Student sa vola {self.name} z krajiny {self.country} a ma {self.age} rokov"
#
#     def vloz_do_suboru(self, nazov_suboru):
#         with open(nazov_suboru, "wb") as file:
#             pickle.dump(self, file)
#
#     @staticmethod
#     def vytvor_zo_suboru(nazov_suboru):
#         with open(nazov_suboru, "rb") as file:
#             return pickle.load(file)
#
# patrik_zo_suboru = Student.vytvor_zo_suboru("patrik.dat")
# print(patrik_zo_suboru)
#
# patrik = Student("Patrik", 30, "Slovakia")
# patrik.vloz_do_suboru("patrik.dat")

# print(patrik)
# serialized = pickle.dumps(patrik)
#
# patrik_obnoveny = pickle.loads(serialized)
# print(patrik_obnoveny)

import json

class Student():
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
        self.studentov_kamos = None

    def __str__(self):
            return f"Sttudent sa vola {self.name} z krajiny {self.country} a ma {self.age} rokov."

    def to_json(self):
            return json.dumps(self, default=lambda obj: obj.__dict__)

    def uloz_do_suboru(self, nazov):
            with open(nazov, "w") as file:
                file.write(self.to_json())

patrik = Student("Patrik", 30, "Slovakia")
milan = Student("Milan", 29, "Czech Republic")
patrik.studentov_kamos = milan
patrik.uloz_do_suboru("patrik.json")
