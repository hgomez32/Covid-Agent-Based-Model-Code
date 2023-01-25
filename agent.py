import random


class Agent:

    def __init__(self):
        self.health_status = "Susceptible"
        self.color = "green"
        self.recovered = False
        self.y_coordinate = random.uniform(0, 1)
        self.x_coordinate = random.uniform(0, 1)
        self.mask = True
        self.sick_days = 0

    def get_x_coordinate(self):
        return self.x_coordinate

    def set_x_coordinate(self, value):
        self.x_coordinate = value

    def get_y_coordinate(self):
        return self.y_coordinate

    def set_y_coordinate(self, value):
        self.y_coordinate = value

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_sick_days(self):
        return self.sick_days

    def set_mask(self, mask):
        self.mask = mask

    def get_mask(self):
        return self.mask

    def set_sick_days(self, sick_days):
        self.sick_days = sick_days
        if self.health_status == "Sick" and self.sick_days == 0:
            self.color = "purple"
            self.health_status = "Recovered/Vaccinated"

    def set_recovered(self, recovered):
        self.recovered = recovered

    def get_recovered(self):
        return self.recovered

    def get_health_status(self):
        return self.health_status

    def set_health_status(self, status):
        self.health_status = status
        sick_days =14

        if self.health_status == "Sick" and self.sick_days == 0 and not self.recovered:
            self.color = "red"
            self.sick_days = sick_days
        elif self.health_status == "Sick" and self.sick_days == 0 and self.recovered:
            self.color = "red"
            self.sick_days = 5
        elif self.health_status == "Susceptible":
            self.color = "green"
        else:
            self.health_status = "Recovered/Vaccinated"
            self.color = "purple"

    def move(self):
        if self.health_status == "Susceptible" or self.health_status == "Recovered/Vaccinated":
            val = random.uniform(-0.05, 0.05)
            val2 = random.uniform(-0.05, 0.05)
            self.y_coordinate = self.y_coordinate + val
            self.x_coordinate = self.x_coordinate + val2
            while True:
                if self.y_coordinate > 1.0:
                    self.y_coordinate -= 1
                elif self.y_coordinate < 0:
                    self.y_coordinate += 1
                else:
                    break
            while True:
                if self.x_coordinate > 1.0:
                    self.x_coordinate -= 1
                elif self.x_coordinate < 0:
                    self.x_coordinate += 1
                else:
                    break
        if self.health_status == "Sick":
            val = random.uniform(-0.01, 0.01)
            val2 = random.uniform(-0.01, 0.01)
            move = random.randint(0, 1)
            if move == 1:
                self.y_coordinate = self.y_coordinate + val
                self.x_coordinate = self.x_coordinate + val2
                while True:
                    if self.y_coordinate > 1.0:
                        self.y_coordinate -= 1
                    elif self.y_coordinate < 0:
                        self.y_coordinate += 1
                    else:
                        break
                while True:
                    if self.x_coordinate > 1.0:
                        self.x_coordinate -= 1
                    elif self.x_coordinate < 0:
                        self.x_coordinate += 1
                    else:
                        break



