from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Movie
from .forms import ReviewForm


class MoviesView(ListView):
    """Список фильмов """

    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movie/movies.html"
    
class MovieDeteilView(DetailView):
    """Полное описание фильма"""

    model = Movie
    slug_field = "url"


class AddReview(View):
    # отзывы

    def post(self, request, pk):
        print(request.POST)
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect("/")
    

