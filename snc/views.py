from django.shortcuts import render
from django.http import JsonResponse

import snc.service as service
import snc.service_geojson as service_geojson
import snc.service_download as service_download
import snc.repository as repo
from snc.const import *
from snc.chart import *
from snc.models import *



def index(request):
    context = service.get_index_context()
    return render(request, 'snc/index.html', context)


def charts_file(request):
    context = service.get_charts_geojson_file_context(SNC_GEOJSON_FILE)
    return render(request, 'snc/charts.html', context)


def download_catalogue_latest(request):
    u = ''
    p = ''
    check_list = ''
    data = {}
    if request.method == 'POST':
        u = request.POST.get('u')
        p = request.POST.get('p')

    if u == '' or p == '':
        check_list = service_download.check_catalogue_file()
    elif u != '' and p != '':
        check_list = service_download.download_catalogue_and_check(u,p)

    if len(check_list) == 4:
        data['check'] = check_list[0]
        data['catalogue_number'] = check_list[1]
        data['catalogue_date'] = check_list[2]
        data['catalogue_lines'] = check_list[3]
    else:
        data['check'] = ''
    return JsonResponse(data, safe=False)

# ------------------- CHS -------------------------------------

# loads chs charts polygons on to single map.Data layer
def chs(request):
    ctx = {}
    map_context = {}
    context = service.get_chs_index_context()
    if request.method == 'GET':
        ctx = service.get_charts_geojson_scale_range_all_split_scales_db_context(SCALE_ALL_TEXT)

    if request.method == 'POST':
        zoom = request.POST['zoom']
        centre = request.POST['centre']
        map_context = {'map_zoom': zoom, 'map_centre': centre} #, 'map_bounds': bounds}

        context = service.get_charts_geojson_scale_range_all_split_scales_db_context(SCALE_ALL_TEXT)
        ctx = {**context, **map_context}

    return render(request, 'snc/chs.html', ctx)


def charts_chs_file(request):
    context = service.get_charts_chs_geojson_file_split_scale_context(CHS_GEOJSON_FILE)
    return render(request, 'snc/chs.html', context)

# ------------------------------------------------------------

# loads main charts polygons on to multiple map.Data layers
def charts(request):
    ctx = {}
    map_context = {}
    context = service.get_info_context()
    if request.method == 'GET':
        context = service.get_charts_geojson_scale_range_all_split_scales_db_context(SCALE_ALL_TEXT)

    if request.method == 'POST':
        zoom = request.POST['zoom']
        centre = request.POST['centre']
        map_context = {'map_zoom': zoom, 'map_centre': centre} #, 'map_bounds': bounds}

        context = service.get_charts_geojson_scale_range_all_split_scales_db_context(SCALE_ALL_TEXT)

    ctx = {**context, **map_context}
    return render(request, 'snc/charts.html', ctx)


# # loads main charts polygon on to a single map.Data layer
def charts2(request):
    ctx = {}
    map_context = {}
    context = service.get_info_context()
    if request.method == 'GET':
        context = service.get_charts_geojson_scale_range_single_db_context(SCALE_ALL_TEXT)

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


def chartgeojson(request):
    geojson = ''
    data = {'chart': ''}
    if request.method == 'GET':
        chart_number = request.GET.get('chart_number')
        geojson = service_geojson.generate_geojson_single_chart(chart_number)

    data['chart'] = geojson
    return JsonResponse(data, safe=False)


# not used
def chartgeojson8XXX(request):
    geojson = ''
    data = {'chart': ''}
    if request.method == 'GET':
        geojson = repo.find_geojson_scale_range_8XXX()

    data['charts'] = geojson
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







