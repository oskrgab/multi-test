class Well:

    def __init__(self, name):
        self.name = name
        self.x_coord = None
        self.y_coord = None
        self.is_producing = False
    
    def set_coordinates(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def start_production(self):
        self.is_producing = True
        print(f"{self.name} is now producing.")
    
    def stop_production(self):
        self.is_producing = False
        print(f"{self.name} has stopped producing.")


if __name__ == "__main__":

    well1 = Well("Well 1")
    well1.set_coordinates(10, 20)
    well1.start_production()
    well1.stop_production()

    well2 = Well("Well 2")
    well2.set_coordinates(30, 40)
    well2.start_production()
    well2.stop_production()

    print(well1.__dict__)
    print(well2.__dict__)
