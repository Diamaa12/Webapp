from django.shortcuts import render, redirect
from GestionUser.gestion_users import get_all_users, User

# Create your views here.
def index(requests):
    return render(requests, "mycontacts/index.html", {"users":get_all_users()})
def add_contact(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    adress = request.POST.get("address")
    p_number = request.POST.get("tel_number")

    user = User(first_name=first_name, last_name=last_name, address=adress, phone_number=p_number)
    user.data_save(validate=True)
    return redirect("index")
def del_user(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    user = User(first_name, last_name)
    user.delete_user(first_name, last_name)
    return redirect("index")
