import random

def get_player_profile(pokemon_list):
    player_profile = {
        "player_name": input("Escriba el nombre que se mostrara en pantalla"),
        "pokemon_inventory": [random.choice(pokemon_list) for a in range(3)],
        "combats": 0,
        "pokeballs": 0,
        "health_potion": 0,
    }
    print(player_profile)

def main():
    pokemon_list = ['Pikachu', 'Charmander', 'Squirtle']
    get_player_profile(pokemon_list)

if __name__ == "__name__":
    main()