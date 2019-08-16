import pytest

from src.game.exceptions import ModifierTypeNotAllowedException
from src.game.modifier import Modifier


def test_modifier_current_type_is_in_valid_list():
    with pytest.raises(ModifierTypeNotAllowedException):
        Modifier(current_type='toto', name='poison')
