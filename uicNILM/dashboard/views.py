from django.shortcuts import render


def index(request):
    context = dict()
    return render(request, 'dashboard-index.html', context)


def visualization_index(request):
    context = dict()
    return render(request, 'dashboard-index.html', context)
