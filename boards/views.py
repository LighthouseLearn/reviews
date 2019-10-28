from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Board, Company, Review
from django.conf import settings
from users.models import CustomUser
from .forms import NewCompanyForm
# Create your views here.

def boardhome(request):
    boards = Board.objects.all()
    return render(request, 'boardhome.html', {'boards': boards})

def board_companies(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'companies.html', {'board': board})

def new_company(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = CustomUser.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewCompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.board = board
            company.starter = user
            company.save()
            review = Review.objects.create(
                additional_comments=form.cleaned_data.get('additional_comments'),
                company=company,
                created_by=user,
                address=address,
                move_in_condition=move_in_condition,
            )
   #     name = request.POST['name']
    #    address = request.POST['address']
     #  additional_comments = request.POST['additional_comments']

     #   company = Company.objects.create(
      #      name=name,
       #     board=board,
        #    starter=user
       # )

       # review = Review.objects.create(
        #    address=address,
         #   company=company,
          #  additional_comments=additional_comments,
           # created_by=user
        #)

        return redirect('board_companies', pk=board.pk)
    else:
        form = NewCompanyForm()  # TODO: redirect to the created topic page
    return render(request, 'new_company.html', {'board': board, 'form': form})