from src.game.hero import Hero
from src.game.modifier import Modifier
from .game_status import GAME_STATUS
from random import randrange


class GameState(object):
    """
    This interface describes the game state which should be return after each game turn
    """

    def __init__(self, player_name, hero, game_map):
        self.player_name = player_name
        self.hero = hero
        self.game_map = game_map
        self.log = ['Commencez la partie']
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

    def get_current_case(self):
        """
        Returns:
            int: the current case index (base 1)
        """
        return self.current_case

    def get_last_log(self):
        return '\n' + '\n'.join(self.log)

    def init_log(self):
        self.log = []

    def next_turn(self):
        """
        Called by the client to execute a new turn in the game.

        Returns:
            bool: True if the move can be execute, False if move is impossible
        """
        # EMPTY LOG EVERY TURN
        self.init_log()
        start_position = self.current_case
        roll_dice = randrange(1, 7)
        self.log.append(f'Vous êtes sur la case {start_position}, vous lancez un dé de {roll_dice}')
        self.current_case += roll_dice
        # TESTS WHETHER GAME IS WON
        if self.current_case > self.game_map.number_of_case:
            self.nextTurn = False
            self.log.append('Vous avez GAGNE')
            print(self.get_last_log())
            self.game_status = GAME_STATUS[2]
        else:
            # GAME CONTINUES
            self.nextTurn = True
            # self.log.append(f'Vous arrivez sur la case {self.current_case}')
            self.log.append(
                ' | '.join(map(str, self.game_map.build_path_to_display(self.hero, start_position, self.current_case))))
            # HERO INTERACTS WITH CASE CONTENT
            if self.game_map.case_not_empty(self.current_case):
                # CASE CONTENT IS (POTION, WEAPON OR SPELL() OF MODIFIER TYPE
                if isinstance(self.game_map.cases[self.current_case], Modifier):
                    self.log.append(f'Vous tombez sur {self.game_map.get_name_of_case_content(self.current_case)}')
                    # self.log.append(f'Votre niveau de vie était {self.hero.life} et '
                    #                 f'votre niveau d\'attaque était {self.hero.attack_level}')
                    if self.hero.can_use_modifier(self.game_map.cases[self.current_case]):
                        self.hero.use_modifier(self.game_map.cases[self.current_case])
                        self.log.append(f'Votre niveau de vie est maintenant {self.hero.life} et '
                                        f'votre niveau d\'attaque est maintenant {self.hero.attack_level}')
                    else:
                        self.log.append(f'Vous ne savez pas utiliser {self.game_map.cases[self.current_case].name}')
                # CASE CONTENT IS (MONSTER) OF HERO TYPE
                if isinstance(self.game_map.cases[self.current_case], Hero):
                    self.log.append(f'Vous tombez sur un {self.game_map.get_name_of_case_content(self.current_case)} '
                                    f'(vie {self.game_map.cases[self.current_case].life}, '
                                    f'attaque {self.game_map.cases[self.current_case].attack_level}), '
                                    f'le combat commence...')
                    self.hero.combat_monster(self.game_map.cases[self.current_case])
                    if self.game_map.cases[self.current_case].life == 0:
                        self.log.append(f'Vous avez tué un {self.game_map.cases[self.current_case].name}')
                    else:
                        self.log.append(f'Il reste {self.game_map.cases[self.current_case].life} '
                                        f'points de vie à votre adversaire. Il vous attaque!')
                        if self.hero.life == 0:
                            self.log.append(f'Vous mourrez')
                            print(self.get_last_log())
                            self.game_status = GAME_STATUS[1]
                            self.nextTurn = False
                        else:
                            self.log.append(f'Il vous reste {self.hero.life} points de vie, votre adversaire s\'enfuit')

        return self.nextTurn
