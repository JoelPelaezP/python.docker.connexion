import multiprocessing
import os
import platform
import pwd
import threading

from connexion import FlaskApp
from gunicorn.app.base import BaseApplication


class GunicornWrapper(BaseApplication):
    def __init__(self, app: FlaskApp, port: int):
        workers = (multiprocessing.cpu_count() * 2) + 1
        threads = 4
        self.options = {
            "bind": "%s:%s" % ("0.0.0.0", port),
            "workers": workers,
            "threads": threads,
            "worker_class": "uvicorn.workers.UvicornWorker",
            "log-level": "info",
            "keep-alive": 65,
            "post_request": post_request_hook,
        }
        print(f"App with workers {workers} and threads {threads}")

        self.application = app
        super().__init__()
        # elf.cfg.set("errorlog", None)

    def load_config(self):
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }

        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self) -> FlaskApp:
        print(
            f"starting worker: hostname {platform.node()}, pid {os.getpid()}, user {os.getuid()}({pwd.getpwuid(os.getuid()).pw_name})"
        )
        return self.application


post_request_hook_lock = threading.Lock()
total_request_count = 0


def post_request_hook(_worker, _request, _environ, _resp):
    global total_request_count
    with post_request_hook_lock:
        total_request_count += 1
        request_count = total_request_count

    if (request_count % 1000) == 0:
        _threads = " ".join(thr.name for thr in threading.enumerate())
        print(
            f"worker status: pid {os.getpid()}, request count {total_request_count}, threads {threading.active_count()} ({_threads})"
        )
