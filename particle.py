import math
import random


class Particle:

    def __init__(self, size, type, relations):

        self.size = size
        self.pos = [random.randint(0, self.size), random.randint(0, self.size)]
        self.vel = [0, 0]
        self.type = type
        self.colour = relations[type]["colour"]
        self.relations = relations[type]["relations"]

    def getpos(self):
        return int(self.pos[0]), int(self.pos[1])

    def wrap(self, dimension):
        if self.pos[dimension] < 0:
            self.pos[dimension] += self.size
        elif self.pos[dimension] > self.size:
            self.pos[dimension] -= self.size

    def move(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        self.wrap(0)
        self.wrap(1)

    def get_attraction_for(self, otype):
        return self.relations[otype]["attraction"]

    def get_range_for(self, otype):
        return self.relations[otype]["range"]

    def calc_distance_over_wrap(self, other, dimension):
        delta = self.pos[dimension] - other.pos[dimension]
        if delta > (self.size/2):
            delta -= self.size
        if delta < (self.size/-2):
            delta += self.size
        return delta

    def calculate_attraction(self, other):

        xd = self.calc_distance_over_wrap(other, 0)
        yd = self.calc_distance_over_wrap(other, 1)
        range = self.get_range_for(other.type)
        distance = math.sqrt(xd**2 + yd**2)

        if distance >= 20 + range:
            return

        limit = 15
        attraction = self.get_attraction_for(other.type)
        angle = math.atan2(yd, xd)

        force = 0
        if distance < limit:
            force = 2
        elif distance < limit + (range/2):
            force = 2 * (attraction/range) * (distance - limit)
        elif distance < limit + range:
            force = 2 * (attraction/range) * (limit - distance) + (2 * attraction)

        self.vel[0] += force * math.cos(angle)
        self.vel[1] += force * math.sin(angle)

    def calc_forces(self, others):
        friction = 0.6

        for o in others:
            if o is not self:
                self.calculate_attraction(o)
        self.vel[0] *= friction
        self.vel[1] *= friction

