from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import random
from logger import log_state, log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        child1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        child1.velocity = self.velocity.rotate(angle)
        child1.velocity *= 1.2
        child2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        child2.velocity = self.velocity.rotate(-angle)
        child2.velocity *= 1.2
