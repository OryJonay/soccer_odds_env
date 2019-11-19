# Sports odds betting environment
A sports betting environment for OpenAI Gym.

## Installation

    pip install git+https://github.com/OryJonay/Odds-Gym.git

## Environment

The starting bank is X (X > 0), representing X available bets.
Actions are all available bets for a game (depends on sport), placing 1 bet for each option. Also, the agent can not bet over his current bank (i.e can't place 3 bets when the current bank is 2).
For example, in 3-way betting for soccer, the avilable actions are:

    1. Bet on home team
    2. Bet on away team
    3. Bet on draw
    4. Bet on home team and away team
    5. Bet on home team and draw
    6. Bet on away team and draw
    7. Bet on home team and away team and draw
    8. Don't place a bet for this game

A step is placing a bet on a single game. In each step, the agent knows the betting odds for this game.
The reward for each step is the amount of money won (negative reward when losing money).
An episode is betting for a whole year, when "striking out" (losing all the money) or when winning Y (Y > X) bets total.
