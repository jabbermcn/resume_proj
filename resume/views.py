from django.views.generic import TemplateView


class ContextMixin:
    context = {
        'site_title': '*****',
        'site_name': 'mikhailouski_n',
        'facebook': 'https://www.facebook.com/jabber.mcn/',
        'twitter': 'https://twitter.com',
        'linkedin': 'https://www.linkedin.com/in/николай-михайловский-612744246/',
        'instagram': 'https://www.instagram.com/mikhailouski_n/',
        'email': 'jabber_mcn@tut.by',
        'github': 'https://github.com/jabbermcn',
        'phone': '+375 29 5692410',
    }


class HomeTemplateView(ContextMixin, TemplateView):
    template_name = 'resume/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data()
        context.update(self.context)
        return context


class AboutTemplateView(ContextMixin, TemplateView):
    template_name = 'resume/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutTemplateView, self).get_context_data()
        context.update(self.context)
        return context


class ResumeTemplateView(ContextMixin, TemplateView):
    template_name = 'resume/resume.html'

    def get_context_data(self, **kwargs):
        context = super(ResumeTemplateView, self).get_context_data()
        context.update(self.context)
        return context


class PortfolioTemplateView(ContextMixin, TemplateView):
    template_name = 'resume/portfolio.html'

    def get_context_data(self, **kwargs):
        context = super(PortfolioTemplateView, self).get_context_data()
        context.update(self.context)
        return context


class ContactTemplateView(ContextMixin, TemplateView):
    template_name = 'resume/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactTemplateView, self).get_context_data()
        context.update(self.context)
        return context
