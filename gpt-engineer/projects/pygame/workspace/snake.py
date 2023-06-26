from dataclasses import dataclass
from typing import List

@dataclass
class Segment:
    x: int
    y: int

class Snake:
    def __init__(self, x, y):
        self.segments = [Segment(x, y)]
        self.direction = "right"

    def move(self, direction):
        if (
            (direction == "left" and self.direction != "right") or
            (direction == "right" and self.direction != "left") or
            (direction == "up" and self.direction != "down") or
            (direction == "down" and self.direction != "up")
        ):
            head = self.segments[0]

            if direction == "left":
                new_head = Segment(head.x - 1, head.y)
            elif direction == "right":
                new_head = Segment(head.x + 1, head.y)
            elif direction == "up":
                new_head = Segment(head.x, head.y - 1)
            elif direction == "down":
                new_head = Segment(head.x, head.y + 1)

            self.segments.insert(0, new_head)
            self.segments.pop()

            self.direction = direction

    def grow(self):
        tail = self.segments[-1]
        self.segments.append(tail)

    def get_head_position(self):
        return (self.segments[0].x, self.segments[0].y)

    def get_body_positions(self):
        return [(segment.x, segment.y) for segment in self.segments[1:]]
