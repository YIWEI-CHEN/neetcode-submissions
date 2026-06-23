
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        1. [0, 1]: 1 -> 0, where 1 pre-req. indegree of 0 = 1 (one edge)
        2. graph tracks a node as pre-req, and its edge are a list of course, that need the pre-req
           [1, 0], [2, 0] => 0 -> 1
                             0 -> 2
            graph = [
                [1, 2]  # pre-req course 0
            ]
        3. Kahn's algo: find the nodes with indegree=0, reduce the indegree of adjanct nodes, and add nodes without indegree
           ie, find courses without prereq, update next courses indegree, if they are free, add to queue
        """
        
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        queue = deque(course for course in range(numCourses) if indegree[course] == 0)
        order = []

        # Kahn's algorith
        while queue:
            course = queue.popleft()
            order.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        # cyclic course, indegree = 1, but order will be zero
        return order if len(order) == numCourses else []

        