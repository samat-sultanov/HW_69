from django.shortcuts import render


def indexview(request, *args, **kwargs):
    return render(request, 'index.html', context={})
