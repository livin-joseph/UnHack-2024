from collections import defaultdict

class Wafer():
    def __init__(self, type, processing_times, id, quantity):
        self.type = type
        self.steps = list(processing_times.keys())
        self.processing_times = processing_times
        self.id = id
        self.quantity = quantity
        self.time = 0
        self.dependencies = defaultdict(list)
    def __str__(self):
        return str([f"{self.type}-{self.id}", self.steps, self.processing_times, self.dependencies])

class Machine():
    def __init__(self, id, step_id, cooldown_time, params, fluctuation, n):
        self.id = id
        self.step_id = step_id
        self.cooldown_time = cooldown_time
        self.params = params
        self.fluctuation = fluctuation
        self.n = n
        self.curr_n = n

        self.start_time = 0
        self.end_time = 0
    def __str__(self):
        return str([self.id, self.step_id, self.cooldown_time, self.params, self.fluctuation, self.n, self.curr_n, self.start_time, self.end_time])

    def __lt__(self, other):
        return self.end_time < other.end_time
