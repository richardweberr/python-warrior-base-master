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
        return Hero.get_hero_list()

    def get_maps(self):
        """
        Called by the client to retrieve the list of available maps.
        Returns
            list: the list of available maps
        """
        return Map.get_map_list()

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
