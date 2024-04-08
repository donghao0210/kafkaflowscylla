from config import DEBUG
import time

def debug_print(*args):
    if DEBUG:
        message = " ".join(map(str, args))
        print("[DEBUG]", message , "[",time.ctime(time.time()),"]")

def debug_assert(condition, message):
    if DEBUG and not condition:
        raise AssertionError("[DEBUG ASSERTION FAILED] " + message)