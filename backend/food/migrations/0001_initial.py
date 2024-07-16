# Generated by Django 3.2.16 on 2024-07-16 07:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название категории')),
                ('slug', models.SlugField(help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.', max_length=30, unique=True, verbose_name='Идентификатор категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Например "От шефа (если речь про шаурму)"', max_length=30, verbose_name='Название блюда')),
                ('image', models.ImageField(default=None, help_text='Загрузите изображение для блюда', null=True, upload_to='dishes/', verbose_name='Изображение')),
                ('text', models.TextField(help_text='Описание блюда', verbose_name='Описание')),
                ('cooking_time', models.PositiveSmallIntegerField(help_text='Введите время приготовления', validators=[django.core.validators.MinValueValidator(15, 'Минимальное время: 15 минут')], verbose_name='Время приготовления')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Названия ингридинта для блюда', max_length=30, verbose_name='Название ингредиента')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
                'ordering': ('name',),
            },
        ),
        migrations.AddConstraint(
            model_name='ingredient',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_ingredient'),
        ),
        migrations.AddField(
            model_name='dish',
            name='category',
            field=models.ForeignKey(blank=True, help_text='Можно установить несколько тегов на один рецепт', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='food.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='dish',
            name='ingredients',
            field=models.ManyToManyField(help_text='Ингредиенты в составе блюда', related_name='dishes', to='food.Ingredient', verbose_name='Ингредиенты'),
        ),
    ]
