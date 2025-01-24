from django.shortcuts import render
from django.views.generic import TemplateView,FormView,CreateView
from website.forms import ContactUsModelForm,NewletterModelForm
from django.contrib import messages
from django.shortcuts import redirect

class IndexView(TemplateView):
    template_name = 'website/index.html'

class AboutView(TemplateView):
    template_name = 'website/about.html'

class ContactView(TemplateView):
    template_name = 'website/contact.html'

class SendTicketView(CreateView):
    http_method_names = ['post']
    form_class = ContactUsModelForm
    

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, 'تیکت شما با موفقیت ثبت شد و در اسرع وقت با شما تماس حاصل خواهد شد')
        return super().form_valid(form)

    def form_invalid(self, form):
        # handle unsuccessful form submission
        messages.error(
            self.request, 'مشکلی در ارسال فرم شما پیش آمد لطفا ورودی ها رو بررسی کنین و مجدد ارسال نمایید')
        return redirect(self.request.META.get('HTTP_REFERER'))

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')


class NewletterView(CreateView):
    http_method_names = ['post']
    form_class = NewletterModelForm
    success_url = '/'

    def form_valid(self, form):
        # handle successful form submission
        messages.success(
            self.request, 'از ثبت نام شما ممنونم، اخبار جدید رو براتون ارسال می کنم 😊👍')
        return super().form_valid(form)

    def form_invalid(self, form):
        # handle unsuccessful form submission
        messages.error(
            self.request, 'مشکلی در ارسال فرم شما وجود داشت که می دونم برا چی بود!! چون ربات هستید!')
        return redirect('website:index')


