from django.shortcuts import render

import snc.service as service



def index(request):
    context = service.get_index_context()
    return render(request, 'snc/index.html', context)


def admin(request):
    context = service.get_index_context()
    return render(request, 'snc/index.html', context)


def info(request):
    context = service.get_info_context()
    return render(request, 'snc/index.html', context)


def multisearch(request):
    nums = []
    data = ''
    if request.method == 'POST':
        data = request.POST['number']
    if ',' in data:
        nums = data.split(',')
        nums = [x.strip() for x in nums]
    elif '-' in data:
        limits = data.split('-')
        limits = [x.strip() for x in limits]
        try:
            nums = list(range(int(limits[0]), int(limits[1])))
        except:
            pass
    else:
        nums.append(data.strip())
    context = service.get_search_multiple_context(nums)
    return render(request, 'snc/index.html', context)


def charts_all(request):
    context = service.get_all_charts_context()
    return render(request, 'snc/index.html', context)


def charts_1(request):
    context = service.get_SCALE1_charts_context()
    return render(request, 'snc/index.html', context)


def charts_2(request):
    context = service.get_SCALE2_charts_context()
    return render(request, 'snc/index.html', context)


def charts_3(request):
    context = service.get_SCALE3_charts_context()
    return render(request, 'snc/index.html', context)


def charts_4(request):
    context = service.get_SCALE4_charts_context()
    return render(request, 'snc/index.html', context)


def charts_5(request):
    context = service.get_SCALE5_charts_context()
    return render(request, 'snc/index.html', context)


def charts_6(request):
    context = service.get_SCALE6_charts_context()
    return render(request, 'snc/index.html', context)


def charts_7(request):
    context = service.get_SCALE7_charts_context()
    return render(request, 'snc/index.html', context)









