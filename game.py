from typing import List
from gameInfo import LadderState, RollOption
from player import Player
import random


class Game:
    def __init__(self, numOfPlayers=3):
        self.playerToScore = {}
        self.ladders = {num: LadderState() for num in range(2, 13)}
        self.players = [Player(i) for i in range(numOfPlayers)]
        self.roundNumber = 0

    def getPlayer(self, turnNumber):
        return self.players[turnNumber % len(self.players)]

    def playRound(self):
        roundOver = False
        turnNumber = 0
        while not roundOver:
            turnNumber += 1
            self.playTurn(turnNumber)
            # check score

    def checkRoundOver(self, ):
        hi = 234

    def playTurn(self, turnNumber: int):
        currPlayer = self.getPlayer(turnNumber)
        stopping = False
        tempBoardState = self.ladders
        while not stopping:
            # role dice
            choices = self.rollDice()
            # ask player to select choice from dice
            choice = currPlayer.chooseDiceRole(choices)

            # ask player if they want to stop


    def rollDice(self) -> RollOption : 
        diceResults = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
        return RollOption.getRollOptionsFromRolls(diceResults)

    def playersTurn(player):
        hi = 123
