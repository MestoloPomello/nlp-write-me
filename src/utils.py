from datetime import datetime


def printf(*arg, **kwarg):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}]", *arg, **kwarg)
