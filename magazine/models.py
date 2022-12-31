from ckeditor.fields import RichTextField
from django.db import models


class Logo(models.Model):
    logo = models.FileField(upload_to='logo', blank=True, null=True)

    def __str__(self):
        return 'Логотип'


    class Meta:
        verbose_name_plural = 'Логотип'
        verbose_name = 'Логотип'


class Contacts(models.Model):
    address = models.CharField(max_length=500, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    whatsapp = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    vk = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return 'Контакты'

    class Meta:
        verbose_name_plural = 'Контакты'
        verbose_name = 'Контакты'


class ContactsPhone(models.Model):
    priem = models.CharField(max_length=50, blank=True, null=True)
    faqs = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return 'Телефоны'

    class Meta:
        verbose_name_plural = 'Телефоны'
        verbose_name = 'Телефоны'


class Partner(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    image = models.FileField(upload_to='partners', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Партнеры'
        verbose_name = 'Партнеры'


class HomeBanner(models.Model):
    home = models.FileField(upload_to='banner', blank=True, null=True)
    authors = models.FileField(upload_to='banner', blank=True, null=True)
    issues = models.FileField(upload_to='banner', blank=True, null=True)
    contacts = models.FileField(upload_to='banner', blank=True, null=True)

    def __str__(self):
        return 'Банеры'

    class Meta:
        verbose_name_plural = 'Банеры'
        verbose_name = 'Банеры'


class HomeBook(models.Model):
    number1 = models.CharField(max_length=50, blank=True, null=True)
    number2 = models.CharField(max_length=50, blank=True, null=True)
    extra = models.CharField(max_length=50, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    text = RichTextField(blank=True, null=True)

    def __str__(self):
        return 'Главная - Книга'

    class Meta:
        verbose_name_plural = 'Главная - Книга'
        verbose_name = 'Главная - Книга'


class HomeAbout(models.Model):
    description = RichTextField(blank=True, null=True)
    text = RichTextField(blank=True, null=True)

    def __str__(self):
        return 'Главная - О журнале'

    class Meta:
        verbose_name_plural = 'Главная - О журнале'
        verbose_name = 'Главная - О журнале'


class HomeAfisha(models.Model):
    image = models.FileField(upload_to='banner', blank=True, null=True)
    day = models.CharField(max_length=50, blank=True, null=True)
    month_year = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    text = RichTextField(blank=True, null=True)

    def __str__(self):
        return 'Главная - Афиша'

    class Meta:
        verbose_name_plural = 'Главная - Афиша'
        verbose_name = 'Главная - Афиша'



class HomeComment(models.Model):
    image = models.FileField(upload_to='banner', blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    text = RichTextField(blank=True, null=True)

    def __str__(self):
        return 'Главная - Комментарий'

    class Meta:
        verbose_name_plural = 'Главная - Комментарии'
        verbose_name = 'Главная - Комментарии'


class HomeAcademy(models.Model):
    image = models.FileField(upload_to='banner', blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    text = RichTextField(blank=True, null=True)

    def __str__(self):
        return 'Главная - Комментарий'


class HomeStatistic(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Главная - Статистика'
        verbose_name = 'Главная - Статистика'


class News(models.Model):
    image = models.FileField(upload_to='news')
    title = models.CharField(max_length=1000, blank=True, null=True)
    text = RichTextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Главная - Новости'
        verbose_name = 'Главная - Новости'


class IssuesCategory(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Выпуски - Категории'
        verbose_name = 'Выпуски - Категории'


class Issues(models.Model):
    category = models.ForeignKey(IssuesCategory, on_delete=models.CASCADE)
    image = models.FileField(upload_to='news')
    title = models.CharField(max_length=1000, blank=True, null=True)
    file = models.FileField(upload_to='issues')
    text = RichTextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Выпуски - Категории'
        verbose_name = 'Выпуски - Категории'
