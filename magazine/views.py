from django.shortcuts import render
from django.views.generic import DetailView
from django.views import View
from .models import *


def home(request):
    logo = Logo.objects.last()
    contacts = Contacts.objects.last()
    phones = ContactsPhone.objects.last()
    banner = HomeBanner.objects.last()
    book = HomeBook.objects.last()
    about = HomeAbout.objects.last()
    afisha = HomeAfisha.objects.last()
    comment = HomeComment.objects.last()
    academy = HomeAcademy.objects.last()
    partners = Partner.objects.all()
    statistic = HomeStatistic.objects.all()
    issues_list = Issues.objects.all()
    if len(issues_list) >= 9: issues = Issues.objects.all()[-9:]
    else: issues = Issues.objects.all()

    category = IssuesCategory.objects.all()
    context = {'logo': logo, 'contacts': contacts, 'phones': phones, 'banner': banner, 'book': book, 'about': about,
               'afisha': afisha, 'comment': comment, 'academy': academy, 'partners': partners, 'statistic': statistic,
               'issues': issues, 'category': category}
    return render(request, 'home.html', context)


def for_authors(request):
    logo = Logo.objects.last()
    contacts = Contacts.objects.last()
    phones = ContactsPhone.objects.last()
    banner = HomeBanner.objects.last()

    context = {'logo': logo, 'contacts': contacts, 'phones': phones, 'banner': banner}
    return render(request, 'forauthor/forauthor.html', context)


def contact_page(request):
    logo = Logo.objects.last()
    contacts = Contacts.objects.last()
    phones = ContactsPhone.objects.last()
    banner = HomeBanner.objects.last()

    context = {'logo': logo, 'contacts': contacts, 'phones': phones, 'banner': banner}
    return render(request, 'epos_contacts/epos_contacts.html', context)


def news_page(request):
    logo = Logo.objects.last()
    contacts = Contacts.objects.last()
    phones = ContactsPhone.objects.last()
    news = News.objects.all()
    context = {'logo': logo, 'contacts': contacts, 'phones': phones, 'news': news}
    return render(request, 'news/news.html', context)


class NewsDetail(DetailView):
    model = News
    template_name = 'news/news-detail.html'
    context_object_name = 'news'
    pk_url_kwarg = 'news_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['logo'] = Logo.objects.last()
        context['phones'] = ContactsPhone.objects.last()
        context['contacts'] = Contacts.objects.last()
        return context


def issues_page(request):
    logo = Logo.objects.last()
    contacts = Contacts.objects.last()
    phones = ContactsPhone.objects.last()
    issues = Issues.objects.all()
    category = IssuesCategory.objects.all()
    banner = HomeBanner.objects.last()

    context = {'logo': logo, 'contacts': contacts, 'phones': phones, 'issues': issues, 'category': category,
               'banner': banner}
    return render(request, 'issues/issues.html', context)


# class IssuesDetail(DetailView):
#     model = Issues
#     template_name = 'issues/issues-detail.html'
#     context_object_name = 'issues'
#     pk_url_kwarg = 'issues_id'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['logo'] = Logo.objects.last()
#         context['phones'] = ContactsPhone.objects.last()
#         context['contacts'] = Contacts.objects.last()
#         return context

class MailCreateView(View):
    @staticmethod
    def post(request, *args, **kwargs):
        form = MailForm(request.POST)

        if form.is_valid():
            form.save()
            last_sender = Mail.objects.first()
            message = f'Имя: {last_sender.name}\n' \
                      f'Почта: {last_sender.email}\n' \
                      f'Текст: {last_sender.text}'

            send_mail(
                f'{last_sender.name} {last_sender.email}',
                message,
                'send_mail_asoi@mail.ru',
                ['itpythonzhanbolot@gmail.com'],
                fail_silently=False,
            )

            messages.add_message(request, messages.SUCCESS, 'Письмо отправлено!')
            return HttpResponseRedirect(redirect_to=reverse_lazy('contacts'))

        messages.add_message(request, messages.ERROR, 'Ошибка отправки данных.')