import random

from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.views.generic.edit import UpdateView

from .models import SeedFortune


def result(request):
    """
    Show the results of the fortune cookie.
    :param request:
    :return:
    """

    fortunes = SeedFortune.objects.all()
    fortune = fortunes[random.randrange(0, len(fortunes))]
    template = loader.get_template('pool/result.html')
    context = {
        'fortune': fortune
    }

    return HttpResponse(template.render(context, request))


class FortuneUpdate(SuccessMessageMixin, UpdateView):
    """
    Generic update class
    """
    model = SeedFortune
    fields = ['description']
    template_name_suffix = '_update_form'
    success_message = 'Congrats! You have successfully made your own fortune.'

    def get_success_url(self):
        """
        Redirects upon success
        :return:
        """

        print ("PKish :{}".format(self.get_object().id))
        return reverse("change_fortune", args=(self.get_object().id,))
