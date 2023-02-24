from django.views.generic import TemplateView


class ContextMixin:
    context = {
        'site_title': '*****',
        'site_name': 'mikhailouski_n',
        'facebook': 'https://facebook.com',
        'twitter': 'https://twitter.com',
        'linkedin': 'https://www.linkedin.com/in/николай-михайловский-612744246/',
        'instagram': 'https://instagram.com',
        'email': 'jabber_mcn@tut.by',
        'Github': 'https://github.com/jabbermcn',
        'phone': '+375 29 5692410',
    }


class HomeTemplateView(ContextMixin, TemplateView):
    template_name = 'resume/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data()
        context.update(self.context)
        return context
