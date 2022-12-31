from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Contacts)
class ContactsTranslation(TranslationOptions):
    fields = ('address',)

@register(ContactsPhone)
class ContactsPhoneTranslation(TranslationOptions):
    fields = ('priem', 'faqs',)

@register(HomeBook)
class HomeBookTranslation(TranslationOptions):
    fields = ('number1', 'number2', 'extra', 'description', 'text')





@register(HomeAfisha)
class HomeAfishaTranslation(TranslationOptions):
    fields = ('day', 'month_year', 'title', 'text',)


@register(HomeComment)
class HomeCommentTranslation(TranslationOptions):
    fields = ('name', 'text',)


@register(HomeAcademy)
class HomeAcademyTranslation(TranslationOptions):
    fields = ('title', 'text',)

@register(HomeStatistic)
class HomeStatisticTranslation(TranslationOptions):
    fields = ('title',)


@register(News)
class NewsTranslation(TranslationOptions):
    fields = ('title', 'text',)


@register(IssuesCategory)
class IssuesCategoryTranslation(TranslationOptions):
    fields = ('title',)


@register(Issues)
class IssuesTranslation(TranslationOptions):
    fields = ('title', 'text',)