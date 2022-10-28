# Mireole#8364
import unittest

return_values = []


def input_mock(*args, **kwargs):
    return return_values.pop(0)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
