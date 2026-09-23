def input_temperature(temp_str: str) -> int:
    MIN_TEMP = 0
    MAX_TEMP = 40
    temperature = int(temp_str)
    if temperature < MIN_TEMP:
        raise ValueError(f"{temperature}°C is too cold for plants "
                         f"(min {MIN_TEMP}°C)")
    if temperature > MAX_TEMP:
        raise ValueError(f"{temperature}°C is too hot for plants "
                         f"(max {MAX_TEMP}°C)")
    return temperature


def run_test(test_str: str) -> None:
    print(f"Input data is '{test_str}'")
    try:
        temperature = input_temperature(test_str)
        print(f"Temperature is now {temperature}°C\n")
    except (ValueError, TypeError) as e:
        print(f"Caught input_temperature error: {e}\n")


def test_temperature() -> None:
    run_test("25")
    run_test("abc")
    run_test("100")
    run_test("-50")


def main() -> None:
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
