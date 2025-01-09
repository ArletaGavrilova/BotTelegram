from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()

        self.hp = 100
        self.power = 10

        Pokemon.pokemons[pokemon_trainer] = self

    def attack(self, enemy):
        #Отнять от hp врага значение нашего power
        enemy.hp = enemy.hp - self.power
        if enemy.hp > 0:
            return f"Здоровье врага: {enemy.hp}"
        else:
            return "Враг проиграл"
    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
        else:
            return "Pikachu" 
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/1/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покемона: {self.name}, сила: {self.power}, хп:{self.hp}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

class Fighter(Pokemon):
    def attack(self, enemy):
        self.power += 5
        result = super().attack(enemy)
        self.power -= 5
        return result

if __name__ == '__main__':
    pokemon1 = Pokemon("")
    pokemon2 = Pokemon("")
    print(pokemon1.attack(pokemon2))
    print(pokemon1.attack(pokemon2))
    print(pokemon1.attack(pokemon2))

    print("pokemon1:", pokemon1.hp)
    print("pokemon2:", pokemon2.hp)