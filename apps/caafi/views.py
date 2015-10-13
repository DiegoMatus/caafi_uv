from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import JsonResponse
from apps.caafi.models import Language, Category, Subcategory, Url
from django.views.decorators.csrf import csrf_exempt


def sorting(items):
    items_name = []
    for item in items:
        items_name.append(item.name)

    items_sort = []
    for name in sorted(items_name):
        for item in items:
            if item.name == name:
                items_sort.append(item)
    return items_sort


# Create your views here.
def index(request):
    languages = Language.objects.all()
    languages = sorting(languages)
    context = {'languages': languages}
    return render(request, 'index.html', context)


def categories_view(request, language_slug):
	return render(request, 'index.html')

def subcategories_view(request, language_slug, category_slug):
	return render(request, 'index.html')

def urls_view(request, language_slug, category_slug, subcategory_slug):
	return render(request, 'index.html')

def reported_urls_view(request):
	return render(request, 'index.html')

#def lista_categorias(request, language_name):
#    languages = Language.objects.all()
#    languages = sorting(languages)
#    language_id = Language.objects.filter(slug=language_name)
#    if len(language_id) > 0:
#        language = get_object_or_404(Language, pk=language_id[0].id)
#        # menu_name = language.name
#        categories = language.categories.all()
#        categories = sorting(categories)
#
#        return render_to_response('caafi/categories.html',
#                                  {'languages': languages, 'menu': language, 'language': language_name,
#                                   'categories': categories})
#    else:
#        return render_to_response('caafi/404.html')
#
#
#def lista_subcategorias(request, language_name, category_name):
#    languages = Language.objects.all()
#    languages = sorting(languages)
#    language_id = Language.objects.filter(slug=language_name)
#    if len(language_id) > 0:
#        language = get_object_or_404(Language, pk=language_id[0].id)
#        # menu_name = language.name
#        categories = language.categories.all()
#        categories = sorting(categories)
#        category_id = Category.objects.filter(slug=category_name)
#        if len(category_id) > 0:
#            category = get_object_or_404(Category, pk=category_id[0].id)
#            subcategories = category.subcategories.all()
#            subcategories = sorting(subcategories)
#            return render_to_response('caafi/subcategories.html',
#                                  {'languages': languages, 'menu': language, 'language': language_name,
#                                   'categories': categories, 'category': category.name, 'categoryname': category_name, 'subcategories': subcategories})
#    #return render_to_response('caafi/404.html')
#
#
#def lista_urls(request, language_name, category_name, subcategory_name):
#    languages = Language.objects.all()
#    languages = sorting(languages)
#    language_id = Language.objects.filter(slug=language_name)
#    if len(language_id) > 0:
#        language = get_object_or_404(Language, pk=language_id[0].id)
#        # menu_name = language.name
#        categories = language.categories.all()
#        categories = sorting(categories)
#        category_id = Category.objects.filter(slug=category_name)
#        if len(category_id) > 0:
#            category = get_object_or_404(Category, pk=category_id[0].id)
#            subcategory_id = Subcategory.objects.filter(slug=subcategory_name)
#            if len(subcategory_id) > 0:
#                subcategory = get_object_or_404(Subcategory, pk=subcategory_id[0].id)
#                urls = subcategory.urls2.all()
#                return render_to_response('caafi/urls.html', {'languages': languages, 'menu': language, 'language': language_name,
#                                                  'categories': categories, 'urls': urls,
#                                                  'subcategory': subcategory.name}, context_instance =RequestContext(request))
#    #return render_to_response('caafi/404.html')
#
#
#@csrf_exempt
#def urls_reportadas(request):
#    if request.method == 'POST':
#        reported_url = request.POST.get("link", None)
#        url = Url.objects.get(address = reported_url)
#        url.status = False
#        url.save()
#        return JsonResponse(dict({'msj': 'Haz reportado la direccion: ' + url.address}))
#    else:
#        return render_to_response('caafi/urls.html', context_instance=RequestContext(request))
