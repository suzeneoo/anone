from django.shortcuts import render

# Create your views here.

def board(request):
    if request.method == "GET":
        context = {
            "title":"안녕 베어유?"
        }
        return render(request, 'page/index.html', context=context)