class Bassin:
    def __init__(self, day, start=int) -> None:
        self.day = day
        self.start = start
        self.pixels = set()

        self.compute(start)

    def compute(self, start):
        self.pixels.add(start)

        neighboors = self.day.get_neighboors_indexes(start)
        for neighboor in neighboors:
            if neighboor not in self.pixels:
                if self.day.at_index(neighboor) <= 8:
                    self.compute(neighboor)
