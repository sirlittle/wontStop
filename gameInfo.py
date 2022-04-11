from typing import List, Tuple, Dict
from player import Player


class LadderState:
    def __init(self, ladderNum: int):
        if ladderNum > 7:
            self.ladderLength = (13-ladderNum)*2 - 1
        else:
            self.ladderLength = ladderNum*2 - 1
        self.playersOnRung = {}
        self.won = False
        self.winningPlayer = -1

    def getPlayerHeight(self, player: Player):
        if player.playerNumber in self.playersOnRung:
            return self.playersOnRung[player.playerNumber]
        else:
            return -1
    
    def movePlayerToNextRung(self, player: Player):
        if not self.won:
            self.playersOnRung[player.playerNumber] = self.getPlayerHeight(player) + 1
            if self.playersOnRung[player.playerNumber] == self.ladderLength:
                self.won = True
                self.winningPlayer = player.playerNumber

    def isLadderPlayable(self):
        return not self.won
        
class RollOption:
    def __init__(self, option1: Tuple[int], option2:Tuple[int], option3:Tuple[int]):
        self.options = list(dict.fromkeys([option1, option2, option3]))

    def getRollOptionsFromRolls(rolls: List[int]):
        return RollOption((rolls[0] + rolls[1], rolls[2] + rolls[3]), (rolls[0] + rolls[2], rolls[1] + rolls[3]), (rolls[0] + rolls[3], rolls[1] + rolls[2]))

    def legitChoicesExist(self, boardState: Dict[int, LadderState]):
        return self.options()
