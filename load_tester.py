import time
import os
import json
import requests


def get_ones(url: str, session, model: str, iter: int):
    print("\n==============================\nStart get objects one by one\n")
    avg = 0
    for i in range(iter):
        start_time = time.time()
        response = session.get(f"{url}{model}/")
        if response.status_code != 200:
            return
        latency = time.time() - start_time
        avg += latency
        print(f"{i} : {latency} ms")

    avg //= iter
    print("\nAvg latency : " + str(avg) + " ms")
    return avg


def get_all(url: str, session, model: str):
    print("\n==============================\nStart get all objects\n")
    start_time = time.time()
    response = session.get(f"{url}{model}/")
    latency = time.time() - start_time
    print("Latency : " + str(latency) + " ms")

    return latency


def create_many(url: str, session, model: str, headers: dict, iter: int):
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
            f"{url}{model}/",
            headers=headers,
            data=json.dumps(data),
        )
        if response.status_code not in (200, 201):
            return
        latency = time.time() - start_time
        avg += latency
        print(f"{i} : {latency} ms")

    avg //= iter
    print("\nAvg latency : " + str(avg) + " ms")
    return avg


def delete_all(url: str, session, model: str, headers: dict):
    print("\n==============================\nStart delete all objects\n")
    start_time = time.time()
    response = session.delete(f"{url}{model}/", headers=headers)
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

    url = "http://127.0.0.1:8000/"
    iter = int(os.environ["ITER"])
    session = requests.Session()

    response = session.get(url + "admin")
    csrf_token = response.headers["Set-Cookie"][10:74]

    url += "testapp/"
    headers = {
        "Content-Type": "application/json",
        "X-CSRFToken": csrf_token,
    }

    all_time = time.time()
    function_start = all_time
    c_avg = create_many(url, session, model, headers, iter)
    print("create_many takes : " + str(time.time() - function_start) + " ms")

    function_start = time.time()
    g_avg = get_ones(url, session, model, iter)
    print("get one takes : " + str(time.time() - function_start) + " ms")

    function_start = time.time()
    g_lat = get_all(url, session, model)
    print("get all takes : " + str(time.time() - function_start) + " ms")

    function_start = time.time()
    d_lat = delete_all(url, session, model, headers)
    print("delete all takes : " + str(time.time() - function_start) + " ms")

    print("\n-----------------------------")
    print("Create avg : " + str(c_avg) + " ms")
    print("Get ones avg : " + str(g_avg) + " ms")
    print("Get all avg : " + str(g_lat) + " ms")
    print("Delete all takes : " + str(d_lat) + " ms")
    print("Total latency : " + str(time.time() - all_time) + " ms")
