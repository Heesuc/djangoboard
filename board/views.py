from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from board.models import Board
from rest_framework.response import Response
from rest_framework.decorators import api_view
from serializers import BoardSerializer

def home(request):
    return render(request, 'home.html')

def board(request):
    rsBoard = Board.objects.all()
    return render(request, 'board_list.html', {'rsBoard': rsBoard})

def board_write(request):
    return render(request, 'board_write.html')

def board_insert(request):
    b_title = request.GET.get('b_title')
    b_note = request.GET.get('b_note')
    b_writer = request.GET.get('b_writer')
    
    if b_title and b_note and b_writer:
        row = Board.objects.create(b_title=b_title, b_note=b_note, b_writer=b_writer)
        return redirect('/board')
    else:
        board_data = {'b_title': b_title, 'b_note': b_note, 'b_writer': b_writer}
        return render(request, 'board_write.html', board_data)
    
def board_view(request):
    b_no = request.GET['b_no']
    rsDetail = Board.objects.get(b_no=b_no)
    return render(request, "board_view.html", {'rsDetail' : rsDetail})

def board_edit(request):
    b_no = request.GET['b_no']
    b_title = request.GET.get('b_title')
    b_note = request.GET.get('b_note')
    b_writer = request.GET.get('b_writer')
    
    rsDetail = Board.objects.get(b_no=b_no)
    if b_title:
        rsDetail.b_title = b_title
    if b_note:
        rsDetail.b_note = b_note
    if b_writer:
        rsDetail.b_writer = b_writer

    try:
        rsDetail.save()
        return render(request, "board_view.html", {'rsDetail' : rsDetail})
    except ValueError:
        return render(request, "board_update.html", {'rsDetail' : rsDetail})

def board_update(request):
    b_no = request.GET['b_no']
    rsDetail = Board.objects.get(b_no=b_no)
    return render(request, "board_update.html", {'rsDetail' : rsDetail})

def board_delete(request):
    b_no = request.GET['b_no']
    Board.objects.get(b_no=b_no).delete()
    return redirect('/board')

def viewjson(Request):
    return JsonResponse("REST API end point", safe=False)

@api_view(['GET'])
def index(request):
    api_urls = {
        'List' : '/boardlist/',
        'Detail' : '/board_view/<str:pk>/',
        'Create' : '/board_insert/',
        'Update' : '/board_edit/<str:pk>/',
        'Delete' : '/board_delete/<str:pk>/',
    }

    return Response(api_urls)