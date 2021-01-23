from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TeamMembers, Teams

# Create your views here.


def View_to_change(request):
    context = {'welcome': "Hello on our site"}
    return render(request, template_name='index.html', context=context)


class MockTeamsListView(ListView):
    template_name = 'mock_dashboard.html'
    model = Teams


class MockMembersListView(ListView):
    template_name = 'mock_team_members.html'
    model = TeamMembers
    # queryset = MockTeamMembers.objects.filter(team_name=self.request.resolver_match.kwargs['pk'])

    def get_queryset(self):
        return TeamMembers.objects.filter(team_name=self.request.resolver_match.kwargs['pk'])





