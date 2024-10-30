from timeout_decorator.timeout import TimeoutException, timeout


def main():

    @timeout(3)
    def fn_in_time():
        print("I'm in time!")

    @timeout(5)
    def long_running_function():
        import time
        print("Starting a long task...")
        time.sleep(10)  # Simulate a long-running process
        print("Task completed.")

    try:
        fn_in_time()
        long_running_function()
    except TimeoutException as e:
        print(e)


if __name__ == "__main__":
    main()
