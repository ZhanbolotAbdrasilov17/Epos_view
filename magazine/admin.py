from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *


# class ContactsPhoneAdmin(admin.TabularInline):
#     model = ContactsPhone
#     fields = ('priem', 'faqs')
#     max_num = 100
#     extra = 0

# @admin.register(Contacts)
# class ContactsAdminList(TranslationAdmin):
#     inlines = [ContactsPhoneAdmin]


admin.site.register(ContactsPhone)
admin.site.register(Logo)
admin.site.register(Partner)



@admin.register(Contacts)
class ContactsAdminList(admin.ModelAdmin):
    pass

@admin.register(HomeBanner)
class HomeBannerAdminList(admin.ModelAdmin):
    pass

@admin.register(HomeBook)
class HomeBookAdminList(admin.ModelAdmin):
    pass


@admin.register(HomeAbout)
class HomeAboutAdminList(admin.ModelAdmin):
    pass


@admin.register(HomeAfisha)
class HomeAfishaAdminList(admin.ModelAdmin):
    pass


@admin.register(HomeComment)
class HomeCommentAdminList(admin.ModelAdmin):
    pass


@admin.register(HomeAcademy)
class HomeAcademyAdminList(admin.ModelAdmin):
    pass


@admin.register(HomeStatistic)
class HomeStatisticAdminList(admin.ModelAdmin):
    pass


@admin.register(News)
class NewsAdminList(admin.ModelAdmin):
    pass


@admin.register(IssuesCategory)
class IssuesCategoryAdminList(admin.ModelAdmin):
    pass


@admin.register(Issues)
class IssuesAdminList(admin.ModelAdmin):
    pass