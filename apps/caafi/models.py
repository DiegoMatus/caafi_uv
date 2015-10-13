# -*- coding:utf-8 -*-
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.conf import settings
import uuid
import os

# Create your models here.
def get_file_path_languages(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images/languages', filename)


class Language(models.Model):
    '''Se puede registrar cualquier cantidad de idiomas.'''
    name = models.CharField('Nombre', max_length=50)
    image = models.FileField(upload_to=get_file_path_languages)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Lenguaje'
        verbose_name_plural = 'Lenguajes'

    def save(self):
        self.slug = slugify(str(self.name))
        super(Language, self).save()

    def __str__(self):
        return self.name


#############################################################################################
def get_file_path_category(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images/categories', filename)


class Category(models.Model):
    '''Una categoría puede pertenecer a un único idioma. Un idioma puede contener una o varias categorías registradas.'''
    language = models.ForeignKey(Language, verbose_name='Idioma', related_name='categories')
    name = models.CharField('Nombre', max_length=50)
    description = models.TextField ('Descripción')
    image = models.FileField(upload_to=get_file_path_category)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def save(self):
        self.slug = slugify(str(self.name))
        super(Category, self).save()

    def get_total(self):
        return self.count()

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    '''Cada categoría cuenta debería contar con varias subcategorías y estás a su vez sólo deben estar disponibles en los idiomas a los que se le asocie.'''
    #language = models.ForeignKey(Language, verbose_name='Idioma', related_name='subcategories2')
    name = models.CharField('Nombre', max_length=50)
    category = models.ForeignKey(Category, verbose_name='Categoria', related_name='subcategories')
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Subcategoría'
        verbose_name_plural = 'Subcategorías'

    def save(self):
        self.slug = slugify(str(self.name))
        super(Subcategory, self).save()

    def __str__(self):
        return self.name


class Competence(models.Model):
    '''Catálogo de competencias que podrán ser seleccionadas al registrar una nueva URL'''
    name = models.CharField('Nombre', max_length=50)

    class Meta:
        verbose_name = 'Competencia'
        verbose_name_plural = 'Competencias'

    def __str__(self):
        return self.name


class Exercise(models.Model):
    '''Catálogo de los diferentes tipos de ejercicio que podrán ser seleccionadas al registrar una nueva URL'''
    name = models.CharField('Nombre', max_length=50)

    class Meta:
        verbose_name = 'Ejercicio'
        verbose_name_plural = 'Ejercicios'

    def __str__(self):
        return self.name


class Url(models.Model):
    '''Una URL está registrada dentro de una o varias subcategorías pertenecientes a una misma categoría de un idioma'''
    CORRECTIONS = (
        ('SI', 'Tiene correción'),
        ('SI+', 'Tiene correción más explicación'),
        ('NO', 'No tiene correción'),
        ('NA', 'No aplica')
    )

    LEVELS = (
        ('A1', 'A1 - Principiante'),
        ('A2', 'A2 - Intermedio bajo'),
        ('B1', 'B1 - Intermedio'),
        ('B2', 'B2 - Intermedio alto'),
        ('C1', 'C1 - Avanzado'),
        ('C2', 'C2 - Perfeccionamiento')
    )

    address = models.URLField('Dirección', max_length=255)
    description = models.TextField('Descripción')
    #language = models.ForeignKey(Language, verbose_name='Idioma', related_name='urls6')
    subcategory = models.ForeignKey(Subcategory, verbose_name='Subcategorías', related_name='urls_subcategory')
    level = models.CharField('Nivel', max_length=2, choices=LEVELS)
    primary_competence = models.ForeignKey(Competence, verbose_name='Competencia primaria', related_name='urls_competences_primary')
    secondary_competence = models.ForeignKey(Competence, verbose_name='Competencia secundaria', related_name='urls_competences_secondary')
    kind_exercise = models.ForeignKey(Exercise, verbose_name='Tipo de ejercicio', related_name='urls_exercise')
    kind_item = models.CharField('Cantidad/Duración de Items', max_length=50)
    kind_correction = models.CharField('Tipo de correción', max_length=3, choices=CORRECTIONS)
    status = models.BooleanField('Sin reportar', default=True)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Url'
        verbose_name_plural = 'Urls'

    def __str__(self):
        return self.address

