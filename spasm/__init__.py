"""

"""
import os
import multiprocessing
import signal
import collections
import time


_SETTINGS = {
    "plugin_dir": "./plugins"
}


class Process(object):
    """

    """
    def __init__(self, name, timeout=None, init=None):
        """

        :param name: Easy to reference name of the process
        :param timeout: Default timeout of all action ran by this process
        :param init: Custom initialization functions
        """
        self.name = name
        self.timeout = timeout
        self.init = init
        self.state = "Stopped"
        self._process = None
        self._queue = None

    def __str__(self):
        """

        :return:
        """
        output = "Process:\n\tName: {}".format(self.name)
        if self.timeout:
            output += "\n\tTimeout: {}".format(self.timeout)
        if self.init:
            if isinstance(self.init, collections.Iterable):
                output += "\n\tInitial Functions: "
                for init in self.init:
                    output += "\n\t\t{}".format(init.__name__)
            else:
                output += "\n\tInitial Function: {}".format(self.init.__name__)
        output += "\n\tState: {}".format(self.state)
        return output

    def start(self):
        self._queue = multiprocessing.JoinableQueue()
        self._process = multiprocessing.Process(target=_process_worker, args=(self._queue,), name=self.name)
        self._process.daemon = True
        self._process.start()
        self.state = "Running"

    def stop(self):
        self._queue.put("!@#$1234SENTINEL4321$#@!")
        self.state = "Stopped"
        self._process.join()
        self._queue.join()

    def kill(self):
        pass

    def run(self):
        pass


class Pool(object):
    """

    """
    def __init__(self, name, timeout=None, async=True, ordered=True, init=None, cpus=None):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def kill(self):
        pass

    def run(self):
        pass

    def _init(self):
        pass


class Server(object):
    """

    """
    def __init__(self):
        pass


class Client(object):
    """

    """
    def __init__(self):
        pass


def set_plugin_dir(path):
    """
    Sets the plugin path for SPASM
    :return: None
    """
    path = os.path.abspath(path)
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)
    _SETTINGS["plugin_dir"] = path


def _init():
    """

    :return:
    """
    signal.signal(signal.SIGINT, signal.SIG_IGN)


def _process_worker(queue):
    """

    :return:
    """
    _init()
    while True:
        try:
            data = queue.get()
            if data == "!@#$1234SENTINEL4321$#@!":
                queue.task_done()
                break
            if len(data) == 1:
                func = data[0]
                print(func)
            else:
                func = data[0]
                args = data[1:]
                print(func, args)
            queue.task_done()
        except multiprocessing.Queue.empty():
            pass
