import enum
import pygame


class Color(enum.Enum):
    WHITE = (0xFF, 0xFF, 0xFF)
    BLACK = (0, 0, 0)

    GREEN = (0, 0xFF, 0)

    LOWER0 = (0, 0, 255 - (20 * 1))
    LOWER1 = (0, 0, 255 - (20 * 2))
    LOWER2 = (0, 0, 255 - (20 * 3))
    LOWER3 = (0, 0, 255 - (20 * 4))
    LOWER4 = (0, 0, 255 - (20 * 5))
    LOWER5 = (0, 0, 255 - (20 * 6))
    LOWER6 = (0, 0, 255 - (20 * 7))
    LOWER7 = (0, 0, 255 - (20 * 8))
    LOWER8 = (0, 0, 255 - (20 * 9))
    LOWER9 = (0, 0, 255 - (20 * 10))

    DEFAULT = (0, 0, 50)

    @classmethod
    def getColorFromPt(cls, pt: int) -> tuple:
        return getattr(cls, f"LOWER{pt}")


class Drawing:
    def __init__(self, day) -> None:
        self.day = day

    def fill_pixel(self, x, y, color):
        pygame.draw.rect(
            self.screen,
            color,
            pygame.Rect(
                x * self.pixel_width,
                y * self.pixel_height,
                self.pixel_width,
                self.pixel_height,
            ),
        )

    def start(self):
        size = width, height = 800, 600

        self.pixel_width = int(width / self.day.width)
        self.pixel_height = int(height / self.day.height)

        speed = [2, 2]
        black = 0, 0, 0
        self.screen = pygame.display.set_mode(size)

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.screen.fill(black)

            for index in range(len(self.day.map)):
                x, y = self.day.get_coord_from_index(index)
                pt = self.day.at(x, y)
                neighboors = self.day.neighboors(x, y)
                self.fill_pixel(x, y, Color.getColorFromPt(pt).value)

                if all(pt < n for n in neighboors):
                    self.fill_pixel(x, y, Color.GREEN.value)

            pygame.display.flip()
