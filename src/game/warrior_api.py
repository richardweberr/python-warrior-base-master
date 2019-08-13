from src.game.modifier import Modifier
from .game_map import Map
from .hero import Hero
from .game_state import GameState


class WarriorsAPI(object):
    """the Warriors Game API"""

    def get_heroes(self):
        """
        Called by the client to retrieve the list of available heroes.

        Returns
            list: the list of available heroes

        """
        return [Hero('Wizard', 'Merlin', 'imageUrl', 3, 8),
                Hero('Wizard', 'Gandalf', 'imageUrl', 3, 8),
                Hero('Warrior', 'Conan', 'imageUrl', 5, 5)]

    def get_maps(self):
        """
        Called by the client to retrieve the list of available maps.

        Returns
            list: the list of available maps
        """
        goblins = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
        sorciers = [10, 20, 25, 32, 36, 37, 40, 44, 47]
        dragons = [45, 52, 56, 62]
        arcs = [2, 11, 14, 19, 26]
        massues = [5, 22, 38]
        epees = [42, 53]
        eclairs = [1, 4, 8, 17, 23]
        boules_de_feu = [48, 49]
        potions_mineures = [7, 13, 28, 29, 33]
        potions_standards = [31, 39, 43]
        potions_grandes = [41]

        cases = {}
        for goblin in goblins:
            cases[goblin] = Hero('monster', 'Goblin', 'imageUrl', life=6, attack_level=1)
        for sorcier in sorciers:
            cases[sorcier] = Hero('monster', 'Sorcier', 'imageUrl', life=9, attack_level=2)
        for dragon in dragons:
            cases[dragon] = Hero('monster', 'Dragon', 'imageUrl', life=15, attack_level=4)
        for arc in arcs:
            cases[arc] = Modifier(mod_type='weapon', name='Arc', mod_attack_level=1)
        for massue in massues:
            cases[massue] = Modifier(mod_type='weapon', name='Massue', mod_attack_level=3)
        for epee in epees:
            cases[epee] = Modifier(mod_type='weapon', name='Epée', mod_attack_level=5)
        for eclair in eclairs:
            cases[eclair] = Modifier(mod_type='spell', name='Eclair', mod_attack_level=2)
        for boule_de_feu in boules_de_feu:
            cases[boule_de_feu] = Modifier(mod_type='spell', name='Boule de Feu', mod_attack_level=7)
        for potion_mineure in potions_mineures:
            cases[potion_mineure] = Modifier(mod_type='potion', name='Potion Mineure', mod_life=1)
        for potion_standard in potions_standards:
            cases[potion_standard] = Modifier(mod_type='potion', name='Potion Standard', mod_life=2)
        for potion_grande in potions_grandes:
            cases[potion_grande] = Modifier(mod_type='potion', name='Grande Potion', mod_life=5)

        # for case in cases:
        #     print(case, ': ', cases[case].name)

        return [Map('Maxiland', 64, cases),
                Map('Miniland', 16)]

    def create_game(self, player_name, hero, game_map):
        """Called by the client to create a new game

        Args:
            player_name (str): the name of the player
            hero (Hero): the chosen hero for the game
            game_map (Map): the chosen map for the game

        Returns
            GameState: the initial game state
        """
        return GameState(player_name, hero, game_map)
