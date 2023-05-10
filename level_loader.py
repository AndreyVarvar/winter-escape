import json


def load_level(level_n):
    with open(f"assets/levels/level {level_n}.json", "r") as file:
        level = json.loads("".join(file.readlines()))

    return level
