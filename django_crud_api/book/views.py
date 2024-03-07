from django.shortcuts import render
from .models import Book
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import BookForm
from django.db.models import Q
# Create your views here.

def create_book(request):
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
				form.save()
				return redirect('books_app:books')  # Reemplaza 'book_list' con el nombre de tu vista de lista de libros
	else:
			form = BookForm()
	return render(request, 'books/new-book.html', {'form': form})



def book_list_view(request):
	template_name="books/books.html"
	if request.GET.get("datatables"):
		draw = int(request.GET.get("draw", "1"))
		length = int(request.GET.get("length", "10"))
		start = int(request.GET.get("start", "0"))
		sv = request.GET.get("search[value]", None)
		qs = Book.objects.order_by("id")
		if sv:
				# Dividir el término de búsqueda por espacios
				search_terms = sv.split()
				# Crear una lista de Q objects para buscar en los campos de autor
				author_q_objects = Q()
				for term in search_terms:
						author_q_objects |= Q(author__first_name__icontains=term) | Q(author__last_name__icontains=term)
				qs = qs.filter(
						Q(title__icontains=sv)
						| Q(isbn__icontains=sv)
						| Q(genre__icontains=sv)
						| Q(synopsis__icontains=sv)
						| author_q_objects
				)
		filtered_count = qs.count()
		qs = qs[start : start + length]

		data = []
		for book in qs:
			data.append({
					'title': book.title,
					'author': f"{book.author.first_name} {book.author.last_name}",
					'isbn': book.isbn,
					'genre': book.genre,
					'synopsis': book.synopsis,
			})

		return JsonResponse(
				{
						"recordsTotal": Book.objects.count(),
						"recordsFiltered": filtered_count,
						"draw": draw,
						"data": data,
				},
				safe=False,
		)
	else:
		context = {}  # Aquí puedes agregar cualquier contexto necesario
		return render(request, template_name, context)
