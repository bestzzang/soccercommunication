from django.shortcuts import render, get_object_or_404


from .models import *
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect
from django.views.generic.detail import DetailView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator



def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)


    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)


    return render(request, 'shop/list.html',
                  {'current_category': current_category, 'categories': categories, 'products': products})





@method_decorator(login_required, name="dispatch")
class ProductDetailView(DetailView):

    model = Product
    template_name = 'shop/detail.html'


    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['product_list'] = Product.objects.all()
        return context

index = ProductDetailView.as_view()




@login_required
def product_mypage(request):
    products = Product.objects.all()
    return render(request, 'shop/mypage.html', {'products':products})


'''
class ProductUploadView(LoginRequiredMixin, CreateView):
    login_url = 'accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Product
    fields = ['category', 'image', 'cname', 'pname', 'description', 'meta_description', 'slug', 'unit_price', 'stock', 'available_display', 'available_order']
    template_name = 'shop/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})
'''


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Product
    success_url = '/'
    template_name = 'shop/delete.html'

class ProductUpdatedView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Product
    fields = ['image', 'pname', 'description', 'meta_description', 'slug', 'unit_price', 'stock',]
    template_name = 'shop/update.html'









from .search_indexes import *

@login_required
def search(request):
    search_form = NoteIndex()
    return render(request, 'search/search.html', {'form':search_form})
