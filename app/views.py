from django.views import generic

from .models import Category


class CategoryList(generic.ListView):
    model = Category
    template_name = 'category_list.html'

    def get_queryset(self):
        return self.model.objects.find_all_active()
