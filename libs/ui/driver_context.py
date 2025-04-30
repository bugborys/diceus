import threading

_driver_storage = threading.local()

def set_driver(driver):
    _driver_storage.driver = driver

def get_driver():
    return getattr(_driver_storage, "driver", None)

def clear_driver():
    _driver_storage.driver = None