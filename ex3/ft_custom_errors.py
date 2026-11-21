class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant_health(message: str) -> None:
    raise PlantError(message)


def check_water_supply(message: str) -> None:
    raise WaterError(message)


def test_custom_errors() -> None:
    plant_message = "The tomato plant is wilting!"
    water_message = "Not enough water in the tank!"

    print("Testing PlantError...")
    try:
        check_plant_health(plant_message)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        check_water_supply(water_message)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    for check, message in ((check_plant_health, plant_message),
                           (check_water_supply, water_message)):
        try:
            check(message)
        except GardenError as e:
            print(f"Caught GardenError: {e}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()

    test_custom_errors()
    print()

    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
