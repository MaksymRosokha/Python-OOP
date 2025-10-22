class Rectangle:
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return self.length * self.height

    def __str__(self):
        return f"Rectangle: length {self.length}, height {self.height}"

    def __repr__(self):
        return f"Rectangle({self.length}, {self.height})"


class Cuboid(Rectangle):
    def __init__(self, length, height, width):
        super().__init__(length, height)
        self.width = width

    def area(self):
        return (super().area() * 2 +
                self.length * self.width * 2 +
                self.height * self.width * 2)

    def volume(self):
        return super().area() * self.width

    def __str__(self):
        return f"Cuboid: length {self.length}, height {self.height}, width {self.width}"


class InvalidData(Exception):
    pass


def print_rectangle_data(rect):
    print(rect)
    print("Area: ", rect.area())
    print("-" * 50)


def print_cuboid_data(cuboid):
    print(cuboid)
    print("Area: ", cuboid.area())
    print("Volume: ", cuboid.volume())
    print("-" * 50)


if __name__ == "__main__":
    rectangles = list()
    cuboids = list()
    try:
        with open("dane.txt", "r") as data:
            for d in data:
                shape = d.split(" ")

                if int(shape[0]) == 1:
                    try:
                        if not len(shape) == 3:
                            raise InvalidData
                        length = float(shape[1])
                        height = float(shape[2])
                        if length <= 0 or height <= 0:
                            raise InvalidData

                        rect = Rectangle(length, height)
                        rectangles.append(rect)
                    except InvalidData:
                        continue
                    except TypeError:
                        continue
                elif int(shape[0]) == 2:
                    try:
                        if not len(shape) == 4:
                            raise InvalidData
                        length = float(shape[1])
                        height = float(shape[2])
                        width = float(shape[3])
                        if length <= 0 or height <= 0 or width <= 0:
                            raise InvalidData
                        cub = Cuboid(length, height, width)
                        cuboids.append(cub)
                    except InvalidData:
                        continue
                    except TypeError:
                        continue

        for rect in rectangles:
            print_rectangle_data(rect)

        for cub in cuboids:
            print_cuboid_data(cub)
    except IOError:
        print("File not found")