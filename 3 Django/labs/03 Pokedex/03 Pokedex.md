

# Pokedex

Let's build a searchable pokedex! First we'll load the data from a `json` file into our own database. Then we'll list those pokemon in the page and add search.

> The Pokédex (Japanese: ポケモン図鑑 illustrated Pokémon encyclopedia) is a digital encyclopedia for [Trainers](https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Trainer) in the Pokémon world. It gives information about all Pokémon in the world that are contained in its database. 
>
>Pokédex entries typically describe a Pokémon in only two or three sentences. They may give background information on the habitat or activities of a Pokémon in the wild or other information on the Pokémon's history or anatomy. 
>
>Pokédex entries also include height, weight, cry, footprint, location, other forms, and a picture of the Pokémon.

[Pokedex Wiki](https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9dex), [Pokemon.com](https://www.pokemon.com/us/pokedex/)

## Part 1

Create an app `pokedex` and add two models to store our pokemon, `Pokemon` and `PokemonType`.

`PokemonType` should have the following fields:
- `name` (CharField)

`Pokemon` should have the following fields:
- `number` (IntegerField)
- `name` (CharField)
- `height` (FloatField)
- `weight` (FloatField)
- `image_front` (CharField)
- `image_back` (CharField)
- `types` (ManyToManyField with `PokemonType`)

## Part 2

Write a [custom management command](../docs/01%20Django%20Overview.md#custom-management-commands) `load_pokemon.py` to load the data from [pokemon.json](./pokemon.json) into your database. You can do this by saving the file next to your `.py` file and using [opening the file](../../1%20Python/10%20Dictionaries/13%20File%20IO.md). To handle the types, check out [many to many fields](../docs/06%20Models.md#many-to-many). In the first line of your management command, you may want to delete all the records in the table so each time you run it you start with a clean slate. To verify that the data was loaded, open your admin panel and check that the pokemon are there.

## Part 3

Write a `view`, `route` and `template` to show a list of pokemon on the front page. You can either show all the information as a table, or show only their name and icon and link to a detail page with all their information. Use `<img src="...">` to display their front and back image. Create a search bar to filter by `name` and `type`.

## Part 4 (optional)

Check out the [script](./load_pokemon.py) that creates the json file, you can use it to load even more pokemon into your database!

