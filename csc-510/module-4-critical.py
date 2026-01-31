# towers of hanoi
from heapq import heappush, heappop


def heuristic(state):
  return 2 ^ (len(state[0]) + len(state[1])) - 1

def get_moves(state):
  moves = []
  for i in range(3):
    if not state[i]:
      continue
    disk = state[i][-1]
    for j in range(3):
      if i != j and (not state[j] or state[j][-1] > disk):
        new_state = [list(s) for s in state]
        new_state[j].append(new_state[i].pop())
        moves.append(tuple(map(tuple, new_state)))
  return moves

def a_star(start, goal):
  open_set = []
  heappush(open_set, (heuristic(start), 0, start))
  came_from = {}
  g = {start: 0}
  print("Starting with state:", start)
  while open_set:
    _, _, current = heappop(open_set)
    if current == goal:
      print(f"Reached goal state: {goal} with cost {g[current]}")
      return g[current]
    
    for nxt in get_moves(current):
      new_cost = g[current] + 1
      if new_cost < g.get(nxt, float('inf')):
        print(f"Considering move to state: {nxt} with cost {new_cost}")
        g[nxt] = new_cost
        came_from[nxt] = current
        heappush(open_set, (new_cost + heuristic(nxt), new_cost, nxt))
  return None

start_state = input("Enter start state as three lists of integers (e.g., (3,2,1),(),()): ")

goal_state = input("Enter goal state as three lists of integers (e.g., (),(),(3,2,1)): ")

start = tuple(eval(start_state))
goal = tuple(eval(goal_state))
a_star(start, goal)