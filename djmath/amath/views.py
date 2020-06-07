from django.shortcuts import render
from django.http import HttpResponse
from .get_examples import get_k_examples


def home(request):
    # tests = list()
    # answers = list()
    # for t in get_k_examples(5):
    #     tests.append(t[0])
    #     answers.append(t[1])
    context = {
        "tests": get_k_examples(5)
    }
    return render(request, "amath/index.html", context=context)
