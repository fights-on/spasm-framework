import os
import collections
import multiprocessing as mp
import signal


_RUNNING_PROCESSES = list()


class Pool(object):
    """
    """
    def __init__(self, name, cpus=os.cpu_count(), async=True, timeout=None, init=None):
        self.name = name
        self.cpus = cpus
        self.async = async
        self.timeout = timeout
        self.init = _func_packer(init)
        self.state = "Stopped"
        self._pool = None
    
    def __str__(self):
        output = "SPASM Pool"
        output += "\n  Name: {}".format(self.name)
        output += "\n  CPUs: {}".format(self.cpus)
        output += "\n  Async: {}".format(self.async)
        if self.timeout:
            output += "\n  Timeout:  {}".format(self.timout)
        if self.init:
            output += "\n Initializers:"
            for item in self.init.keys():
                output += "\n    {}".format(item)
        output += "\n  State: {}".format(self.state)
        return output
    
    def __repr__(self):
        return "SPASM Pool: {}".format(self.name)
    
    def start(self):
        if self in _RUNNING_PROCESSES:
            print("{} is already running.".format(self.name))
        else:
            self._pool = mp.Pool(processes=self.cpus, initializer=_initilializer, initargs=(self.init,))
            _RUNNING_PROCESSES.append(self)
            self.state = "Running"
    
    def stop(self):
        if self in _RUNNING_PROCESSES:
            self._pool.close()
            self._pool.join()
            _RUNNING_PROCESSES.remove(self)
            self.state = "Stopped"
        else:
            print("{} is not running.".format(self.name))
    
    def kill(self):
        if self in _RUNNING_PROCESSES:
            self._pool.terminate()
            self._pool.join()
            _RUNNING_PROCESSES.remove(self)
            self.state = "Stopped"
        else:
            print("{} is not running.".format(self.name))
    
    def run(self, func, args=None, kwds=None, timeout=None, run_multiple=False):
        if self.state == "Stopped":
            print("{} is not running.".format(self.name))
        else:
            print(func)


class Process(object):
    """
    """
    def __init__(self, name, timeout=None, init=None):
        pass


def run(name, func, args=None, kwargs=None, timout=None, async=True, run_multiple=False):
    pass
    

def _func_packer(func):
    """
    
    """
    if func:
        if isinstance(func, collections.Iterable) and not isinstance(func, str):
            output = dict()
            current_func = None
            for item in func:
                if isinstance(item, collections.Iterable) and not isinstance(item, str) \
                and not isinstance(item, dict) and callable(item[0]):
                   output[item[0].__name__] = item
                else:
                    if callable(item):
                        current_func = item.__name__
                        output[current_func] = [item]
                    else:
                        output[current_func].append(item)
            return output
        elif callable(func):
            return {func.__name__: [func]}
        else:
            print("{} is not a valid function.".format(func))
    else:
        return None


def _initilializer(funcs=None):
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    if funcs:
        for _, item in funcs.items():
            func = item[0]
            args = list()
            kwargs = dict()
            for arg in item[1:]:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    args.append(arg)
            func(*args, **kwargs)
