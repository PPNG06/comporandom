from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, View
from .models import Character, Vehicle, Tire, Glider, Compo
import random
# Create your views here.

class home_page(TemplateView):
    template_name = "home_page.html"

def list_compo(request):
    choices1 = ['(Orange)','(Rose)','(Blue)','(White)','(Yellow)','(Rose)','(Black)','(Cyan)',]
    choices2 = ['(B)','(G)']
    char_num = random.randint(1,41)
    vehicle_num = random.randint(1,41)
    tire_num = random.randint(1,22)
    glider_num = random.randint(1,15)
    char = Character.objects.get(index=char_num)
    if "Yoshi" in char.name:
        x = random.randint(0,7)
        charname = char.name + f" {choices1[x]}"
        print(charname)
        char = Character.objects.get(name = charname)
        print(f"Got a {char.name}")
    elif "Shyguy" in char.name:
        x = random.randint(0,7)
        charname = char.name + f" {choices1[x]}"
        print(charname)
        char = Character.objects.get(name = charname)
        print(f"Got a {char.name}")
    elif "Inkling" in char.name:
        x = random.randint(0,1)
        charname = char.name[0:7] + f" {choices2[x]}"
        print(charname)
        char = Character.objects.get(name = charname)
        print(f"Got a {char.name}")
    elif "Villager" in char.name:
        x = random.randint(0,1)
        charname = char.name[0:8] + f" {choices2[x]}"
        print(charname)
        char = Character.objects.get(name = charname)
        print(f"Got a {char.name}")
    vehicle = Vehicle.objects.get(index=vehicle_num)
    tire = Tire.objects.get(index=tire_num)
    glider = Glider.objects.get(index=glider_num)

    compo = Compo.objects.get_or_create(char=char, veh=vehicle, tire=tire, glider=glider)[0]
    context = {'compo':compo}
    return render(request,'home_page.html',context)

def another_one(request):
    choices1 = ['(Orange)','(Rose)','(Blue)','(White)','(Yellow)','(Rose)','(Black)','(Cyan)',]
    choices2 = ['(B)','(G)']
    char_num = random.randint(1,41)
    vehicle_num = random.randint(1,41)
    tire_num = random.randint(1,22)
    glider_num = random.randint(1,15)
    char = Character.objects.get(index=char_num)
    if "Yoshi" in char.name:
        x = random.randint(0,7)
        charname = char.name + f" {choices1[x]}"
        print(charname)
        char = Character.objects.get(name = charname)
        print(f"Got a {char.name}")
    elif "Shyguy" in char.name:
        x = random.randint(0,7)
        charname = char.name + f" {choices1[x]}"
        print(charname)
        char = Character.objects.get(name = charname)
        print(f"Got a {char.name}")
    elif "Inkling" in char.name:
        x = random.randint(0,1)
        charname = char.name[0:7] + f" {choices2[x]}"
        print(charname)
        char = Character.objects.get(name = charname)
        print(f"Got a {char.name}")
    elif "Villager" in char.name:
        x = random.randint(0,1)
        charname = char.name[0:8] + f" {choices2[x]}"
        print(charname)
        char = Character.objects.get(name = charname)
        print(f"Got a {char.name}")
    vehicle = Vehicle.objects.get(index=vehicle_num)
    tire = Tire.objects.get(index=tire_num)
    glider = Glider.objects.get(index=glider_num)

    compo = Compo.objects.get_or_create(char=char, veh=vehicle, tire=tire, glider=glider)[0]
    context = {'compo':compo}
    return render(request,'another_one.html',context)
