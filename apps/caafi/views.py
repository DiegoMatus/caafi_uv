from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import JsonResponse
from apps.caafi.models import Language, Category, Subcategory, Url
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    languages = Language.objects.all() #Hacerlo global
    context = { 'languages': languages }
    return render(request, 'index.html', context)


def categories_view(request, language_slug):
	languages = Language.objects.all()
	language = get_object_or_404(Language, slug = language_slug)
	categories = language.categories.all()
	context = { 'languages': languages, 'language': language, 'categories': categories }
	return render(request, 'categories.html', context)

def subcategories_view(request, language_slug, category_slug):
	languages = Language.objects.all()
	language = get_object_or_404(Language, slug = language_slug)
	categories = language.categories.all()
	category = get_object_or_404(Category, slug = category_slug)
	subcategories = category.subcategories.all()
	context = { 'languages': languages, 'language': language, 'categories': categories,
				'category': category, 'subcategories': subcategories }
	return render(request, 'subcategories.html', context)

def urls_view(request, language_slug, category_slug, subcategory_slug):
	languages = Language.objects.all()
	language = get_object_or_404(Language, slug = language_slug)
	category = get_object_or_404(Category, slug = category_slug)
	categories = language.categories.all()
	subcategory = get_object_or_404(Subcategory, slug = subcategory_slug)
	urls = subcategory.urls_subcategory.all()
	context = { 'languages': languages, 'language': language, 'categories': categories,
				'category': category, 'subcategory': subcategory, 'urls': urls }
	return render(request, 'urls.html', context)

@csrf_exempt
def reported_urls_view(request):
    if request.method == 'POST':
        reported_url = request.POST.get("link", None)
        url = Url.objects.get(address = reported_url)
        url.status = False
        url.save()
        return JsonResponse(dict({'msj': 'Haz reportado la direccion: ' + url.address}))
    else:
        return render('urls.html')