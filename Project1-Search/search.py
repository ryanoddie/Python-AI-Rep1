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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    """
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())           
    from game import Directions
    
    closed = set()
    fringe = util.Stack() 
    startplan = [(problem.getStartState(), 'Start', 0)]
    #print 'StartNode:' , startplan
    fringe.push(startplan)
    
    while not fringe.isEmpty():
        #fringe = printFringe(fringe)
        testplan = fringe.pop()
        teststatefull = testplan[len(testplan)-1]
        teststate = teststatefull[0]
        #print 'TestState:', teststate
        #print 'ClosedSet:', closed
        #print 'isGoalState:', problem.isGoalState(teststate)
        if problem.isGoalState(teststate) == False:
            closed.add(teststate)
            successors = problem.getSuccessors(teststate)
            #print 'Number of Successors:', len(successors)
            #print 'Possible Successors:', successors
            for successor in successors:
                #print 'Successor:', successor
                #print 'TestPlan:', testplan
                if successor[0] not in closed:
                    newplan = testplan[:]
                    newplan.append(successor)
                    #print 'NewPlan:', newplan
                    fringe.push(newplan)
        else:
            #print 'Found solution!'
            solution = []
            for statefull in testplan[1:]:
                direction = statefull[1]
                #print 'Direction:', direction
                #directionMap = {'North':Directions.NORTH,
                #                'South':Directions.SOUTH, 
                #                'East':Directions.EAST,
                #                'West':Directions.WEST}
                #solution.append(directionMap[direction])
                solution.append(direction)
            #print 'Solution Length', len(solution)
            #util.pause()
            return solution
    return "Failure"

def printFringe(fringe):

    #newfringe = util.Stack()
    newfringe = util.Queue()
    while not fringe.isEmpty():
        singlenode = fringe.pop()
        print "Fringe:", singlenode
        newfringe.push(singlenode)
    # Printing reverses fringe order so put it back    
    while not newfringe.isEmpty():
        singlenode = newfringe.pop()
        fringe.push(singlenode)
    return fringe

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())           
    from game import Directions
    
    closed = set()
    fringe = util.Queue() 
    startplan = [(problem.getStartState(), 'Start', 0)]
    #print 'StartNode:' , startplan
    fringe.push(startplan)
    
    while not fringe.isEmpty():
        testplan = fringe.pop()
        teststatefull = testplan[len(testplan)-1]
        teststate = teststatefull[0]
        print 'TestState:', teststate
        #print 'ClosedSet:', closed
        #print 'isGoalState:', problem.isGoalState(teststate)
        if problem.isGoalState(teststate) == False:
            closed.add(teststate)
            successors = problem.getSuccessors(teststate)
            #print 'Number of Successors:', len(successors)
            #print 'Possible Successors:', successors
            for successor in successors:
                #print 'Successor:', successor
                #print 'Successoro:', successor[0]
                #print 'Closed:', closed
                #print 'TestPlan:', testplan
                if successor[0] not in closed:
                    newplan = testplan[:]
                    newplan.append(successor)
                    #print 'NewPlan:', newplan
                    fringe.push(newplan)
            #util.pause()
        else:
            #print 'Found solution!'
            solution = []
            for statefull in testplan[1:]:
                direction = statefull[1]
                #print 'Direction:', direction
                #directionMap = {'North':Directions.NORTH,
                #                'South':Directions.SOUTH, 
                #                'East':Directions.EAST,
                #                'West':Directions.WEST}
                #solution.append(directionMap[direction])
                solution.append(direction)
            #print 'Solution Length', len(solution)
            #util.pause()
            return solution
    return "Failure"

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())           
    from game import Directions
    
    closed = set()
    fringe = util.PriorityQueue() 
    startplan = [(problem.getStartState(), 'Start', 0)]
    #print 'StartNode:' , startplan
    fringe.push(startplan, startplan[0][2])
    
    while not fringe.isEmpty():
        testplan = fringe.pop()
        teststatefull = testplan[len(testplan)-1]
        teststate = teststatefull[0]
        print 'TestState:', teststate
        #print 'ClosedSet:', closed
        #print 'isGoalState:', problem.isGoalState(teststate)
        if problem.isGoalState(teststate) == False:
            closed.add(teststate)
            successors = problem.getSuccessors(teststate)
            #print 'Number of Successors:', len(successors)
            #print 'Possible Successors:', successors
            for successor in successors:
                print 'Successor:', successor
                print 'Successoro:', successor[0]
                print 'Closed:', closed
                #print 'TestPlan:', testplan
                if successor[0] not in closed:
                    newplan = testplan[:]
                    newplan.append(successor)
                    print 'NewPlan:', newplan
                    fringe.push(newplan, newplan[len(newplan)-1][2])
            #util.pause()
        else:
            #print 'Found solution!'
            solution = []
            for statefull in testplan[1:]:
                direction = statefull[1]
                #print 'Direction:', direction
                #directionMap = {'North':Directions.NORTH,
                #                'South':Directions.SOUTH, 
                #                'East':Directions.EAST,
                #                'West':Directions.WEST}
                #solution.append(directionMap[direction])
                solution.append(direction)
            #print 'Solution Length', len(solution)
            #util.pause()
            return solution
    return "Failure"

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    print "Heuristic:", 0 + heuristic(problem.getStartState(), problem)
    
    closed = set()
    fringe = util.PriorityQueue() 
    startplan = [(problem.getStartState(), 'Start', 0)]
    #print 'StartNode:' , startplan
    fringe.push(startplan, startplan[0][2])
    
    while not fringe.isEmpty():
        testplan = fringe.pop()
        teststatefull = testplan[len(testplan)-1]
        teststate = teststatefull[0]
        #print "Test Heuristic:", heuristic(teststate, problem) 
        print 'TestState:', teststate
        #print 'ClosedSet:', closed
        #print 'isGoalState:', problem.isGoalState(teststate)
        if problem.isGoalState(teststate) == False:
            closed.add(teststate)
            successors = problem.getSuccessors(teststate)
            #print 'Number of Successors:', len(successors)
            #print 'Possible Successors:', successors
            for successor in successors:
                print 'Successor:', successor
                print 'Successoro:', successor[0]
                print 'Closed:', closed
                #print 'TestPlan:', testplan
                if successor[0] not in closed:
                    newplan = testplan[:]
                    newplan.append(successor)
                    print 'NewPlan:', newplan
                    fringe.push(newplan, newplan[len(newplan)-1][2] + heuristic(teststate, problem))
            #util.pause()
        else:
            #print 'Found solution!'
            solution = []
            for statefull in testplan[1:]:
                direction = statefull[1]
                #print 'Direction:', direction
                #directionMap = {'North':Directions.NORTH,
                #                'South':Directions.SOUTH, 
                #                'East':Directions.EAST,
                #                'West':Directions.WEST}
                #solution.append(directionMap[direction])
                solution.append(direction)
            #print 'Solution Length', len(solution)
            #util.pause()
            return solution
    return "Failure"


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
