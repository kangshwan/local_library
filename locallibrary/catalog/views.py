from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    # models에서 BookInstance안에 status를 만들어놨음! 그것에 대한 값을 비교하는것. m, a, o, r
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic
class BookListView(generic.ListView):
    model = Book
    # context_object_name = 'book_list'
    # queryset = Book.objects.all()
    # template_name = 'book_list.html'
    # model = Book을 하면 위 세개를 한것과 같음. 위 세개를 바꾸고싶다면 충분히 바꿀 수 있음
    paginate_by = 10
class BookDetailView(generic.DetailView):
    model = Book
    from django.shortcuts import get_object_or_404

    def book_detail_view(request, primary_key):
        book = get_object_or_404(Book, pk=primary_key)
        return render(request, 'catalog/book_detail.html', context={'book': book})
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10
class AuthorDetailView(generic.DetailView):
    model = Author
