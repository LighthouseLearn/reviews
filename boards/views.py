from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Board, Company, Review
from django.conf import settings
from users.models import CustomUser
from .forms import NewCompanyForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.views.generic import UpdateView
from django.utils import timezone
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required, name='dispatch')
class ReviewUpdateView(UpdateView):
    model = Review
    fields = ('address', 'length_of_stay', 'move_in_condition', 'treatment', 'response_speed', 'maintenance_quality', 'security_deposit_returned', 'is_this_a_fair_amount', 'would_you_recommend', 'additional_comments')
    template_name = 'edit_review.html'
    pk_url_kwarg = 'review_pk'
    context_object_name = 'review'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

    def form_valid(self, form):
        review = form.save(commit=False)
        review.updated_by = self.request.user
        review.updated_at = timezone.now()
        review.save()  
        return redirect('company_reviews', pk=review.company.board.pk, company_pk=review.company.pk)   

def boardhome(request):
    boards = Board.objects.all()
    return render(request, 'boardhome.html', {'boards': boards})

def board_companies(request, pk):
    board = get_object_or_404(Board, pk=pk)
    companies = board.companies.order_by('-last_updated') .annotate(replies=Count('reviews'))
    return render(request, 'companies.html', {'board': board, 'companies': companies})

def company_reviews(request, pk, company_pk):
    company = get_object_or_404(Company, board__pk=pk, pk=company_pk)
    company.views += 1
    company.save()
    return render(request, 'company_reviews.html', {'company': company})

@login_required
def add_review_company(request, pk, company_pk):
    company = get_object_or_404(Company, board__pk=pk, pk=company_pk)
    if request.method =='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.company = company
            review.created_by = request.user
            review.save()
            return redirect('company_reviews', pk=pk, company_pk=company_pk)
    else:
        form = ReviewForm()
    return render(request, 'add_review_company.html', {'company': company, 'form': form})


@login_required
def new_company(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = CustomUser.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewCompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.board = board
            company.starter = request.user
            company.save()
            return redirect('company_reviews', pk=pk, company_pk=company.pk)#need to redirect this to company detail
    else:
        form = NewCompanyForm()  # TODO: redirect to the created topic page
    return render(request, 'new_company.html', {'board': board, 'form': form})