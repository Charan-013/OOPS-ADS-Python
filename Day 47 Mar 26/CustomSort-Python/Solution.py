from functools import cmp_to_key

class Team:
    def __init__(self, team_name, wins, losses, draws, no_result, points):
        self.team_name = team_name
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.no_result = no_result
        self.points = points
    
    def __str__(self):
        return f"{self.team_name}: Points={self.points}, Wins={self.wins}, Losses={self.losses}, Draws={self.draws}, NoResult={self.no_result}"

    @staticmethod
    def compare(self, other):
        if self.points < other.points:
            return 1
        elif self.points > other.points:
            return -1
        else:
            if self.wins < other.wins:
                return 1
            elif self.wins > other.wins:
                return -1
            else:
                if self.losses < other.losses:
                    return -1
                elif self.losses > other.losses:
                    return 1
                else:
                    if self.draws < other.draws:
                        return 1
                    elif self.draws > other.draws:
                        return -1
                    else:
                        if self.no_result < other.no_result:
                            return -1
                        elif self.no_result > other.no_result:
                            return 1
                        else:
                            if self.team_name < other.team_name:
                                return -1
                            elif self.team_name > other.team_name:
                                return 1
        return 0

class Heap:
    def __init__(self):
        self.queue = []
        self.size_ = 0
    
    def add(self, e):
        self.queue.append(e)
        self.size_ += 1
        self.bubble_up(self.size_ - 1)

    def offer(self, e):
        self.add(e)

    def clear(self):
        self.queue = []
        self.size_ = 0

    def contains(self, o):
        return o in self.queue
    
    def iterator(self):
        return iter(sorted(self.queue, key=cmp_to_key(Team.compare)))
    
    def peek(self):
        if len(self.queue) < 1:
            return None
        highest_priority = min(self.queue, key=cmp_to_key(Team.compare))
        return highest_priority
    
    def poll(self):
        if len(self.queue) < 1:
            return None
        root = self.queue[0]
        self.queue[0] = self.queue[self.size_ - 1]
        self.size_ -= 1
        self.queue.pop()
        self.bubble_down(0)
        return root

    def remove(self, o):
        if len(self.queue) < 1:
            return False
        for ele in self.queue[::]:
            if ele == o:
                self.queue.remove(ele)
                return True
        return False
    
    def size(self):
        return self.size_

    def bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if Team.compare(self.queue[index], self.queue[parent]) < 0:
                self.queue[index], self.queue[parent] = self.queue[parent], self.queue[index]
                index = parent
            else:
                break

    def bubble_down(self, idx):
        left = 2 * idx + 1
        right = 2 * idx + 2
        s = idx
        
        if left < self.size_ and Team.compare(self.queue[left], self.queue[s]) < 0:
            s = left
        
        if right < self.size_ and Team.compare(self.queue[right], self.queue[s]) < 0:
            s = right
        
        if s != idx:
            self.queue[idx], self.queue[s] = self.queue[s], self.queue[idx]
            self.bubble_down(s)

def main():
    data = []
    c = 0
    while True:
        try:
            s = input().split(",")
            if len(s) == 1:
                c = int(s[0])
            elif len(s) > 1:
                team = Team(s[0], int(s[1]), int(s[2]), int(s[3]), int(s[4]), int(s[5]))
                data.append(team)
        except Exception as e:
            break
    
    heap = Heap()
    for team in data:
        heap.add(team)
    
    print(f"Top {c} teams:")
    for i in range(c):
        print(heap.poll())

main()
