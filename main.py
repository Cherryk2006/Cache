import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Номер числа Фібоначчі повинен бути невід'ємним")
    if r.get(str(n)) is None:
        if n <= 1:
            r.set(str(n), n)
        else:
            r.set(str(n), fibonacci(n - 1) + fibonacci(n - 2))
    return int(r.get(str(n)))

if __name__ == "__main__":
    print(fibonacci(100))
    print(fibonacci(153))