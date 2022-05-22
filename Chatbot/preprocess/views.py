from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
def index(request):
    return HttpResponse("This is first page of our bot site")


@csrf_exempt
@require_http_methods(['GET'])
def detail(request):
    items=("train","models","chat","tkinter","good","happy")
    if request.method=='GET':
        paginator= Paginator(items,2)
        pages=request.GET.get('page',1)
        try:
            items=paginator.page(pages)
        except PageNotAnInteger:
            items=paginator.page(1)
        return render(request,'preprocess/list.html',{'items':items})
    elif request.method=='POST':
        return HttpResponseNotFound("Post is not allowed")