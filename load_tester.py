import time
import os
import json
import requests


def get_ones(session, model: str, iter: int):
    print("\nStart get objects one by one\n==============================\n")
    avg = 0
    for i in range(iter):
        start_time = time.time()
        response = session.get(f"http://127.0.0.1:9009/testapp/{model}/")
        if response.status_code != 200:
            return
        latency = time.time() - start_time
        avg += latency
        print(f"{i} : {latency} ms")

    avg //= iter
    print("\nAvg latency : " + str(avg) + " ms")
    return avg


def get_all(session, model: str):
    print("\n==============================\nStart get all objects\nn")
    start_time = time.time()
    response = session.get(f"http://127.0.0.1:9009/testapp/{model}/")
    latency = time.time() - start_time
    print("Latency : " + str(latency) + " ms")

    return latency


def create_many(session, model: str, headers: dict, iter: int):
    print("\n==============================\nStart create many objects\n")
    avg = 0
    for i in range(iter):
        data = {
            "title": str(i),
            "author": "Anonymous",
            "volume": str(i),
        }
        start_time = time.time()
        response = session.post(
            f"http://127.0.0.1:9009/testapp/{model}/",
            headers=headers,
            data=json.dumps(data),
        )
        if response.status_code != 201:
            return
        latency = time.time() - start_time
        avg += latency
        print(f"{i} : {latency} ms")

    avg //= iter
    print("\nAvg latency : " + str(avg) + " ms")
    return avg


def delete_all(session, model: str, headers: dict):
    print("\n==============================\nStart delete all objects\n")
    start_time = time.time()
    response = session.delete(
        f"http://127.0.0.1:9009/testapp/{model}/", headers=headers
    )
    latency = time.time() - start_time
    print("Latency : " + str(latency) + " ms")

    return latency


if __name__ == "__main__":
    TEST_ENV = os.environ["TEST_ENV"]
    if TEST_ENV == "sync":
        model = "books"
    elif TEST_ENV == "async":
        model = "async-books"
    else:
        print("Wrong ENV !!")
        exit()

    iter = 1

    session = requests.Session()

    response = session.get("http://127.0.0.1:9009/admin")
    csrf_token = response.headers["Set-Cookie"][10:74]
    print(csrf_token)

    headers = {
        "Content-Type": "application/json",
        "X-CSRFToken": csrf_token,
    }

    all_time = time.time()
    function_start = all_time
    c_avg = create_many(session, model, headers, iter)
    print("create_many takes : " + str(time.time() - function_start) + " ms")

    function_start = time.time()
    g_avg = get_ones(session, model, iter)
    print("get one takes : " + str(time.time() - function_start) + " ms")

    function_start = time.time()
    g_lat = get_all(session, model)
    print("get all takes : " + str(time.time() - function_start) + " ms")

    function_start = time.time()
    d_lat = delete_all(session, model, headers)
    print("delete all takes : " + str(time.time() - function_start) + " ms")

    print("\n-----------------------------")
    print("Create avg : " + str(c_avg) + " ms")
    print("Get ones avg : " + str(g_avg) + " ms")
    print("Get all avg : " + str(g_lat) + " ms")
    print("Delete all takes : " + str(d_lat) + " ms")
    print("Total latency : " + str(time.time() - all_time) + " ms")
