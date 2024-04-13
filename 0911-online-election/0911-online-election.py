class TopVotedCandidate:
    
    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        
        n = len(persons)
        self.leading_votes = n * [0]
        count_votes = defaultdict(int)
        top_candidate = persons[0]
        max_vote = 1
        
        for i in range(n):
            count_votes[persons[i]] += 1
            if count_votes[persons[i]] >= max_vote:
                max_vote = count_votes[persons[i]]
                top_candidate = persons[i]
            self.leading_votes[i] = top_candidate
            
    def q(self, t: int) -> int:
        l, r = 0, len(self.times)-1
        
        if t in self.times:
            return self.leading_votes[self.times.index(t)]
        
        relative_t = 0
        while l <= r:
            mid = (l+r)//2
            if self.times[mid] <= t:
                relative_t = self.times[mid]
                l = mid+1
            else:
                r = mid-1
                
        return self.leading_votes[self.times.index(relative_t)]
            
    
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)