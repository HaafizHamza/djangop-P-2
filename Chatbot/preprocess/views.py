from django.http import HttpResponse,HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

def index(request):
    return HttpResponse("This is first page of our bot site")


@csrf_exempt
@require_http_methods(['GET'])
def detail(request):
    if request.method=='GET':
        return HttpResponse("This is dtail page of our bot site")
    elif request.method=='POST':
        return HttpResponseNotFound("Post is not allowed")