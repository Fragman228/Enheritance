class Spaceobject:
    def __init__(self, size):
        self.size = size

class Planet:

    @staticmethod
    def poputation(size, years, engrowment):
        return f"Size of planet - {Spaceobject(size)}\nPopulation of current planet after"\
               f" {years} will be {engrowment}"

class Stars(Spaceobject):
    def shiness(self, brightness):
        self.brightness = brightness
        return f"Size of planet - {Spaceobject(self.size).size}\nBrightness of this star is {self.brightness}"


print(Planet.poputation(Spaceobject(5).size,2,3000000))
