import pygame
import random
import particle
import asyncio
import pprint
import relations

SIZE = 600
TYPES = {"Red": (255, 0, 0),
         "Green": (0, 255, 0),
         "Blue": (0, 0, 255),
         "Yellow": (255, 255, 0),
         "Purple": (255, 0, 255)}


def create_relation():
    return {
        "attraction": round(random.random() * random.choice([-1, 1]), 2),
        "range": random.randint(75, 150)
    }


def create_relations(names):
    types = {}
    for n in names:
        relations = {o: create_relation() for o in names}

        types.update({n:
                {"colour": (TYPES[n]),
                 "relations": relations}
                })
    pprint.pprint(types)
    return types


async def run_particle(p, particles):
    p.calc_forces(particles)
    p.move()
    pygame.draw.circle(screen, p.colour, p.pos, 5)


async def run_particles(particles):
    futures = [run_particle(p, particles) for p in particles]

    for f in futures:
        await f


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((SIZE, SIZE))

    names = [k for k in TYPES.keys()]
    relations = create_relations(names)

    particles = [particle.Particle(SIZE, random.choice(names), relations) for r in range(250)]

    num = 100

    while True:
        screen.fill((0, 0, 0))

        asyncio.run(run_particles(particles))

        pygame.display.update()
