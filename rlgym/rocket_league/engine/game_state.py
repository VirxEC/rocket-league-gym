"""
    Object to contain all relevant information about the game state.
"""
import numpy as np
from typing import Dict, TypeVar

from rlgym.rocket_league.engine.agent import Agent
from rlgym.rocket_league.engine.physics_object import PhysicsObject

AgentID = TypeVar("AgentID", bound=str)


class GameState:
    blue_score: int
    orange_score: int
    gravity: float
    boost_consumption: float
    agents: Dict[AgentID, Agent]
    ball: PhysicsObject
    inverted_ball: PhysicsObject
    # List of "booleans" (1 or 0)
    boost_pads: np.ndarray
    inverted_boost_pads: np.ndarray

    #TODO update with grav and boost
    def __str__(self):
        output = "{}GAME STATE OBJECT{}\n" \
                 "Orange Score: {}\n" \
                 "Blue Score: {}\n" \
                 "BALL: {}\n" \
                 "INV_BALL: {}\n" \
                 "".format("*" * 8, "*" * 8,
                           self.orange_score,
                           self.blue_score,
                           self.ball,
                           self.inverted_ball)
        output = "{}BOOSTS: {}\nINV_BOOSTS: {}\n".format(output, self.boost_pads.tolist(),
                                                         self.inverted_boost_pads.tolist())
        for agent in self.agents:
            output = "{}AGENTS: {}\n".format(output, agent)

        return output