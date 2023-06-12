"""
Drawing Library for MicroPython SSD1306 OLED displays.
draws pixel by pixel circles and elypses

by Roy Medina

"""


class Drawer:
    def __init__(self, oled):
        self.oled = oled

    def draw_circle(self, x0, y0, r):
        x = r
        y = 0
        decision_over_2 = 1 - x

        while y <= x:
            self.oled.pixel(x0 + x, y0 + y, 1) # Octant 1
            self.oled.pixel(x0 + y, y0 + x, 1) # Octant 2
            self.oled.pixel(x0 - y, y0 + x, 1) # Octant 3
            self.oled.pixel(x0 - x, y0 + y, 1) # Octant 4
            self.oled.pixel(x0 - x, y0 - y, 1) # Octant 5
            self.oled.pixel(x0 - y, y0 - x, 1) # Octant 6
            self.oled.pixel(x0 + y, y0 - x, 1) # Octant 7
            self.oled.pixel(x0 + x, y0 - y, 1) # Octant 8
            y += 1
            if decision_over_2 <= 0:
                decision_over_2 += 2 * y + 1
            else:
                x -= 1
                decision_over_2 += 2 * (y - x) + 1
        self.oled.show()

    def draw_ellipse(self, x0, y0, a, b):
        a2 = a*a
        b2 = b*b
        twoa2 = 2*a2
        twob2 = 2*b2
        p = round(b2 - (a2 * b) + (0.25 * a2))
        x = 0
        y = b
        px = 0
        py = twoa2 * y
        while px < py:  # first region of ellipse
            self.draw_ellipse_points(x0, y0, x, y)
            x += 1
            px += twob2
            if p < 0:
                p += b2 + px
            else:
                y -= 1
                py -= twoa2
                p += b2 + px - py
        p = round(b2 * (x + 0.5) * (x + 0.5) + a2 * (y - 1) * (y - 1) - a2 * b2)
        while y >= 0:  # second region of ellipse
            self.draw_ellipse_points(x0, y0, x, y)
            y -= 1
            py -= twoa2
            if p > 0:
                p += a2 - py
            else:
                x += 1
                px += twob2
                p += a2 - py + px
        self.oled.show()

    def draw_ellipse_points(self, x0, y0, x, y):
        self.oled.pixel(x0 + x, y0 + y, 1)
        self.oled.pixel(x0 - x, y0 + y, 1)
        self.oled.pixel(x0 + x, y0 - y, 1)
        self.oled.pixel(x0 - x, y0 - y, 1)
