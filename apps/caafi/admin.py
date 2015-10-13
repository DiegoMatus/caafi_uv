from django.contrib import admin
from apps.caafi.models import Language, Category, Subcategory, Url, Competence, Exercise

class CategoryAdmin (admin.ModelAdmin):
	list_display = ('language', 'name', 'description')
	list_filter = [ 'language' ]

class SubcategoryAdmin (admin.ModelAdmin):
	list_display = ('name', 'category')
	list_filter = [ 'category' ]

class UrlAdmin (admin.ModelAdmin):
	list_display = ( 'address', 'subcategory', 'level', 'primary_competence', 'secondary_competence', 
					'kind_exercise', 'kind_correction', 'status', 'published')
	list_filter = [ 'subcategory' ]

# Register your models here.
#admin.site.register(Attendant)
admin.site.register(Language)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Competence)
admin.site.register(Exercise)
admin.site.register(Url, UrlAdmin)