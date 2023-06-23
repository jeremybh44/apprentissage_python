from dataclasses import dataclass

@dataclass
class Car:
    fuel_reserve: int = 100

    def print_fuel_reserve(self):
        print(f"Il vous reste {self.fuel_reserve}L d'essence")

    def drive(self, km):
        if(self.fuel_reserve - km*5 / 100 < 0):
            print("Vous n'avez plus assez d'essence !")
        else:
            self.fuel_reserve = self.fuel_reserve - km*5 / 100
            print(f"Vous avez parcouru {km} km")
            print(f"Il vous reste {self.fuel_reserve}L d'essence")
            if(self.fuel_reserve < 10):
                print("Votre niveau d'essence est critique ⚠")

    def refuel(self):
        self.fuel_reserve = 100
        print("Vous pouvez repartir !")


if __name__ == "__main__":
    voiture = Car()

    voiture.print_fuel_reserve()

    voiture.drive(km=10)

    voiture.print_fuel_reserve()

    voiture.refuel()

    voiture.print_fuel_reserve()

    voiture.drive(km=1900)

    voiture.print_fuel_reserve()
