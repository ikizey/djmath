"""
import get_k_examples from <this>

function returns list of tuples with basic addition equations and its answer
equation part is str answer is int

return example with k==2: [('7 + 1 = ', 8), ('3 + 8 = ', 11)]
"""
from random import sample
from functools import partial

# generates list of all combinations of addition from 1+1 to 11+11
# format: [("1 + 1 = ", 2), ...]
__ALL_EXAMPLES = [("".join(f"{i} + {j} = "), i+j)
                  for i in range(1, 12)
                  for j in range(1, 12)]


def __get_k_examples(examples: list, k: int) -> list:
    """
    Returns k random examples from list of examples
    """
    return sample(examples, k=k)


# returns k random examples from __ALL_EXAMPLES
get_k_examples = partial(__get_k_examples, __ALL_EXAMPLES)


# print(get_k_examples(5))
# print(get_k_examples(5))
# print(get_k_examples(5))
# print(get_k_examples(5))
