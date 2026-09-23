def input_temperature(temp_str: str) -> int:
    return int(temp_str)


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


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
