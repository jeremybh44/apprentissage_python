import re
import string
from pathlib import Path
from typing import List
import random

from tinydb import TinyDB, where


class User:
    DB = TinyDB(Path(__file__).resolve().parent / 'db.json', indent=4)

    def __init__(self, first_name: str, last_name: str, phone_number: str = "", address: str = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        # self.full_name = f"{self.first_name} {self.last_name}" # cet attribut ne contiendra les informations qu'au moment de l'init

    def __str__(self):
        return f"{self.full_name}\n{self.phone_number}\n{self.address}"

    def __repr__(self):
        return f"User({self.first_name}, {self.last_name})"

    @property # permet d'avoir acces à la valeur d'un attribut de manière dynamique
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def db_instance(self):
        return User.DB.get((where('first_name') == self.first_name) & (where('last_name') == self.last_name))

    def _checks(self):
        self._check_phone_number()
        self._check_names()

    def _check_phone_number(self):
        phone_digits = re.sub(r"[+()\s]*", "", self.phone_number)
        print(phone_digits)
        if len(phone_digits) < 10 or not phone_digits.isdigit():
            raise ValueError(f"Numéro de téléphone {self.phone_number} invalide.")

    def _check_names(self):
        if not (self.first_name and self.last_name):
            raise ValueError(f"Le prénom et le nom de famille ne peuvent pas être vides.")

        special_characters = string.punctuation + string.digits

        for character in self.first_name + self.last_name:
            if character in special_characters:
                raise ValueError(f"Nom invalide {self.full_name}.")

    def exists(self):
        return bool(self.db_instance)

    def delete(self) -> List[int]:
        if self.exists():
            return User.DB.remove(doc_ids=[self.db_instance.doc_id])

        return []

    def save(self, validate_data: bool = False) -> int:
        if validate_data:
            self._checks()

        return User.DB.insert(self.__dict__)

def get_all_users():
    return [User(**user) for user in User.DB.all()]

if __name__ == "__main__":
    from faker import Faker

    fake = Faker(locale="fr_FR")

    for _ in range(10):
        user = User(first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    phone_number=fake.phone_number(),
                    address=fake.address())
        user.save()

    print(get_all_users())
    print(False + True)
    liste = [1, 2]
    liste.extend(3, 4)
    print(liste)


