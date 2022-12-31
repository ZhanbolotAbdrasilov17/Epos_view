from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('for-authors', for_authors, name='for_authors'),
    path('epos-contacts', contact_page, name='contact_page'),
    path('mail/create/', MailCreateView.as_view(), name='mail_create'),
    path('news', news_page, name='news'),
    path('news/<int:news_id>/', NewsDetail.as_view(), name='news'),
    path('issues', issues_page, name='issues'),
    # path('issues/<int:issues_id>/', IssuesDetail.as_view(), name='issues'),



]
