import requests

def get_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon?limit=100&offset=0"

    all_pokemon = []

    while url:
        response = requests.get(url)
        data = response.json()

        for p in data["results"]:
            pokemon_url = p["url"]
            pokemon_id = int(pokemon_url.rstrip("/").split("/")[-1])

            all_pokemon.append({
                "name" : p["name"],
                "id" : pokemon_id
            })

            url = data["next"]

    return all_pokemon