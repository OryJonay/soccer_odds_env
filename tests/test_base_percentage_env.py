import pytest
import numpy
from gym.spaces import Box


def test_attributes(basic_percentge_env):
    assert basic_percentge_env.action_space == Box(low=numpy.array([0.] * 3),
                                                   high=numpy.array([2 ** 2 - 0.01] + [1.] * 2))
    assert basic_percentge_env.observation_space == Box(low=1., high=float('Inf'), shape=(1, 2))
    assert basic_percentge_env.STARTING_BANK == 10
    assert basic_percentge_env.balance == basic_percentge_env.STARTING_BANK
    assert basic_percentge_env.current_step == 0
    assert basic_percentge_env.bet_size_matrix is None


@pytest.mark.parametrize("action,expected_reward", [((0, 0.25, 0.25), 0), ((1, 0.25, 0.25), 2.5),
                                                          ((2, 0.25, 0.25), -2.5), ((3, 0.25, 0.25), 0)])
def test_step(basic_percentge_env, action, expected_reward):
    odds, reward, done, _ = basic_percentge_env.step(action)
    assert reward == expected_reward
    assert done
    assert basic_percentge_env.current_step == 0
