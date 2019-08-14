from src.game.hero import Hero


def test_warrior_life_cannot_exceed_warrior_max_life_on_instanciation():
    hero = Hero(current_type='Warrior', name='toto', image='image', life=500, attack_level=5)
    assert hero.life == hero.WARRIOR_MAX_LIFE


def test_warrior_life_cannot_exceed_warrior_max_life_on_property_call():
    hero = Hero(current_type='Warrior', name='toto', image='image', life=10, attack_level=5)
    hero.life += 1
    assert hero.life == hero.WARRIOR_MAX_LIFE
