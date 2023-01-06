from django.shortcuts import render

# Create your views here.
def user_client(name: str):
    return f"Client {name} number 1"