from django.views.generic import TemplateView, FormView
from .opensecrets import getContributionsByIssue
from .readpolitifact import read_recent_statements
from django.http.response import HttpResponseRedirect
from django.shortcuts import reverse
from .forms import IssueForm


class Home(FormView):
    template_name = 'home.html'
    form_class = IssueForm

    def form_valid(self, form):
        topic = form.cleaned_data.get("issue")
        # Get the OpenSecrets data on the given topic
        self.request.session["os_data"] = {
            "hillary_os": getContributionsByIssue("hillary-clinton", topic),
            "gary_os": getContributionsByIssue("gary-johnson", topic),
            "donald_os": getContributionsByIssue("donald-trump", topic),
        }

        # Get the Politifact data on the given topic
        self.request.session["pf_data"] = {
            "hillary_pf": read_recent_statements("hillary-clinton", topic),
            "gary_pf": read_recent_statements("gary-johnson", topic),
            "donald_pf": read_recent_statements("donald-trump", topic),
        }
        return HttpResponseRedirect(reverse('results'))


class Results(TemplateView):
    template_name = 'results.html'
