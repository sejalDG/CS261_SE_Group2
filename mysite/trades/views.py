from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Trade
from .forms import AddTradeForm, EditTradeForm
from django.urls import reverse, reverse_lazy
from django.views import generic
from datetime import date, datetime
from .render import Render

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def add(request):
    if request.method == "POST":
        form = AddTradeForm(request.POST)
        if form.is_valid():
            trade = form.save(commit=False)
            trade.save()
            # return redirect('post_detail', pk=post.pk)
            return redirect('trades:daily')
    else:
        form = AddTradeForm()
    return render(request, 'trades/addtradepage.html', {'form': form})

# def daily(request):
#     return render(request, 'trades/dailytrades.html')

def delete(request):
    return render(request, 'trades/deletetrades.html')

def edit(request, trade_id):
    trade = get_object_or_404(Trade, pk=trade_id)
    if request.method == "POST":
        form = EditTradeForm(request.POST, instance=trade)
        if form.is_valid():
            trade = form.save(commit=False)
            trade.save()
            # return redirect('post_detail', pk=post.pk)
            return redirect('trades:daily')
    else:
        form = EditTradeForm(initial={
        'dateCreated': trade.dateCreated,
        'timeCreated': str(trade.timeCreated)[:-3],
        'prodInfo': trade.prodInfo,
        'buyingPartyInfo': trade.buyingPartyInfo,
        'sellingPartyInfo': trade.sellingPartyInfo,
        'notionalAmount': trade.notionalAmount,
        'quantity': trade.quantity,
        'maturityDate': trade.maturityDate,
        'underlyingAmount': trade.underlyingAmount,
        'underlyingCurrency': trade.underlyingCurrency,
        'strikePrice': trade.strikePrice})
    return render(request, 'trades/edittrades.html', {'form': form, 'trade': trade})

def archive(request):
    return render(request, 'trades/reportarchive.html')

def settings(request):
    return render(request, 'trades/settingspage.html')

class DailyView(generic.ListView):
    template_name = 'trades/dailytrades.html'
    context_object_name = 'latest_trade_list'

    def get_queryset(self):
        """Return all trades from the current day."""
        return Trade.objects.filter(dateCreated=date.today())

class TradeDelete(generic.DeleteView):
        #template_name = 'deletetrades.html'
        model = Trade
        success_url = reverse_lazy('trades:daily')

class Pdf(generic.View):

    def get(self, request):
        trades = Trade.objects.filter(dateCreated=date.today())
        today = datetime.now()
        params = {
            'today': today,
            'latest_trade_list': trades,
            'request': request
        }
        return Render.render('trades/dailytrades.html', params)


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'

#
# class AddView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice']) # Returns ID of selected choice as a string
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
