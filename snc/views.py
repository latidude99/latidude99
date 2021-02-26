from django.shortcuts import render

import snc.service as service



def index(request):
    context = service.get_index_context()
    return render(request, 'snc/index.html', context)


def admin(request):
    context = service.get_index_context()
    return render(request, 'snc/index.html', context)















