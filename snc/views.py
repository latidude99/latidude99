from django.shortcuts import render
from django.http import JsonResponse

import snc.service as service
from snc.const import *
from snc.chart import *
from snc.models import *



def index(request):
    context = service.get_index_context()
    return render(request, 'snc/index.html', context)


def charts_file(request):
    context = service.get_charts_geojson_file_context(SNC_GEOJSON_FILE)
    return render(request, 'snc/charts.html', context)

# loads main charts polygon on to map.Data layers
def charts(request):
    ctx = {}
    map_context = {}
    context = service.get_info_context()
    if request.method == 'GET':
        context = service.get_charts_geojson_scale_range_all_split_scales_db_context(SCALE_ALL_TEXT)

    if request.method == 'POST':
        scales = request.POST.getlist('scale')
        zoom = request.POST['zoom']
        centre = request.POST['centre']
        # bounds = request.POST['bounds']
        map_context = {'map_zoom': zoom, 'map_centre': centre} #, 'map_bounds': bounds}

        if len(scales) < 1:
            context = service.get_index_context()
            return render(request, 'snc/index.html', context)
        context = service.get_charts_geojson_scale_range_multiple_db_context(scales)

    ctx = {**context, **map_context}
    return render(request, 'snc/charts.html', ctx)


def chartdetails(request):
    chartJSON = ''
    data = {'chart': ''}
    if request.method == 'GET':
        chart_number = request.GET.get('chart_number')
        chartDTO = service.get_single_context(chart_number)
        chartJSON = service.chartDTO_2_chartJSON(chartDTO)

    data['chart'] = chartJSON
    return JsonResponse(data, safe=False)


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
        data.capitalize()
    if ',' in data:
        nums = data.split(',')
        nums = [x.strip() for x in nums]
    elif '-' in data:
        limits = data.split('-')
        limits = [x.strip() for x in limits]
        try:
            first = int(limits[0])
            second = int(limits[1])
            if first < second:
                nums = list(range(first, second))
            else:
                nums = list(range(second, first))
        except:
            pass
    else:
        nums.append(data.strip())
    context = service.get_search_multiple_context(nums)
    return render(request, 'snc/index.html', context)


def charts_all(request):
    context = service.get_all_charts_context()
    return render(request, 'snc/index.html', context)







