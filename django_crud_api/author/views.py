from django.shortcuts import render
from django.http import JsonResponse
from .models import Author, Item
# Create your views here.
from django.shortcuts import render, redirect
from .forms import AuthorForm

from django.db.models import Q
##########################################################################
#                            Author                                      #
##########################################################################

def create_author(request):
	if request.method == 'POST':
		form = AuthorForm(request.POST)
		if form.is_valid():
				form.save()
				return redirect('author_app:authors')  # Reemplaza 'author_list' con el nombre de tu vista de lista de autores
	else:
			form = AuthorForm()
	return render(request, 'authors/new-author.html', {'form': form})

def author_list_view(request):
	template_name = "authors/authors.html"

	if request.GET.get("datatables"):
		draw = int(request.GET.get("draw", "1"))
		length = int(request.GET.get("length", "10"))
		start = int(request.GET.get("start", "0"))
		sv = request.GET.get("search[value]", None)
		qs = Author.objects.order_by("id")
		if sv:
				qs = qs.filter(
						Q(first_name__icontains=sv)
						| Q(last_name__icontains=sv)
				)
		filtered_count = qs.count()
		qs = qs[start : start + length]

		return JsonResponse(
				{
						"recordsTotal": Author.objects.count(),
						"recordsFiltered": filtered_count,
						"draw": draw,
						"data": list(qs.values()),
				},
				safe=False,
		)
	else:
		context = {}  # Aquí puedes agregar cualquier contexto necesario
		return render(request, template_name, context)


##########################################################################
#                            Item                                        #
##########################################################################




from django.db.models import Q
from django.http import JsonResponse
from django.views.generic import ListView

class ItemListView(ListView):
	model = Item
	template_name = "authors/item_datatable.html"

	def render_to_response(self, context, **response_kwargs):
		if self.request.GET.get("datatables"):
			draw = int(self.request.GET.get("draw", "1"))
			length = int(self.request.GET.get("length", "2"))
			start = int(self.request.GET.get("start", "0"))
			sv = self.request.GET.get("search[value]", None)
			qs = self.get_queryset().order_by("id")
			if sv:
					qs = qs.filter(
							Q(name__icontains=sv)
							| Q(code__icontains=sv)
							| Q(name_en__icontains=sv)
					)
			filtered_count = qs.count()
			qs = qs[start : start + length]
			print("\n"*5)
			print("queryset",qs)
			print()
			for item in qs:
				print(item.name)
			print("\n"*5)
			return JsonResponse(
					{
							"recordsTotal": self.get_queryset().count(),
							"recordsFiltered": filtered_count,
							"draw": draw,
							"data": list(qs.values()),
					},
					safe=False,
			)
		return super().render_to_response(context, **response_kwargs)




from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from .models import Item

def item_list_view(request):
	template_name = "authors/item_datatable.html"

	if request.GET.get("datatables"):
		draw = int(request.GET.get("draw", "1"))
		length = int(request.GET.get("length", "10"))
		start = int(request.GET.get("start", "0"))
		sv = request.GET.get("search[value]", None)
		qs = Item.objects.order_by("code")
		if sv:
				qs = qs.filter(
						Q(name__icontains=sv)
						| Q(code__icontains=sv)
						| Q(name_en__icontains=sv)
				)
		filtered_count = qs.count()
		qs = qs[start : start + length]

		return JsonResponse(
				{
						"recordsTotal": Item.objects.count(),
						"recordsFiltered": filtered_count,
						"draw": draw,
						"data": list(qs.values()),
				},
				safe=False,
		)
	else:
		context = {}  # Aquí puedes agregar cualquier contexto necesario
		return render(request, template_name, context)




from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_app:items')  # Cambiar 'item-list' por el nombre correcto de la URL para la lista de ítems
    else:
        form = ItemForm()
    return render(request, 'authors/new-item.html', {'form': form})

