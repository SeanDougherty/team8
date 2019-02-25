import datetime

class Clock(object):
    def __init__(self):
        self.reset()
    def reset(self):
        self.accumulator = datetime.timedelta(0)
        self.started = None
    def start_stop(self):
        if self.started:
            self.accumulator += (
                datetime.datetime.utcnow() - self.started
            )
            self.started = None
        else:
            self.started = datetime.datetime.utcnow()
    @property
    def elapsed(self):
        if self.started:
            return self.accumulator + (
                datetime.datetime.utcnow() - self.started
            )
        return self.accumulator
    def __repr__(self):
        return "<Clock {} ({})>".format(
            self.elapsed,
            'started' if self.started else 'stopped'
        )
