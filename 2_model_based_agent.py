
# 2. Improve the vacuum cleaning agent’s efficiency by implementing a model-based agent. Provide your arguments.
# A model-based intelligent agent is an agent with internal state or memory. It uses this internal state to retain informaton regarding its environment/world. This information can then help the agent make its decisions afterwards. Here, the reflex agent from first question is improved as it is making use of self.room (i.e. the state of the room) to make informed movements. Particularly, the nearest_dirty_position() method is introduced which provides position/location of nearest dirty cell in the room with Euclidean distance measurement. This method is utilized by the updated move() method that moves the vacuum agent closer to this position instead of moving sequentially as was the previous case with reflex agent.

# We observe improvements as the steps taken by this model-based agent are almost always less than that of prior reflex agent.

from math import dist
from random import randint


class VacuumModelBasedAgent:
    def __init__(self, size=(10, 10)):
        """
        Initialize room of provided size as 2D array and choose random starting position.
        """
        self.size = size
        self.room = [[randint(0, 1) for _ in range(size[0])] for _ in range(size[1])]
        self.position = [randint(0, size[0] - 1), randint(0, size[1] - 1)]

    def display_room(self):
        """
        Display all cells of room.
        """
        for row in self.room:
            for cell in row:
                print(cell, end=" ")
            print()

    def perceive(self):
        """
        Perceive the cleanliness at current position with 1 being dirty and 0 being clean.
        """
        x, y = self.position
        return self.room[x][y]

    def act(self):
        """
        Clean if perception indicates current cell is dirty.
        """
        x, y = self.position
        if self.perceive() == 0:
            print(f"Cell ({x}, {y}) is already clean.")
            return
        print(f"Cell ({x}, {y}) is dirty. Cleaning ...")
        self.room[x][y] = 0
        print(f"Cell ({x}, {y}) is now cleaned.")

    def nearest_dirty_position(self):
        """
        Calculates and returns the nearest dirty position from current position
        """
        x, y = self.position
        height, width = self.size

        nearest_dirty = None
        nearest_distance = height * width  # initially set to large value
        for i in range(height):
            for j in range(width):
                if self.room[i][j] == 0:  # skip if cell is clean
                    continue
                d = dist((x, y), (i, j))  # calculate Euclidean distance
                if d < nearest_distance:
                    nearest_distance = d
                    nearest_dirty = [i, j]

        return nearest_dirty

    def move(self):
        """
        Move closer to nearest dirty position.
        """
        dirty_position = self.nearest_dirty_position()
        if dirty_position is None:
            return

        x, y = self.position
        nx, ny = dirty_position
        if y < ny:
            y = y + 1
        elif y > ny:
            y = y - 1

        if x < nx:
            x = x + 1
        elif x > nx:
            x = x - 1

        self.position = [x, y]

    def room_cleaned(self):
        """
        Check if the room has been completely cleaned.
        """
        return all(cell == 0 for row in self.room for cell in row)

    def run(self):
        """
        Run the model-based Vacuum Agent.
        """
        print("Initial status of room (with 1 = dirty and 0 = clean):\n")
        self.display_room()

        steps = 0
        while not self.room_cleaned():
            steps += 1
            print(f"\nStep {steps}:")
            self.act()
            self.move()

        print(f"\nRoom is totally cleaned in {steps} steps.\n")
        self.display_room()


agent = VacuumModelBasedAgent()
agent.run()


