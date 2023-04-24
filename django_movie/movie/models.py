from django.db import models
from datetime import date
from django.urls import reverse

class Category(models.Model):

    # Катигория фильмов

    name = models.CharField('Имя', max_length=150) #
    descriprions = models.TextField("Описания ") # TextFiled - текстовое поле 
    url = models.SlugField(max_length=150, unique=True) # SlugField - использвуется для url(s)
 
    # Возвращает  значение в виде строки
    def __str__(self):
        return self.name
    

    # Мета данные которые связываются с базой данных 
    class Meta:
        verbose_name = "Категория" # ед. число 
        verbose_name_plural = "Категория" 


class Actor(models.Model):

    # Категория актеров и режисеров

    name = models.CharField('Имя', max_length=150)
    age = models.PositiveSmallIntegerField('Возраст', default=0) # PositiveSmallIntegerField - значения от 0 до 32767
    descriprions = models.TextField("Описания ") # TextFiled - текстовое поле 
    imgae = models.ImageField('Изоброжения ', upload_to='actors/') # Сохраняет изображения в дериктории actors

    # Возвращает  значение в виде строки
    def __str__(self):
        return self.name
    

    # Мета данные которые связываются с базой данных 
    class Meta:
        verbose_name = "Актеры и Режисеры" # ед. число 
        verbose_name_plural = "Актеры и Режисеры" 


class Ganre(models.Model):

    # Жанры

    name = models.CharField('Имя', max_length=100)
    descriprions = models.TextField("Описания ") # TextFiled - текстовое поле 
    url = models.SlugField(max_length=150, unique=True) # SlugField - используется  для url(s)
    

    # Возвращает  значение в виде строки
    def __str__(self):
        return self.name


    # Мета данные которые связываются с базой данных 
    class Meta:
        verbose_name = "Жанры" # ед. число 
        verbose_name_plural = "Жанры" 


class Movie(models.Model):
    
    # Фильмы

    title = models.CharField('Название', max_length=150)
    tagline = models.CharField('Слоган', max_length=100, default='')
    descriprions = models.TextField("Описания ") # TextFiled - текстовое поле 
    poster = models.ImageField('Постер', upload_to='movies/') # сохроняет значение в дерикторий movies
    year = models.PositiveSmallIntegerField('Дата выхода', default=2018)
    county = models.CharField('Страны', max_length=50)
    directors = models.ManyToManyField(Actor, verbose_name='Режиссер', related_name='film_director') # ManyToManyField - Отношение многих ко многим
    actors = models.ManyToManyField(Actor, verbose_name="Актеры", related_name='film_actor') # ManyToManyField - Отношение многих ко многим
    gengers = models.ManyToManyField(Ganre, verbose_name="Жанры") # ManyToManyField - Отношение многих ко многим
    world_premier = models.DateField("Примьера в мире", default=date.today) # ставить значение времени
    budger = models.PositiveIntegerField('Бюджет', default=0, help_text='Указывать сумму в долларах')
    fees_in_usa = models.PositiveIntegerField(
        'Сборы в сша', default=0, help_text='Укажите сумму в долларах'
    )
    fees_in_world = models.PositiveIntegerField(
        'Сборы в мире', default=0, help_text='Укажите сумму в долларх'
    )

    category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True
    ) # ForeignKey - отношение многих к одному

    url = models.SlugField(max_length=150, unique=True) # SlugField - используется   для url(s)
    draft = models.BooleanField('Черновик', default=False)

    # Возвращает  значение в виде строки
    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.url})



    # Мета данные которые связываются с базой данных 
    class Meta:
        verbose_name = "Фильм " # ед. число 
        verbose_name_plural = "Фильм" 


class MovieShort(models.Model):

    # Отрывки из фильма

    title = models.CharField('Название', max_length=150)
    descriprions = models.TextField('Описания ') # TextFiled - текстовое поле 
    imgae = models.ImageField('Изоброжения ', upload_to='movie_shorts/') # сохроняет изоброженияв дериктории movie_shorts
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)    # ForeignKey - отношение многих к одному


    # Возвращает  значение в виде строки
    def __str__(self):
        return self.title
    

    # Мета данные которые связываются с базой данных 
    class Meta:
        verbose_name = "Кадры из фильма" # ед. число 
        verbose_name_plural = "Кадры из фильма" 


class RatingStar(models.Model):

    # рейтинг в виде звезд

    value = models.SmallIntegerField('Значение', default=0)

    def __str__(self):
        return self.value
    
    class Meta:
        verbose_name = "Звезда рейтинга" # ед. число 
        verbose_name_plural = "Звезда рейтинга" 

class Rating(models.Model):

    # рейтинг фильма

    ip = models.CharField('IP адрес', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фильм')


    def __str__(self):
        return f'{self.star} - {self.movie}'
    
    class Meta:
        verbose_name = "Рейтинг" # ед. число 
        verbose_name_plural = "Рейтинг" 

class Reviews(models.Model):

    email = models.EmailField()
    name = models.CharField('Имя', max_length=150)
    text = models.TextField('Сообщение', max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True
    )

    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'
    
    class Meta:
        verbose_name = "Отзыв" # ед. число 
        verbose_name_plural = "Отзыв" 