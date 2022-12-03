from difflib import context_diff
from django.shortcuts import (
    render,
    HttpResponse,
)
from django.http.request import HttpRequest



def index(request:HttpRequest) -> HttpRequest:
    """index view."""
    numbers: list[int] = []
    i: int

    for i in range(1, 11):
        numbers.append(i)

    context_data: dict[str, str | int ] = {
        'ctx_title': 'Заголовок главной страницы',
        'ctx_numbers': numbers
    }
    return render(
        request,
        template_name='main/index.html',
        context = context_data
)
