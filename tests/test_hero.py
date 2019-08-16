import pytest

from src.game.exceptions import HeroTypeNotAllowedException
from src.game.hero import Hero
from src.game.modifier import Modifier


def populate():
    warrior = Hero(current_type='Warrior', name='tata', image='image', life=5, attack_level=5)
    wizard = Hero(current_type='Wizard', name='toto', image='image', life=3, attack_level=8)
    monster = Hero(current_type='monster', name='monster', image='image', life=10, attack_level=1)
    potion = Modifier(current_type='potion', name='potion', mod_life=1)
    weapon = Modifier(current_type='weapon', name='weapon', mod_attack_level=1)
    spell = Modifier(current_type='spell', name='spell', mod_attack_level=2)
    return {'warrior': warrior, 'wizard': wizard, 'monster': monster, 'potion': potion, 'weapon': weapon, 'spell': spell}


def test_warrior_life_cannot_exceed_warrior_max_life_on_instanciation():
    warrior = Hero(current_type='Warrior', name='toto', image='image', life=Hero.WARRIOR_MAX_LIFE + 1, attack_level=5)
    assert warrior.life == warrior.WARRIOR_MAX_LIFE


def test_warrior_life_cannot_exceed_warrior_max_life_on_property_call():
    warrior = Hero(current_type='Warrior', name='toto', image='image', life=Hero.WARRIOR_MAX_LIFE, attack_level=5)
    warrior.life += 1
    assert warrior.life == warrior.WARRIOR_MAX_LIFE


def test_warrior_life_cannot_be_negative_value_on_instantiation():
    warrior = Hero(current_type='Warrior', name='toto', image='image', life=-1, attack_level=5)
    assert warrior.life == 0


def test_warrior_life_cannot_be_negative_value_on_properety_call():
    warrior = Hero(current_type='Warrior', name='toto', image='image', life=0, attack_level=5)
    warrior.life -= 1
    assert warrior.life == 0


def test_wizard_life_cannot_exceed_wizard_max_life_on_instanciation():
    wizard = Hero(current_type='Wizard', name='toto', image='image', life=Hero.WIZARD_MAX_LIFE + 1, attack_level=8)
    assert wizard.life == wizard.WIZARD_MAX_LIFE


def test_wizard_life_cannot_exceed_wizard_max_life_on_property_call():
    wizard = Hero(current_type='Wizard', name='toto', image='image', life=Hero.WIZARD_MAX_LIFE, attack_level=8)
    wizard.life += 1
    assert wizard.life == wizard.WIZARD_MAX_LIFE


def test_wizard_life_cannot_be_negative_value_on_instantiation():
    wizard = Hero(current_type='Wizard', name='toto', image='image', life=-1, attack_level=8)
    assert wizard.life == 0


def test_wizard_life_cannot_be_negative_value_on_properety_call():
    wizard = Hero(current_type='Wizard', name='toto', image='image', life=0, attack_level=8)
    wizard.life -= 1
    assert wizard.life == 0


def test_hero_current_type_is_in_valid_list():
    with pytest.raises(HeroTypeNotAllowedException):
        Hero(current_type='toto', name='titi', image='image', life=0, attack_level=0)


def test_monster_life_cammot_be_negatif():
    monster = Hero(current_type='monster', name='toto', image='image', life=-1, attack_level=0)
    assert monster.life == 0


def test_wizard_cannot_exceed_wizard_max_attack_level():
    wizard = Hero(current_type='Wizard', name='toto', image='image', life=3, attack_level=Hero.WIZARD_MAX_ATTACK_LEVEL)
    wizard.attack_level += 1
    assert wizard.attack_level == Hero.WIZARD_MAX_ATTACK_LEVEL


def test_warrior_cannot_exceed_warrior_max_attack_level():
    warrior = Hero(current_type='Warrior', name='toto', image='image', life=3, attack_level=Hero.WARRIOR_MAX_ATTACK_LEVEL)
    warrior.attack_level += 1
    assert warrior.attack_level == Hero.WARRIOR_MAX_ATTACK_LEVEL


def test_monster_life_getter():
    assert populate()['monster'].life == 10


def test_monster_attack_level_getter():
    assert populate()['monster'].attack_level == 1


def test_warrior_can_use_potion():
    assert populate()['warrior'].can_use_modifier(populate()['potion'])


def test_warrior_can_use_weapon():
    assert populate()['warrior'].can_use_modifier(populate()['weapon'])


def test_wizard_can_use_spell():
    assert populate()['wizard'].can_use_modifier(populate()['spell'])


def test_warrior_cannot_use_spell():
    assert not populate()['warrior'].can_use_modifier(populate()['spell'])


def test_wizard_cannot_use_weapon():
    assert not populate()['wizard'].can_use_modifier(populate()['weapon'])


def test_warrior_gets_potion_life_benefit():
    warrior = populate()['warrior']
    warrior.use_modifier(populate()['potion'])
    assert warrior.life == 6


def test_wizard_gets_spell_attack_level_benefit():
    wizard = populate()['wizard']
    wizard.use_modifier(populate()['spell'])
    assert wizard.attack_level == 10


def test_warrior_gets_weapon_attack_level_benefit():
    warrior = populate()['warrior']
    warrior.use_modifier(populate()['weapon'])
    assert warrior.attack_level == 6


def test_wizard_doesnt_get_weapon_attack_level_benefit():
    wizard = populate()['wizard']
    wizard.use_modifier(populate()['weapon'])
    assert wizard.attack_level == 8


def test_warrior_doesnt_get_spell_attack_level_benefit():
    warrior = populate()['warrior']
    warrior.use_modifier(populate()['spell'])
    assert warrior.attack_level == 5


def test_warrior_can_inflict_damage():
    warrior = populate()['warrior']
    monster = populate()['monster']
    warrior.inflict_damage(monster)
    assert monster.life == 5


def test_warrior_can_take_damage():
    warrior = populate()['warrior']
    monster = populate()['monster']
    warrior.take_damage(monster)
    assert warrior.life == 4


def test_moster_can_counterattack_if_it_survives_assault():
    warrior = populate()['warrior']
    monster = populate()['monster']
    warrior.combat_monster(monster)
    assert warrior.life == 4
