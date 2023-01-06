from django.shortcuts import render

# Create your views here.
def user_client(name: str):
    return f"Client {name} number 1"

def user_supplier(name: str):
    return f"Supplier {name} number 1"