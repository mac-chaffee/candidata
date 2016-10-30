from django.views.generic import TemplateView, FormView
from .readopensecrets import read_contributions, read_contributors
from .readpolitifact import read_recent_statements
from .fivethirtyeight import getPollNum
from django.http.response import HttpResponseRedirect
from django.shortcuts import reverse
from .forms import IssueForm


class Home(FormView):
    template_name = 'home.html'
    form_class = IssueForm

    def get(self, request):
        self.request.session ["top_contribs"] = {
            "hillary_contribs": read_contributors("hillary-clinton"),
            "gary_contribs": read_contributors("gary-johnson"),
            "donald_contribs": read_contributors("donald-trump")
        }
        return super(Home, self).get(request)

    def form_valid(self, form):
        topic = form.cleaned_data.get("issue")
        # Get the OpenSecrets data on the given topic
        self.request.session["os_data"] = {
            "hillary_os": read_contributions("hillary-clinton", topic),
            "gary_os": read_contributions("gary-johnson", topic),
            "donald_os": read_contributions("donald-trump", topic),
        }

        # Get the Politifact data on the given topic
        self.request.session["pf_data"] = {
            "hillary_pf": read_recent_statements("hillary-clinton", topic),
            "gary_pf": read_recent_statements("gary-johnson", topic),
            "donald_pf": read_recent_statements("donald-trump", topic),
        }

        # Get polling data from 538
        self.request.session["polling_data"] = {
            "hillary_polling": getPollNum("hillary-clinton"),
            "gary_polling": getPollNum("gary-johnson"),
            "donald_polling": getPollNum("donald-trump")
        }
        print(self.request.session["polling_data"])
        return HttpResponseRedirect(reverse('results'))


class Results(TemplateView):
    template_name = 'results.html'
