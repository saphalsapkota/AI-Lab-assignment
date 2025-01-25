# 4. Implement missionarie and cannible problem (CRN: 020-392, Last Digit: 2)


from collections import deque

class MissionariesAndCannibals:
    def __init__(self, missionaries=3, cannibals=3):
        self.missionaries = missionaries
        self.cannibals = cannibals

    def is_valid_state(self, state):
        # Validate state doesn't have more cannibals than missionaries on either side
        ml, cl, boat = state
        mr, cr = self.missionaries - ml, self.cannibals - cl
        
        if ml < 0 or cl < 0 or mr < 0 or cr < 0:
            return False
        
        if (ml > 0 and cl > ml) or (mr > 0 and cr > mr):
            return False
        
        return True

    def get_successors(self, state):
        ml, cl, boat = state
        successors = []
        
        # Possible moves when boat is on left side
        if boat == 1:
            moves = [
                (ml-2, cl, 0),   # 2 missionaries
                (ml-1, cl-1, 0), # 1 missionary, 1 cannibal
                (ml, cl-2, 0),   # 2 cannibals
                (ml-1, cl, 0),   # 1 missionary
                (ml, cl-1, 0)    # 1 cannibal
            ]
        # Possible moves when boat is on right side
        else:
            moves = [
                (ml+2, cl, 1),   # 2 missionaries
                (ml+1, cl+1, 1), # 1 missionary, 1 cannibal
                (ml, cl+2, 1),   # 2 cannibals
                (ml+1, cl, 1),   # 1 missionary
                (ml, cl+1, 1)    # 1 cannibal
            ]
        
        return [move for move in moves if self.is_valid_state(move)]

    def solve(self):
        start_state = (self.missionaries, self.cannibals, 1)
        goal_state = (0, 0, 0)
        
        queue = deque([(start_state, [start_state])])
        visited = set()
        
        while queue:
            current_state, path = queue.popleft()
            
            if current_state in visited:
                continue
            
            visited.add(current_state)
            
            if current_state == goal_state:
                return path
            
            for successor in self.get_successors(current_state):
                if successor not in visited:
                    queue.append((successor, path + [successor]))
        
        return None

# Run the solution
solver = MissionariesAndCannibals()
solution = solver.solve()

if solution:
    print("Solution path:")
    for state in solution:
        ml, cl, boat = state
        print(f"Left Bank: {ml} Missionaries, {cl} Cannibals | Boat: {'Left' if boat else 'Right'}")
else:
    print("No solution found")