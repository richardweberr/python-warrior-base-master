from src.game.game_map import Map
from src.game.hero import Hero


def test_map_get_name():
    game_map = Map(name="Choco Island", number_of_case=64)
    assert game_map.name == "Choco Island"


def test_map_get_number_of_case():
    game_map = Map(name="Choco Island", number_of_case=64)
    assert game_map.number_of_case == 64


def test_case_in_map_has_a_name1():
    game_map = Map(name="Choco Island", number_of_case=64)
    assert game_map.get_name_of_case_content(range(1, game_map.number_of_case)) == ' '


def test_case_in_map_has_a_name2():
    cases = {}
    cases[23] = Hero(current_type='monster', name='Name', image='Image', life=5, attack_level=5)
    game_map = Map(name="Choco Island", number_of_case=64, cases=cases)
    assert game_map.get_name_of_case_content(23) == 'Name'
