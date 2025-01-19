from collections import deque
class WaterJug:
    def __init__(self, initial_state=(0, 0), goal_state=(2, 0)):
        # Define the initial and goal states
        self.initial_state = initial_state  # Initial state: (0, 0)
        self.goal_state = goal_state  # Goal state: (2, 0)

    def successors(self, state):
        X, Y = state
        succ = []

        # Action 1: Fill Jug X
        if X < 4:
            succ.append((4, Y))

        # Action 2: Fill Jug Y
        if Y < 3:
            succ.append((X, 3))

        # Action 3: Empty Jug X
        if X > 0:
            succ.append((0, Y))

        # Action 4: Empty Jug Y
        if Y > 0:
            succ.append((X, 0))

        # Action 5: Pour from X to Y
        if X > 0 and Y < 3:
            transfer = min(X, 3 - Y)
            succ.append((X - transfer, Y + transfer))

        # Action 6: Pour from Y to X
        if Y > 0 and X < 4:
            transfer = min(Y, 4 - X)
            succ.append((X + transfer, Y - transfer))

        return succ

    def bfs_with_path(self, initial_state, goal_state):
        open_queue = deque([(initial_state, [initial_state])])
        closed_set = set() #set to keep track of visited states

        while open_queue:
            #Get next state and its path from queue
            current_state, path = open_queue.popleft()
            #add current state to visited set
            closed_set.add(current_state)

            if current_state == goal_state:
                return path
            # Generate all possible next states
            for succ in self.successors(current_state):
                # check if successor is unvisited and no already in queue
                if succ not in closed_set and succ not in [state for state, _ in open_queue]:
                    #create new path by adding successor to current path
                    new_path = path + [succ]
                    open_queue.append((succ, new_path))

        return None

    def run(self):
        # Run BFS to find the solution
        result = self.bfs_with_path(self.initial_state, self.goal_state)
        if result is None:
            print("Goal not found")
        else:
            print("Goal found:", result)


# Create an instance of the WaterJug class and run it
sol = WaterJug()
sol.run()


#Note: Implement path generate method to generate path of the solution