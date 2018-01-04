import io
import logging
import pstats
import time
from cProfile import Profile
from functools import wraps

logger = logging.getLogger(__name__)


def timelog(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        before = time.perf_counter()
        try:
            result = method(*args, **kwargs)
        finally:
            after = time.perf_counter()
            logger.debug('Timed %s (%s, %s): %.2f s',
                         method.__name__, args, kwargs, after - before)
        return result

    return wrapper


def proflog(sort_args=['cumulative'], print_args=[10]):
    profiler = Profile()

    def decorator(method):
        @wraps(method)
        def wrapper(*args, **kwargs):
            try:
                result = profiler.runcall(method, *args, **kwargs)
            finally:
                s = io.StringIO()
                stats = pstats.Stats(profiler, stream=s)
                stats.strip_dirs().sort_stats(*sort_args).\
                    print_stats(*print_args)
                logger.debug('Profiled %s (%s, %s): %s',
                             method.__name__, args, kwargs, s.getvalue())
            return result
        return wrapper
    return decorator
