from enum import Enum
import random
class Suite(Enum):
    SPADE,HEART,CLUB,DIAMOND=range(4)

class Card:
    def __init__(self,suite,face):
        self.suite=suite
        self.face=face

    def __repr__(self):
        # print时显示的字符串
        suites='♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'

    def __lt__(self, other):
        # 重载 < 运算符，支持排序
        if self.suite==other.suite:
            # 同花色比点数
            return self.face<other.face
        # 不同花色比花色值
        return self.suite.value<other.suite.value


class Poker:
    def __init__(self):
        self.cards=[Card(s,f) for s in Suite for f in range(1,14)]
        self.current=0

    def shuffle(self):
        self.current=0
        random.shuffle(self.cards)

    def deal(self):
        