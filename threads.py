from threading import Thread

output = {}


def foo(bar):
    return 6


def foo2(bar):
    return 3


def show_output():
    print(max(output.values()))


def got_output(key, val):
    global output
    output[key] = val
    if len(output.keys()) == 2:
        show_output()


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        Thread.__init__(self, group, target, name, args, kwargs, daemon=daemon)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)
            got_output(self._target.__name__, self._return)

    def join(self):
        Thread.join(self)
        return self._return


t1 = ThreadWithReturnValue(target=foo, args=('thr1',))
t2 = ThreadWithReturnValue(target=foo2, args=('thr2',))

t1.start()
t2.start()
