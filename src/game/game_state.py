from .game_status import GAME_STATUS
from random import randrange


class GameState(object):
    """
    This interface describes the game state which should be return after each game turn
    """

    def __init__(self, player_name, hero, game_map, last_log='Commencez la partie', current_case=0):
        self.player_name = player_name
        self.game_id = 1
        self.game_status = GAME_STATUS[0]
        self.hero = hero
        self.game_map = game_map
        self.last_log = last_log
        self.current_case = current_case
        self.nextTurn = True
        self.roll_dice = None

    def get_player_name(self):
        """
        Returns:
            str: The player name
        """
        return self.player_name

    def get_game_id(self):
        """
        Returns:
            int: the game unique ID
        """
        return self.game_id

    def get_game_status(self):
        """
        Returns:
            str: the game status
        """
        return self.game_status

    def get_hero(self):
        """
        Returns:
            Hero: the current hero
        """
        return self.hero

    def get_game_map(self):
        """
        Returns:
            Map: the current map
        """
        return self.game_map

    def get_current_case(self):
        """
        Returns:
            int: the current case index (base 1)
        """
        return self.current_case

    def get_last_log(self):
        """
        Returns:
            str: the last log of the game. This log is displayed by the client after each game turn
        """
        start_position = self.current_case
        self.roll_dice = randrange(1, 7)

        if start_position + self.roll_dice <= self.game_map.number_of_case:
            final_position = self.current_case + self.roll_dice
        else:
            final_position = 'Arrivée'

        self.last_log = '\n' + \
                        'Vous partez de la case ' + str(start_position) + \
                        ', vous lancez un dé de ' + str(self.roll_dice) + \
                        ', vous arrivez sur la case ' + str(final_position) +\
                        '. Vous tombez sur : ' + self.game_map.get_name_of_case_content(final_position) +\
                        '\n' + \
                        ' | '.join(map(str, self.build_path_to_display(start_position, final_position))) + \
                        '\n'

        return self.last_log

    def build_path_to_display(self, start_position, final_position):
        path = [start_position]
        for i in range(1, 12):
            if start_position + i <= self.game_map.number_of_case:
                if start_position + i == final_position:
                    path.append(self.hero.name)
                else:
                    path.append(str(start_position + i) + ' ' + self.game_map.get_name_of_case_content(start_position + i))
            else:
                path.append('Arrivée')
                break
        return path

    def next_turn(self):
        """
        Called by the client to execute a new turn in the game.

        Returns:
            bool: True if the move can be execute, False if move is impossible

        """
        self.current_case += self.roll_dice
        if self.get_current_case() <= self.get_game_map().number_of_case:
            self.nextTurn = True
        else:
            self.nextTurn = False
            self.game_status = GAME_STATUS[2]
            print('status: ' + self.get_game_status())
        return self.nextTurn
