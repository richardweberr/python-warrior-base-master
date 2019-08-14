from src.game.base_name_and_image import BaseClassForNameAndImage


class Modifier(BaseClassForNameAndImage):
    def __init__(self, current_type, name, image=None, mod_life=None, mod_attack_level=None):
        self.current_type = current_type
        super().__init__(name, image)
        self.mod_life = mod_life
        self.mod_attack_level = mod_attack_level

    # current_type = ('weapon', 'spell', 'potion')
