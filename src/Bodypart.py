class Bodypart:
    part_type = None
    hit_points = 0
    contains = []

    def __init__(self, part_type, hp = 10):
        self.part_type = part_type
        self.hit_points = hp
