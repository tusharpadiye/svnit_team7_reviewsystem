from django.shortcuts import render

def login(requests):
    return render(requests,'login.html')
def reg(requests):
    return render(requests,'signup.html')