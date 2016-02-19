from django.contrib import admin
from apps.caafi.models import Language, Category, Subcategory, Url, Competence, Exercise, Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Define an inline admin descriptor for Profile model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )

class CategoryAdmin (admin.ModelAdmin):
	list_display = ('name', 'language', 'description')
	list_filter = [ 'language' ]

class SubcategoryAdmin (admin.ModelAdmin):
	list_display = ('name', 'category')
	list_filter = [ 'category' ]

class UrlAdmin (admin.ModelAdmin):
	list_display = ( 'address', 'subcategory', 'level', 'primary_competence', 'secondary_competence', 
					'kind_exercise', 'kind_correction', 'status', 'published')
	list_filter = [ 'subcategory' ]

# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Language)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Competence)
admin.site.register(Exercise)
admin.site.register(Url, UrlAdmin)