from django.views.generic import ListView

from post.models import Post
from about.models import SocialModel


# Create your views here.
class SearchListView(ListView):
    template_name = 'search/search_view.html'
    context_object_name = 'home_content'

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get('q', None)
        if query is not None:
            return Post.objects.search(query)
        else:
            return Post.objects.none()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['social_link'] = SocialModel.objects.all()[:1]
        context['query'] = self.request.GET.get('q')
        return context
