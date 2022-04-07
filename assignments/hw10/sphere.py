from math import pi


class Sphere:
    """
    Creates a sphere object that you can find the radius,
    surface area, and volume of

    """

    def __init__(self, radius):
        """
        the constructor of the sphere. the only parameter is the radius of
        the sphere
        """
        self.radius = radius

    def get_radius(self):
        """
        returns the radius of the sphere
        """
        return self.radius

    def surface_area(self):
        """
        Returns the surface are of the sphere using the equation 4(pie)radius ** 2
        """

        surface_area = 4 * (pi * (self.radius ** 2))
        return surface_area

    def volume(self):
        """
        returns the volume of the sphere using (4/3) * pi * r^3
        """

        volume = (4 / 3) * pi * (self.radius ** 3)
        return volume
