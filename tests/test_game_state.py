from src.game.game_map import Map
from src.game.game_state import GameState
from src.game.hero import Hero


def test_current_case_increments_on_dice_roll(monkeypatch):
    wizard = Hero(current_type='Wizard', name='toto', image='image', life=3, attack_level=8)
    game_map = Map(name='Maxiland', image='imageURL', number_of_case=64)
    game_state = GameState(player_name='toto', hero=wizard, game_map=game_map)

    def mock_roll_dice(self):
        return 1

    monkeypatch.setattr(GameState, 'roll_dice', mock_roll_dice)
    game_state.next_turn()
    assert game_state.current_case == 1
