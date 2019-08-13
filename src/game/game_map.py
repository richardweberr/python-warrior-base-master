from src.game.base_name_and_image import BaseClassForNameAndImage
from src.game.hero import Hero
from src.game.modifier import Modifier


class Map(BaseClassForNameAndImage):
    """
    This interface contains all data needed by the client about the game map
    """
    def __init__(self, name, image, number_of_case, cases=None):
        """
        Args:
            name: name of the map
            number_of_case: size of map
            cases: Dictionary of {index: case content}
        """
        super().__init__(name, image)
        self.number_of_case = number_of_case
        self.cases = cases

    @classmethod
    def get_map_list(cls):
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
        return [Map('Maxiland', 'imageURL', 64, cases),
                Map('Miniland', 'imageURL', 16)]

    def get_name_of_case_content(self, case):
        """
        Returns
            str: content_name of case
        """
        if case in self.cases:
            return self.cases[case].name
        else:
            return ' '

    def build_path_to_display(self, hero, start_position, final_position):
        """
        Args:
            hero (Hero): the chosen hero for the game
            start_position: case index of hero before
            final_position: case index of hero after dice roll
        Returns
            path: Dictionary of cases starting with start_position and of length PATH_LENGTH
        """
        PATH_LENGTH = 12

        path = [start_position]
        for i in range(1, PATH_LENGTH):
            if start_position + i <= self.number_of_case:
                if start_position + i == final_position:
                    path.append(hero.name)
                else:
                    path.append(
                        str(start_position + i) + ' ' + self.get_name_of_case_content(start_position + i))
            else:
                path.append('Arrivée')
                break

        return path
