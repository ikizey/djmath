from django.shortcuts import render

from amath.get_examples import generate_k_examples


def home(request):

    context = {
        "tests": list(generate_k_examples(10))
    }
    return render(request, "amath/index.html", context=context)
