
import threading

class Singleton:
    # using lock to make singleton thread safe
    _lock =  threading.Lock()
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            # shortcut for avoiding lock overhead
            return cls._instance

        with cls._lock:
            if not cls._instance:
                cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def get_instance(cls):
        return Singleton()


