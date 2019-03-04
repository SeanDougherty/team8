import datetime

class Clock(object):

	#Will reset the clock object upon call
    def __init__(self):
        self.reset()
    def reset(self):
        self.accumulator = datetime.timedelta(0)
        self.started = None
	#When calling the first time it will start the clock and stop when called again
    def start_stop(self):
        if self.started:
            self.accumulator += (
                datetime.datetime.utcnow() - self.started
            )
            self.started = None
        else:
            self.started = datetime.datetime.utcnow()
    @property
	#calculates elapsed time
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
