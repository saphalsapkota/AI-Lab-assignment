import random

class ReflexAgent:
    def __init__(self,room_size=(10,10)):
        self.room_size = room_size
        #initialize the room as a 10x10 grid with random 0 (clean) 1 (dirty) cells.
        self.grid = [[random.choice([0,1]) for _ in range(room_size[1])] for _ in range(room_size[0])]
        print(self.grid)
        #Initialize the agent's position randomly
        self.current_position = (random.randint(0,room_size[0]-1),random.randint(0,room_size[1]-1))
        print(f"Agent's Position is: {self.current_position}")
    def display_room(self):
        #Display the current status of the room grid
        for row in self.grid:
            for cell in row:
                print(str(cell), end=" ")
            print("\n")
    #
    def perceive(self):
        # Perceive the cleanliness of the current cell
        x, y = self.current_position
        return self.grid[x][y]
    #
    def act(self):
        # perform action based on the perception (clean the cell if dirty)
        x, y = self.current_position
        if self.perceive() == 1:
            print(f"cell ({x}, {y}) is Dirty. Cleaning.....")
            self.grid[x][y] = 0 #Clean the cell (set to 0)
            print(f"Cell ({x}, {y}) is now clean.")
        else:
            print(f"Cell ({x}, {y}) is already Clean. ")
    #
    # def move(self):
    #     # Systematic movement to cover the entire grid row by row
    #     x, y = self.current_position
    #     if y < self.room_size[1] -1: #move to the next cell in the same row
    #         self.current_position = (x, y + 1)
    #     elif x < self.room_size[0] - 1: #Move to the first cell of the new row
    #         self.current_position = (x + 1, 0)
    #     else:
    #         self.current_position = None # All cells have been visited
    #
    # Modified move method..
    def optimized_move(self):
        #Tracking of visited cells
        if not hasattr(self,'visited'):
            self.visited = set()
        self.visited.add(self.current_position)
        print(f"visited cells: {self.visited}")

        x,y = self.current_position
        room_height, room_width = self.room_size

        # Check unvisited neighbors first
        possible_moves = [
            (x,y+1),  #right
            (x+1,y), #down
            (x,y-1), #left
            (x-1,y) #up
        ]

        #Finding nearest unvisited dirty cell
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            new_x, new_y = x+dx, y+dy
            if(0<= new_x < room_height and
                0<= new_y < room_width and
                (new_x, new_y) not in self.visited and
                self.grid[new_x][new_y] == 1):
                self.current_position = (new_x, new_y)
                return
        # Any unvisited cell
        for new_x, new_y in possible_moves:
            if(0<= new_x < room_height and
                0<= new_y < room_width and
                (new_x, new_y) not in self.visited):
                self.current_position = (new_x, new_y)
                return
        # Finding nearest dirty cell
        if not self.is_room_clean():
            for i in range(room_height):
                for j in range(room_width):
                    if self.grid[i][j] ==  1:
                        self.current_position = (i,j)
                        return
        else: # If no moves found, mark as complete
            self.current_position = None

    def is_room_clean(self):
        # Check if the entire room is clean
        return all(cell == 0 for row in self.grid for cell in row)

    def run(self):
        # Display initial status of the room
        print("Initial Room Status: ")
        self.display_room()

        steps = 0
        while not self.is_room_clean():
            print(f"\nStep {steps + 1}: ")
            self.act()
            self.optimized_move()
            steps += 1
            if self.current_position is None:
                # Restart from the top left corner if needed to ensure all cells
                self.current_position = (0, 0)
        # Display final status of the room
        print("\nFinal Room Status: ")
        self.display_room()
        print(f"Room cleaned in {steps} steps.")
# Create and run the Room Cleaner Agent
agent = ReflexAgent()
agent.run()
