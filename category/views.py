from django.views.generic import ListView

from post.models import Post
from about.models import SocialModel


# Create your views here.
class CategoryListView(ListView):
    template_name = 'category/category_view.html'
    context_object_name = 'home_content'

    def get_queryset(self, *args, **kwargs):
        category_slug = self.kwargs.get('slug', None)
        if category_slug:
            return Post.objects.category(category_slug)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['social_link'] = SocialModel.objects.all()[:1]
        return context
