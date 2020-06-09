"""
import get_k_examples from <this>

function returns list of tuples with basic addition equations and its answer
equation part is str answer is int

return example with k==2: [('7 + 1 = ', 8), ('3 + 8 = ', 11)]
"""
from functools import partial
from random import randint


def __generate_k_examples(k: int, min: int, max: int) -> None:
    if abs(max) < abs(min):
        raise AttributeError(f"abs(min) should be <= abs(max)")
    if k > abs(max - min):
        raise AttributeError(f"k should be <= abs(max-min)")
    result = set()
    i, j = (randint(min, max) for _ in range(2))

    for _ in range(k):
        while (i, j) in result:
            i, j = (randint(min, max) for _ in range(2))
        result.add((i, j))
        yield ("".join(f"{i} + {j} = "), i + j)
    return


# sets defaults for __generate_k_examples
get_k_examples = partial(__generate_k_examples, min=1, max=11)

print(list(get_k_examples(5)))
print(list(__generate_k_examples(5, 1, 11)))
print(list(__generate_k_examples(5, 1, 11)))
print(list(__generate_k_examples(5, 1, 11)))

# OLD CODE:

# generates list of all combinations of addition from 1+1 to 11+11
# format: [("1 + 1 = ", 2), ...]
# __ALL_EXAMPLES = [("".join(f"{i} + {j} = "), i+j)
#                   for i in range(1, 12)
#                   for j in range(1, 12)]


# def __get_k_examples(examples: list, k: int) -> list:
#     """
#     Returns k random examples from list of examples
#     """
#     return sample(examples, k=k)


# print(get_k_examples(5))
# print(get_k_examples(5))
# print(get_k_examples(5))
# print(get_k_examples(5))
