import random
import requests


BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


POKEMON_LIST = ["pikachu", "charizard", "bulbasaur", "squirtle", "snorlax"]


def fetch_pokemon_data(pokemon_name):
  """Fetches Pokémon data from PokeAPI with error handling."""
  url = f"{BASE_URL}{pokemon_name.lower()}"
  try:
    response = requests.get(url)

   
    if response.status_code == 200:
      return response.json()
    elif response.status_code == 404:
      print(f"Error: Pokémon '{pokemon_name}' not found in the API.")
      return None
    else:
      print(f"Unexpected error: Received status code {response.status_code}")
      return None

  except requests.exceptions.RequestException as e:
    
    print(f"Network error occurred: {e}")
    return None


def play_game():
  print("========================================")
  print("       WELCOME TO WHO'S THAT POKÉMON!   ")
  print("========================================")


  secret_pokemon = random.choice(POKEMON_LIST)


  data = fetch_pokemon_data(secret_pokemon)
  if not data:
    print("Could not retrieve Pokémon data. Exiting game.")
    return

 
  name = data["name"]
  height = data["height"]
  weight = data["weight"]
  
  
  abilities = [item["ability"]["name"] for item in data["abilities"]]

 
  print("\nI have chosen a Pokémon!")
  print(f"📏 Height: {height}")
  print(f"⚖️ Weight: {weight}")
  print(f"✨ Abilities: {', '.join(abilities)}")
  print("\nCan you guess which Pokémon it is?")

  attempts = 3 

  while attempts > 0:
    print(f"\nAttempts remaining: {attempts}")
    guess = input("Your guess: ").strip().lower()

    if guess == name:
      
      print(
          f"\n Correct! You guessed it! The Pokémon was {name.capitalize()}!"
      )
      return
    else:
      attempts -= 1
      if attempts > 0:
        print("Wrong guess! Try again.")
      else:
       
        print(
            "\n You've Ran Out of attempts! Game Over."
            f" The correct Pokémon was: {name.capitalize()}"
        )


if __name__ == "__main__":
  play_game()