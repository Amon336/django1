# Generated by Django 4.1.7 on 2023-04-14 15:48

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')),
                ('descriprions', models.TextField(verbose_name='Описания ')),
                ('imgae', models.ImageField(upload_to='actors/', verbose_name='Изоброжения ')),
            ],
            options={
                'verbose_name': 'Актеры и Режисеры',
                'verbose_name_plural': 'Актеры и Режисеры',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('descriprions', models.TextField(verbose_name='Описания ')),
                ('url', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категория',
            },
        ),
        migrations.CreateModel(
            name='Ganre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('descriprions', models.TextField(verbose_name='Описания ')),
                ('url', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Жанры',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='Слоган')),
                ('descriprions', models.TextField(verbose_name='Описания ')),
                ('poster', models.ImageField(upload_to='movies/', verbose_name='Постер')),
                ('year', models.PositiveSmallIntegerField(default=2018, verbose_name='Дата выхода')),
                ('county', models.CharField(max_length=50, verbose_name='Страны')),
                ('world_premier', models.DateField(default=datetime.date.today, verbose_name='Примьера в мире')),
                ('budger', models.PositiveIntegerField(default=0, help_text='Указывать сумму в долларах', verbose_name='Бюджет')),
                ('fees_in_usa', models.PositiveIntegerField(default=0, help_text='Укажите сумму в долларах', verbose_name='Сборы в сша')),
                ('fees_in_world', models.PositiveIntegerField(default=0, help_text='Укажите сумму в долларх', verbose_name='Сборы в мире')),
                ('url', models.SlugField(max_length=150, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('actors', models.ManyToManyField(related_name='film_actor', to='movie.actor', verbose_name='Актеры')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.category', verbose_name='Категория')),
                ('directors', models.ManyToManyField(related_name='film_director', to='movie.actor', verbose_name='Режиссер')),
                ('gengers', models.ManyToManyField(to='movie.ganre', verbose_name='Жанры')),
            ],
            options={
                'verbose_name': 'Фильм ',
                'verbose_name_plural': 'Фильм',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звезда рейтинга',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie', verbose_name='Фильм')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.reviews', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзыв',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адрес')),
                ('movie', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='movie.movie', verbose_name='фильм')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.ratingstar', verbose_name='звезда')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинг',
            },
        ),
        migrations.CreateModel(
            name='MovieShort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('descriprions', models.TextField(verbose_name='Описания ')),
                ('imgae', models.ImageField(upload_to='movie_shorts/', verbose_name='Изоброжения ')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie', verbose_name='Фильм')),
            ],
            options={
                'verbose_name': 'Кадры из фильма',
                'verbose_name_plural': 'Кадры из фильма',
            },
        ),
    ]