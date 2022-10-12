from django.shortcuts import render

def login(requests):
    return render(requests,'login.html')
