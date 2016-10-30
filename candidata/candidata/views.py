from django.views.generic import TemplateView, FormView
from .opensecrets import getContributionsByIssue
from .politifact import getRecentStatementRulings
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
            "trump_os": getContributionsByIssue("donald-trump", topic),
        }

        # Get the Politifact data on the given topic
        # self.request.session["pf_data"] = {
        #     "hillary_pf": getRecentStatementRulings("hillary-clinton", topic),
        #     "gary_pf": getRecentStatementRulings("gary-johnson", topic),
        #     "trump_pf": getRecentStatementRulings("donald-trump", topic),
        # }
        return HttpResponseRedirect(reverse('results'))


class Results(TemplateView):
    template_name = 'results.html'
