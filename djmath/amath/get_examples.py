from functools import partial
from random import randint


def __generate_k_examples(k: int = 5, min: int = 1, max: int = 11) -> None:
    """generates equations for basic addition problems and its answer

    Args:
        k (int, optional): how many equations. Defaults to 5.
        min (int, optional): starting from min. Defaults to 1.
        max (int, optional): ending with max. Defaults to 11.

    Yields:
        (str, int): str: equation, int: answer
    """
    if min > max:
        min, max = max, min
    if k > ((abs(max - min) + 1) ** 2):
        k = ((abs(max - min) + 1) ** 2)
    if k < 1:
        k = 1

    result = set()

    while len(result) < k:
        i, j = (randint(min, max) for _ in range(2))
        if (i, j) in result:
            continue
        result.add((i, j))
        yield ("".join(f"{i} + {j} = "), i + j)
    return


get_k_examples = __generate_k_examples
