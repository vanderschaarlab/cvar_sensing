class RunningAverageMeter:
    """Computes and stores the average and current value"""

    def __init__(self, momentum=0.99):
        self.momentum = momentum
        self.reset()

    def reset(self):
        self.val = None
        self.avg = 0

    def update(self, val):
        if self.val is None:
            self.avg = val
        else:
            self.avg = self.avg * self.momentum + val * (1 - self.momentum)
        self.val = val


class AggregateMeters:
    def __init__(self, items, momentum=0.99):
        self.meters = {}
        for item in items:
            self.meters[item] = RunningAverageMeter(momentum)

    def reset(self, items=[]):
        for item in items:
            self.meters[item].reset()

    def update(self, pairs={}):
        for k, v in pairs.items():
            self.meters[k].update(v)

    def report(self):
        output = {k: v.avg for k, v in self.meters.items() if v.val is not None}
        return output
