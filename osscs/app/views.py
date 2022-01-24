from django.shortcuts import render, redirect
from app.form import SearchForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SearchForm(data=request.POST)
        query = form.data.get('query')
        return redirect('/app/search/?query={}'.format(query))
    form = SearchForm()
    return render(request, 'index.html', {
        'form': form
    })


def search(request):
    query = request.GET.get('query')
    return render(request, 'app/search.html', {
        'query': query
    })
