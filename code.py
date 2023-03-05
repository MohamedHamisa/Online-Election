class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        votes_count = collections.Counter()
        self.votes_leader = []
        max_votes = -1
        for time, person in zip(times, persons):
            votes_count[person] += 1
            if max_votes <= votes_count[person]:
                max_votes = votes_count[person]
                self.votes_leader.append((time, person)) 
        
    def q(self, t: int) -> int:
        return self.votes_leader[bisect.bisect_left(self.votes_leader, (t, math.inf)) - 1][1]
        
'''
HashMap.put() cost only O(1) for each operation. Therefore,
time complexity: Constructor O(n), q(int t) is O(logn).
'''
