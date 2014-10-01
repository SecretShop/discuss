from django.views.generic.base import TemplateView


class TeamList(TemplateView):
    template_name = "team_list.html"


class PostList(TemplateView):
    template_name = "post_list.html"
