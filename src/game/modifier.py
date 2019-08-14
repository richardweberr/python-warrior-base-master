from src.game.base_name_and_image import BaseClassForNameAndImage
from src.game.exceptions import ModifierTypeNotAllowedException


class Modifier(BaseClassForNameAndImage):

    ALLOWED_MODIFIER_TYPES = ('weapon', 'spell', 'potion')

    def __init__(self, current_type, name, image=None, mod_life=None, mod_attack_level=None):
        self.current_type = current_type
        if current_type not in self.ALLOWED_MODIFIER_TYPES:
            raise ModifierTypeNotAllowedException()
        super().__init__(name, image)
        self.mod_life = mod_life
        self.mod_attack_level = mod_attack_level


