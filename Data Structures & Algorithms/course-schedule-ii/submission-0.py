from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        1. [0, 1], 1 is a pre-requisite: 1 -> 0; 1 is inbound of 0. ie: prereq -> course
        2. iterate prerequisites to get inbounds of all courses and a prereq for a list of courses
          if indegree = 0. we can start to take that course
        3. if pre-requsities complete, we can take that course
        """
        graph = [[] for _ in range(numCourses)]  # i-course is prereq for a list of course
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        queue = deque(course for course in range(numCourses) if indegree[course] == 0)
        res = []

        while queue:
            course = queue.popleft()
            res.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
            
        return res if len(res) == numCourses else []
