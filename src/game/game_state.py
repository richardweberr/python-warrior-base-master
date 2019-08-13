from .game_status import GAME_STATUS
from random import randrange


class GameState(object):
    """
    This interface describes the game state which should be return after each game turn
    """

    def __init__(self, player_name, hero, game_map, ):
        self.player_name = player_name
        self.hero = hero
        self.game_map = game_map
        self.log = []
        self.current_case = 0
        self.nextTurn = True
        self.game_status = GAME_STATUS[0]
        self.game_id = 1

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
        # if self.log['final_position'] != 0:
        #     self.last_log = '\n' + \
        #                     'Vous partez de la case ' + str(self.log['start_position']) + \
        #                     ', vous lancez un dé de ' + str(self.log['roll_dice']) + \
        #                     ', vous arrivez sur la case ' + str(self.log['final_position']) + \
        #                     '. Vous tombez sur : ' + self.game_map.get_name_of_case_content(self.log['final_position']) + \
        #                     '\n' + \
        #                     ' | '.join(
        #                         map(str, self.game_map.build_path_to_display(self.hero, self.log['start_position'],
        #                                                                      self.log['final_position']))) + \
        #                     '\n'
        return self.log

    def next_turn(self):
        """
        Called by the client to execute a new turn in the game.

        Returns:
            bool: True if the move can be execute, False if move is impossible
        """
        # self.log['start_position'] = self.current_case
        # self.log['roll_dice'] = randrange(1, 7)
        # self.current_case += self.log['roll_dice']
        #
        # if self.current_case > self.game_map.number_of_case:
        #     self.log['final_position'] = 'Arrivée'
        #     self.nextTurn = False
        #     self.game_status = GAME_STATUS[2]
        #     print('status: ' + self.game_status)
        # else:
        #     self.log['final_position'] = self.current_case
        #     self.nextTurn = True
        #
        # return self.nextTurn
        self.log = []
        start_position = self.current_case
        self.log.append('Vous êtes sur la case ' + str(self.current_case))
        roll_dice = randrange(1, 7)
        self.log.append('Vous lancez un dé de ' + str(roll_dice))
        self.current_case += roll_dice
        if self.current_case > self.game_map.number_of_case:
            self.log.append('Vous avez GAGNE')
            self.nextTurn = False
            self.game_status = GAME_STATUS[2]
        else:
            self.log.append('Vous arrivez sur la case ' + str(self.current_case))
            self.log.append(' | '.join(map(str, self.game_map.build_path_to_display(self.hero, start_position, self.current_case))))
            self.nextTurn = True

        return self.nextTurn
