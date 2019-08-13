from src.game.base_name_and_image import BaseClassForNameAndImage


class Modifier(BaseClassForNameAndImage):
    def __init__(self, mod_type, name, image=None, mod_life=None, mod_attack_level=None):
        self.mod_type = mod_type
        super().__init__(name, image)
        self.mod_life = mod_life
        self.mod_attack_level = mod_attack_level
