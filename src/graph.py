import re

class Graph:

	__graph = {}

    # To add friends for both user when transtraaction happens
	# Insert e2 into the list after e1 and insert e1 into the list after e2
	def insertEdge(self, e1, e2): #
		if e1 in self.__graph:
			if e2 not in self.__graph[e1]:
				self.__graph[e1].append(e2)
		else:
			self.__graph[e1] = [e2]
		if e2 in self.__graph:
			if e1 not in self.__graph[e2]:
				self.__graph[e2].append(e1)
		else:
			self.__graph[e2] = [e1]

	# depth must be 1, 2, or 4, otherwise return False
	def hasPath(self, n1, n2, depth):
		if depth == 1:
			return self.__isFirstDegreeFriend(n1, n2)
		elif depth == 2:
			return self.__isSecondDegreeFriend(n1, n2)
		elif depth == 4:
			return self.__isFourthDegreeFriend(n1, n2)
		else:
			return False

	# return the first degree friends of a given node as a set
	def __friendOf(self, node):
		if node in self.__graph:
			result = set(self.__graph[node])
			result.add(node)
			return result
		else:
			return set()

	# return the second degree friends of a given node as a set
	def __secondDegreeFriendOf(self, node):
		result = self.__friendOf(node) # add first degree friends
		for n in self.__friendOf(node): # add second degree friends (friends of first degree friends)
			result.update(self.__friendOf(n))
		return result

	def __isFirstDegreeFriend(self, n1, n2):
		return n2 in self.__friendOf(n1)

	def __isSecondDegreeFriend(self, n1, n2):
		f1 = self.__friendOf(n1)
		f2 = self.__friendOf(n2)
		# return true iff the intersection of f1 and f2 is non-empty
		return (len(f1 & f2) > 0)

	def __isFourthDegreeFriend(self, n1, n2):
		f1 = self.__secondDegreeFriendOf(n1)
		f2 = self.__secondDegreeFriendOf(n2)
		# return true iff the intersection of f1 and f2 is non-empty
		return (len(f1 & f2) > 0)
