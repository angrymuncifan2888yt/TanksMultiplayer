class Timer:
    def __init__(self, time: float):
        self.duration = time
        self.time_left = time
        self.paused = False
        self.finised = False

    def update(self, delta: float = 1.0):
        if self.paused or self.finised:
            return

        self.time_left -= delta

        if self.time_left <= 0:
            self.time_left = 0
            self.finised = True

    def pause(self):
        self.paused = True

    def resume(self):
        if not self.finised:
            self.paused = False

    def reset(self):
        self.time_left = self.duration
        self.paused = False
        self.finised = False