from src.game.base_name_and_image import BaseClassForNameAndImage


class Hero(BaseClassForNameAndImage):
    """
    This interface contains all data needed by the client about the hero
    """
    WIZARD_MAX_LIFE = 6
    WIZARD_MAX_ATTACK_LEVEL = 15
    WARRIOR_MAX_LIFE = 10
    WARRIOR_MAX_ATTACK_LEVEL = 10

    def __init__(self, hero_type, name, image, life, attack_level):
        self.hero_type = hero_type
        super().__init__(name, image)
        self.life = life
        self.attack_level = attack_level

    @classmethod
    def get_hero_list(cls):
        return [Hero('Wizard', 'Merlin', 'imageUrl', 3, 8),
                Hero('Wizard', 'Gandalf', 'imageUrl', 3, 8),
                Hero('Warrior', 'Conan', 'imageUrl', 5, 5)]

    def set_life(self, mod):
        if self.hero_type == 'Wizard':
            if self.life + mod < self.WIZARD_MAX_LIFE:
                self.life += mod
            else:
                self.life = self.WIZARD_MAX_LIFE

        if self.hero_type == 'Warrior':
            if self.life + mod < self.WARRIOR_MAX_LIFE:
                self.life += mod
            else:
                self.life = self.WARRIOR_MAX_LIFE

    def set_attack_level(self, mod):
        if self.hero_type == 'Wizard':
            if self.attack_level + mod < self.WIZARD_MAX_ATTACK_LEVEL:
                self.attack_level += mod
            else:
                self.attack_level = self.WIZARD_MAX_ATTACK_LEVEL

        if self.hero_type == 'Warrior':
            if self.attack_level + mod < self.WARRIOR_MAX_ATTACK_LEVEL:
                self.attack_level += mod
            else:
                self.attack_level = self.WARRIOR_MAX_ATTACK_LEVEL
