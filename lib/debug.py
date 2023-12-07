#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

# if __name__ == '__main__':
#     print("HELLO! :) let's debug :vibing_potato:")

#     ipdb.set_trace()


g1 = Game("Halo")
g2 = Game("Halo 2")

p1 = Player("Jacob")
p2 = Player("Isabel")

r1 = Result(p1, g1, 1000)
r2 = Result(p1, g1, 850)
r3 = Result(p2, g1, 200)
r4 = Result(p1, g2, 30)

print()
p1.num_times_played(g1)
print()

