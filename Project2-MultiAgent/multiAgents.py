# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util, time

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        "Add more of your code here if you want to"
        # Collect legal moves and successor states
        ghostPosition = gameState.getGhostPositions()
        print ghostPosition
        legalMoves = gameState.getLegalActions()
        print legalMoves

        # Choose one of the best actions
        # scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        # time.sleep(0.5)

        # bestScore = max(scores)
        # bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        # chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        # closestPelet = [self.evaluationFunction(gameState, action) for action in legalMoves]
        # time.sleep(3)

        # peletFix = min(closestPelet)
        # peletFixIndex = [index for index in range(len(closestPelet)) if closestPelet[index] == peletFix]
        # chosenIndex = random.choice(peletFixIndex)

        peletInfo = []
        for action in legalMoves:
            if action != 'stop':  # Stopping just costs better to stay moving
                peletInfo.append(self.evaluationFunction(gameState, action))
        time.sleep(1)

        peletsleft = []
        closestpelet = []
        for action in peletInfo:
            peletsleft.append(action[0])  # number of pelets left depending on direction pacman goes
            closestpelet.append(action[1])  # shortest distance to next pelet given each possible direction
        minpeletleft = min(peletsleft)
        peletsleftindex = [index for index in range(len(peletsleft)) if peletsleft[index] == minpeletleft]
        print peletsleftindex

        if len(peletsleftindex) == 1:  # if there is a only one pelet next to pacman go for it.
            chosenIndex = peletsleftindex[0]
        else:  # otherwise lets go for the next closest pelet
            newclosestpelet = []
            for index in peletsleftindex:
                newclosestpelet.append(closestpelet[index])
            mindistance = min(newclosestpelet)
            mindistanceindex = [index for index in range(len(newclosestpelet)) if newclosestpelet[index] == mindistance]
            print mindistanceindex

            if len(mindistanceindex) == 1:  # if there is an obvious closest pelet lets go for that one
                chosenIndex = mindistanceindex[0]
            else:  # if there are many pelets equally close then take a random guess
                chosenIndex = random.choice(mindistanceindex)

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """

        "*** YOUR CODE HERE ***"
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        # print successorGameState  # graphical interpretation of the state
        newPos = successorGameState.getPacmanPosition()
        # print newPos

        newFood = successorGameState.getFood()
        # print newFood  # matrix grid represenation of the food pelets true / false
        # print type(newFood)
        # print dir(newFood)
        # print newFood.asList()
        # print 'manhattan distance'
        distanceList = []
        for peletPos in newFood.asList():
            distanceList.append(manhattanDistance(newPos, peletPos))
        # print distanceList

        # distanceSum = 0
        # for distance in distanceList:
        #    distanceSum += distance
        # print distanceSum

        distanceMin = min(distanceList) + 0.0
        # print distanceMin

        ghostLocation = successorGameState.getGhostPositions()
        print ghostLocation

        peletsleft = len(distanceList)

        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        evalInfo = []
        evalInfo.append(peletsleft)
        evalInfo.append(distanceMin)
        # return successorGameState.getScore()
        return evalInfo


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game

          gameState.isWin():
            Returns whether or not the game state is a winning state

          gameState.isLose():
            Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

