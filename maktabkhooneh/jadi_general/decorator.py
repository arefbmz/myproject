import time
from functools import wraps

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Execution time of '{func.__name__}': {end - start:.6f} seconds")
        return result
    return wrapper


@measure_time
def create_list(n):
    return list(range(1, n + 1))


# Example usage
if __name__ == "__main__":
    n = 1_000_000
    result = create_list(n)
    print(f"First 5 elements: {result[:5]}")
    print(f"Last 5 elements: {result[-5:]}")
    print(f"List length: {len(result)}")