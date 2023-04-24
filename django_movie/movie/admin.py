from django.contrib import admin
from .models import Ganre, Movie, MovieShort, Actor, Rating, RatingStar, Reviews, Category
# Register your models here.

admin.site.register(Ganre)
admin.site.register(Movie)
admin.site.register(MovieShort)
admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
