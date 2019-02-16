__all__ = ["BASE_STRUCTURES"]

base = {
    "glider": set(((2, 2), (1, 2), (0, 2), (2, 1), (1, 0))),
    "block": set(((0, 0), (0, 1), (1, 0), (1, 1))),
    "blinker": set(((1, 0), (1, 1), (1, 2))),
}

BASE_STRUCTURES = {**base}
