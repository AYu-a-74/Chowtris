from ChowMians import Block
from XYZs import Position
class OChow(Block):#Original Chow
    def __init__(self):
        super().__init__(id=1)
        self.cells={
            0:[Position(0,0),Position(0,1),Position(1,0),Position(1,1)],
            1:[Position(0,0),Position(0,1),Position(1,0),Position(1,1)],
            2:[Position(0,0),Position(0,1),Position(1,0),Position(1,1)],
            3:[Position(0,0),Position(0,1),Position(1,0),Position(1,1)]
        }
        self.move(0,4)
class LChow(Block):#Loser Chow
    def __init__(self):
        super().__init__(id=3)
        self.cells={
            0:[Position(0,2),Position(1,0),Position(1,1),Position(1,2)],
            1:[Position(0,1),Position(1,1),Position(2,1),Position(2,2)],
            2:[Position(1,0),Position(1,1),Position(1,2),Position(2,0)],
            3:[Position(0,0),Position(0,1),Position(1,1),Position(2,1)]
        }
        self.move(0,3)
class JChow(Block):#Jason Chow
    def __init__(self):
        super().__init__(id=2)
        self.cells={
            0:[Position(0,0),Position(1,0),Position(1,1),Position(1,2)],
            1:[Position(0,1),Position(0,2),Position(1,1),Position(2,1)],
            2:[Position(1,0),Position(1,1),Position(1,2),Position(2,2)],
            3:[Position(0,1),Position(1,1),Position(2,0),Position(2,1)]
        }
        self.move(0,3)
class IChow(Block):#I am Chow
    def __init__(self):
        super().__init__(id=6)
        self.cells={
            0:[Position(1,0),Position(1,1),Position(1,2),Position(1,3)],
            1:[Position(0,2),Position(1,2),Position(2,2),Position(3,2)],
            2:[Position(2,0),Position(2,1),Position(2,2),Position(2,3)],
            3:[Position(0,1),Position(1,1),Position(2,1),Position(3,1)]
        }
        self.move(-1,3)
class SChow(Block):#Suck Chow
    def __init__(self):
        super().__init__(id=5)
        self.cells={
            0:[Position(0,1),Position(0,2),Position(1,0),Position(1,1)],
            1:[Position(0,1),Position(1,1),Position(1,2),Position(2,2)],
            2:[Position(1,1),Position(1,2),Position(2,0),Position(2,1)],
            3:[Position(0,0),Position(1,0),Position(1,1),Position(2,1)]
        }
        self.move(0,3)
class ZChow(Block):#Zero Chow
    def __init__(self):
        super().__init__(id=4)
        self.cells={
            0:[Position(0,0),Position(0,1),Position(1,1),Position(1,2)],
            1:[Position(0,2),Position(1,1),Position(1,2),Position(2,1)],
            2:[Position(1,0),Position(1,1),Position(2,1),Position(2,2)],
            3:[Position(0,1),Position(1,0),Position(1,1),Position(2,0)]
        }
        self.move(0,3)
class Tam(Block):# Mr.Tam
    def __init__(self):
        super().__init__(id=7)
        self.cells={
            0:[Position(0,1),Position(1,0),Position(1,1),Position(1,2)],
            1:[Position(0,1),Position(1,1),Position(1,2),Position(2,1)],
            2:[Position(1,0),Position(1,1),Position(1,2),Position(2,1)],
            3:[Position(0,1),Position(1,0),Position(1,1),Position(2,1)]
        }
        self.move(0,3)