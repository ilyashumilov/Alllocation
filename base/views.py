from django.shortcuts import render, redirect
from .forms import allocateform
from .models import order, client

import json

# Create your views here.

def Allocate(request):
    clients = client.objects.values_list('firstname', flat = True)
    clients = list(clients)
    clients = json.dumps(clients)
    client1 = ''
    type = ''
    weight = ''
    form = allocateform()

    if request.method == 'POST':
        form = allocateform(request.POST)
        if form.is_valid():
            client1 = form.cleaned_data['client']
            type = form.cleaned_data['type']
            weight = form.cleaned_data['weight']
        item = client.objects.get(firstname=client1)
        order1 = order(client = item, type = type, weight = weight)
        order1.save()

        return redirect('Allocate')

    context = {
        'form':form,
        'clients':clients
    }
    return render(request,'Allocate.html',context)