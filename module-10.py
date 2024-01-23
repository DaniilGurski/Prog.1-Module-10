# 1. Skapa en egen klass som innehåller ett bilmärke och modell.
# 2. Skapa en klass och initiera eget bilmärke och modell.
# 3. Skapa en klass med flera bilar.
# 4. Gör så man kan lägga till hur många bilar som helst.
# 5. Gör så man kan ta bort bilar.

# Programmet är anpassad till de två sista frågorna.
import colorama

from os import system
from colorama import Fore
colorama.init(autoreset = True)

class CarList: 
    def __init__(self):
        self.cars = []


    def show_cars(self): 
        for n, carObject in enumerate(self.cars):
            carMake = carObject["make"]
            carModel = carObject["model"]

            print(f"{n + 1}. Make - {carMake}, Model - {carModel}")


    def add_car(self, make, model): 
        self.cars.append({"make": make, "model": model})
        self.show_cars()


    def remove_car(self, index):
        system("cls")
        try: 
            del self.cars[int(index) - 1]
            print(f"{Fore.LIGHTGREEN_EX}Car removed successfully.")
        except: 
            print(f"{Fore.LIGHTRED_EX}No such car found.")


system("cls")
car_list = CarList()


while True: 
    user = input(f"\nEnter cars {Fore.LIGHTBLUE_EX}make{Fore.RESET} and {Fore.LIGHTBLUE_EX}model{Fore.RESET}:")

    if (user.isdigit()): 
        car_list.remove_car(user)
        continue

    data = user.split(" ")[:2]

    if (len(data) <= 1):
        system("cls")
        print(f"{Fore.LIGHTRED_EX}Not all car information is filled in.")
        continue
    
    system("cls")
    make, model = data
    car_list.add_car(make, model)





            

    



