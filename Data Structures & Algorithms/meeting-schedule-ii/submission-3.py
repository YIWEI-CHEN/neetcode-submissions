"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappop, heappush

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        rooms = []
        
        for interval in intervals:
            if rooms and rooms[0] <= interval.start:
                heappop(rooms)
            heappush(rooms, interval.end)
        return len(rooms)