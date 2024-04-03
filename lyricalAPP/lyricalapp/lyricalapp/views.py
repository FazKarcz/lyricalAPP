from django.shortcuts import render


def startingPage(request):
    return render(request, 'index.html')
