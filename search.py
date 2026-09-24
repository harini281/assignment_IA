# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    """

    # DFS uses a Stack (LIFO: Last In, First Out).
    # It stores states that are waiting to be explored.
    stack = util.Stack()

    # Get Pac-Man's starting state.
    start = problem.getStartState()

    # Store:
    # (current state, path used to reach that state)
    # The path is empty at the beginning because Pac-Man has not moved yet.
    stack.push((start, []))

    # Remember states that have already been explored.
    visited = set()

    # Continue searching while there are states waiting in the stack.
    while not stack.isEmpty():

        # Take the most recently added state from the stack.
        state, path = stack.pop()

        # If this state is the goal, return the path used to reach it.
        if problem.isGoalState(state):
            return path

        # Only explore this state if we have not explored it before.
        if state not in visited:

            # Mark the current state as explored.
            visited.add(state)

            # Get all possible next moves from the current state.
            for successor, action, stepCost in problem.getSuccessors(state):

                # Add this new action to the path we already followed.
                newPath = path + [action]

                # Store the successor and its path for later exploration.
                stack.push((successor, newPath))

    # If no solution exists, return an empty path.
    return []

def breadthFirstSearch(problem: SearchProblem):

    # BFS uses a Queue (FIFO: First In, First Out).
    queue = util.Queue()

    # Get the starting state.
    start = problem.getStartState()

    # Store (state, path).
    queue.push((start, []))

    # Keep track of explored states.
    visited = set()

    # Continue while there are states waiting.
    while not queue.isEmpty():

        # Take the FIRST-added state from the queue.
        state, path = queue.pop()

        # If this is the goal, return the path.
        if problem.isGoalState(state):
            return path

        # Only explore states we haven't explored before.
        if state not in visited:

            # Mark current state as explored.
            visited.add(state)

            # Find possible next states.
            for successor, action, stepCost in problem.getSuccessors(state):

                # Create the path to that successor.
                newPath = path + [action]

                # Add successor to the queue.
                queue.push((successor, newPath))

    # No solution found.
    return []

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
