from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers

# Create your views here.
from django.http import HttpResponse
from django.http.response import JsonResponse

from web import models

def hello(request):
    # return HttpResponse("hello world!")
    context = {}
    # 数据绑定
    context['hello'] = 'Hello world!'
    # 将绑定的数据传入前台
    return render(request, 'hello.html', context)

@csrf_exempt
def index(request):
    if request.method == 'POST':
        pass

    else:
        xmu_news_list = models.News.objects.order_by('-release_time').all()
        jwc_news_list = models.jwc_News.objects.order_by('-release_time').all()
        xsc_news_list = models.xsc_News.objects.order_by('-release_time').all()
        xmu_news_paginator = Paginator(xmu_news_list, 10) #show 20 news per page
        jwc_news_paginator = Paginator(jwc_news_list, 10)
        xsc_news_paginator = Paginator(xsc_news_list, 10)
        # print("p.count:"+str(paginator.count))
        # print("p.num_pages:"+str(paginator.num_pages))
        # print("p.page_range:"+str(paginator.page_range))

        source = request.GET.get("source")
        page = request.GET.get('page')
        xmu_news = xmu_news_paginator.get_page(1)
        jwc_news = jwc_news_paginator.get_page(1)
        xsc_news = xsc_news_paginator.get_page(1)
        if(source == 'xmu'):
            xmu_news = xmu_news_paginator.get_page(page)
        elif(source == 'jwc'):
            jwc_news = jwc_news_paginator.get_page(page)
        elif (source == 'xsc'):
            xsc_news = xsc_news_paginator.get_page(page)

        # print("p.number:"+str(news.number))
        return render(request, 'index.html', {'li':xmu_news, 'jwc_li':jwc_news, 'xsc_li': xsc_news})

@csrf_exempt
def get_page(request):
    if request.method == 'GET':
        source = request.GET.get('source')

        num_page = request.GET.get('page')
        all_news_list = models.News.objects.order_by('-release_time').all()
        paginator = Paginator(all_news_list, 20)  # show 20 news per page
        # print("p.count:"+str(paginator.count))
        # print("p.num_pages:"+str(paginator.num_pages))
        # print("p.page_range:"+str(paginator.page_range))
        # page = request.GET.get('page')
        news = paginator.get_page(num_page)

        return HttpResponse()

@csrf_exempt
def get_detail(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        source = request.POST.get("source")
        print("source: {0}, news_id: {1}".format(source, str(id)))

        # 此处用get会报错，用filter比较方便
        if (source == 'xmu'):
            item = models.News.objects.filter(id=id)
            models.News.objects.filter(id=id).update(read_status=2)
        elif (source == 'jwc'):
            item = models.jwc_News.objects.filter(id=id)
            models.jwc_News.objects.filter(id=id).update(read_status=2)
        elif (source == 'xsc'):
            item = models.xsc_News.objects.filter(id=id)
            models.xsc_News.objects.filter(id=id).update(read_status=2)

        item = item
        # print(item)
        # print(item[0])
        #
        json_item = serializers.serialize("json", item)
        # print(json_item)
        #
        json_item = json.loads(json_item)

        print("Data from get_detail(). 数据从get_detail()获取")

        return JsonResponse(json_item[0]['fields'], safe=False)
