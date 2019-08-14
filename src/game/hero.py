from src.game.base_name_and_image import BaseClassForNameAndImage


class Hero(BaseClassForNameAndImage):
    """
    This interface contains all data needed by the client about the hero
    """
    WIZARD_MAX_LIFE = 6
    WIZARD_MAX_ATTACK_LEVEL = 15
    WARRIOR_MAX_LIFE = 10
    WARRIOR_MAX_ATTACK_LEVEL = 10

    def __init__(self, current_type, name, image, life, attack_level):
        self.current_type = current_type
        super().__init__(name, image)
        # prefix life with _ to make the attribute 'private'
        self._life = life
        self._attack_level = attack_level

    # current_type = ('Warrior', 'Wizard', 'monster')

    @classmethod
    def get_hero_list(cls):
        return [cls('Wizard', 'Merlin', 'imageUrl', 3, 8),
                cls('Wizard', 'Gandalf', 'imageUrl', 3, 8),
                cls('Warrior', 'Conan', 'imageUrl', 5, 5)]

    # need to define the getter to be able to add the setter
    @property
    def life(self):
        return self._life

    # setter defined here
    @life.setter
    def life(self, new_value):
        if self.current_type == 'Wizard':
            if new_value >= self.WIZARD_MAX_LIFE:
                self._life = self.WIZARD_MAX_LIFE
            else:
                self._life = new_value

        if self.current_type == 'Warrior':
            if new_value >= self.WARRIOR_MAX_LIFE:
                self._life = self.WARRIOR_MAX_LIFE
            else:
                self._life = new_value

    @property
    def attack_level(self):
        return self._attack_level

    @attack_level.setter
    def attack_level(self, new_value):
        if self.current_type == 'Wizard':
            if new_value >= self.WIZARD_MAX_ATTACK_LEVEL:
                self._attack_level = self.WIZARD_MAX_ATTACK_LEVEL
            else:
                self._attack_level = new_value

        if self.current_type == 'Warrior':
            if new_value >= self.WARRIOR_MAX_ATTACK_LEVEL:
                self._attack_level = self.WARRIOR_MAX_ATTACK_LEVEL
            else:
                self._attack_level = new_value

    def use_modifier(self, case):
        if case.current_type == 'potion':
            # call to setter here
            self.life += case.mod_life
        if case.current_type == 'weapon' and self.current_type == 'Warrior':
            self.attack_level += case.mod_attack_level
        if case.current_type == 'spell' and self.current_type == 'Wizard':
            self.attack_level += case.mod_attack_level

    def combat_monster(self, case):
        print('combat')

