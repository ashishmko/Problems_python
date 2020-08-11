
class Robot:
    rotate_left = {
        'N' : 'W',
        'E' : 'N',
        'W' : 'S',
        'S' : 'E'
    }

    rotate_right = {
        'N' : 'E',
        'E' : 'S',
        'W' : 'N',
        'S' : 'W'
    }

    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 'N'

    def getX(self):
        return self.x

    def getY(self):
        return self.y


    def rotateLeft(self):
        self.direction = self.rotate_left[self.direction]

    def rotateRight(self):
        self.direction = self.rotate_right[self.direction]

    def moveAhead(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'W':
            self.x -= 1
        elif self.direction == 'S':
            self.y -= 1
        else:
            self.x += 1

    def getDirection(self):
        return self.direction

    def getDescription(self):
        if self.direction == 'N':
            print("Robot at ({},{}) facing North".format(self.x, self.y))

        if self.direction == 'E':
            print("Robot at ({},{}) facing East".format(self.x, self.y))

        if self.direction == 'W':
            print("Robot at ({},{}) facing West".format(self.x, self.y))

        if self.direction == 'S':
            print("Robot at ({},{}) facing South".format(self.x, self.y))





if __name__ == '__main__':
    rover = Robot()

    message = '''
    Hello! Robot coming online

    Command the robot with:
    L - turn left
    R - turn right
    M - move forward
    ? - print this message
    Q - quit
    '''


    ch = 0  
    while True:
        if ch == 0:
            print(message)

        ch = input("> ")

        ch = ch.upper()

        if ch == 'L':
            rover.rotateLeft()
            rover.getDescription()
        elif ch == 'R':
            rover.rotateRight()
            rover.getDescription()
        elif ch == 'M':
            rover.moveAhead()
            rover.getDescription()
        elif ch == '?':
            print(message)
        elif ch == 'Q':
            print("  Robot shutting down  ")
        else:
            print("Invalid Option")


        if ch =='Q':
            break
