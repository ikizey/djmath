from random import randint


def generate_k_examples(k: int = 5, min: int = 1, max: int = 11):
    """generates equations for basic addition problems and its answer

    Args:
        k (int, optional): how many equations. Defaults to 5.
        min (int, optional): starting from min. Defaults to 1.
        max (int, optional): ending with max. Defaults to 11.

    Yields:
        (str, int): str: equation, int: answer
    """
    # swap min and max if set incorrect
    if min > max:
        min, max = max, min

    # k shouldn't be greater than ~difference squared
    if k > ((abs(max - min) + 1) ** 2):
        k = ((abs(max - min) + 1) ** 2)
    # or less then 1
    elif k < 1:
        k = 1

    result = set()

    while len(result) < k:
        i, j = [randint(min, max) for _ in range(2)]
        if (i, j) not in result:
            result.add((i, j))
            yield ("".join(f"{i} + {j} = "), i + j)
    return
