from django.shortcuts import render , redirect
from django.views.generic import ListView , DetailView

from django.db.models import Q , F , Func , DecimalField , Value , CharField
from django.db.models.aggregates import Avg , Sum , Count , Max , Min

from .models import Product , Brand , Review , ProductImages
from .forms import ReviewForm

from django.db.models.functions import Cast
from django.views.decorators.cache import cache_page

from .tasks import send_emails


from django.http import JsonResponse
from django.template.loader import render_to_string


# @cache_page(60 * 1)
def debug(request):
    
    # data = Product.objects.all()
    
    # data = Product.objects.filter(price__gt=98)
    # data = Product.objects.filter(price__gte=98)
    # data = Product.objects.filter(price__lt=22)
    # data = Product.objects.filter(price__lte=22)
    # data = Product.objects.filter(price__range=(21,22))
    
    
    # data = Product.objects.filter(name__contains='Jeffrey')
    # data = Product.objects.filter(name__startswith='Jeffrey')
    # data = Product.objects.filter(name__endswith='Mullins')
    
    # data = Product.objects.filter(name__contains='Jeffrey',price__gt=50)
    
    # data = Product.objects.filter(
    #     Q(name__contains='Jeffrey') &
    #     Q(price__gt=50)
    #       )
    
    # data = Product.objects.filter(
    #     Q(name__contains='Jeffrey') |
    #     Q(price__gt=90)
    #       )
    
    
    # data = Product.objects.filter(
    #     Q(name__contains='Jeffrey') |
    #     ~Q(price__gt=22)
    #       )
    
    # data = Product.objects.order_by('price')
    # data = Product.objects.order_by('-price')
    
    # data = Product.objects.all()[:5]
    # data = Product.objects.earliest('price')
    # data = Product.objects.latest('price')
    # print(data)
    
    # django queries are lazy
    # data = Product.objects.filter(name__contains='Jeffrey').order_by('-price')  # merge queries (sql)
    
    # data = Product.objects.filter(name__contains='Jeffrey')
    # data = data.order_by('-price')
    
    # data = Product.objects.all()
    # data = Product.objects.values('name')
    # data = Product.objects.values_list('name')
    # data = Product.objects.only('name')
    #data = Product.objects.defer('slug','description')
    
    #data = Product.objects.all()  # R product:brand
    # data = Product.objects.select_related('brand').all() # products:brands one table  ForeignKey , One-to-one
    # data = Product.objects.prefetch_related('brand').all()   # many-to-many
    
    # aggregation 
    # data = Product.objects.aggregate(myavg=Avg('price'))
    # data = Product.objects.aggregate(mysum=Sum('price'))
    # data = Product.objects.aggregate(mymin=Min('price'))
    # data = Product.objects.aggregate(mymax=Max('price'))
    
    # Annotation
    # data = Product.objects.annotate(sell_price=F('price'*1.20 ,function='ROUND')) 
#     data = Product.objects.annotate(
#     sell_price=Func(F('price') * 1.20,2, function='ROUND',output_field=DecimalField())
# ) 
#     data = Product.objects.annotate(
#     sell_price=Func(Func(F('price') * 1.20, 2, function='ROUND', output_field=DecimalField()), 
#                     function='CONVERT', 
#                     template='%(expressions)s', 
#                     output_field=CharField()
#     )
# )
    
    
    send_emails.delay()
    
    data = Product.objects.all()
    
    
    return render(request,'products/debug.html',{'data':data})


class ProductList(ListView):    
    model = Product
    paginate_by = 50
    
    
    
'''
    1 : product detail :
        - base funtion : get_queryset 
        - extra data : get_context_data 
'''
    
class ProductDetail(DetailView):
    model = Product
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_images"] = ProductImages.objects.filter(product=self.get_object())
        context['product_reviews'] = Review.objects.filter(product=self.get_object())
        return context
    
    
    
    
class BrandList(ListView):
    model = Brand
    paginate_by=20
    
    
class BrandDetail(ListView):
    model = Product             # products    ----> # products 
    template_name = 'products/brand_detail.html'
    paginate_by=20
    
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = super().get_queryset()   # all products 
        queryset = queryset.filter(brand = brand)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context
    
    
    
    
def add_product_review(request,slug):
    
    product = Product.objects.get(slug=slug)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user 
            myform.product = product
            myform.save()
            
        
        reviews = Review.objects.filter(product=product)
        page = render_to_string('includes/review.html',{'product_reviews':reviews})
        return JsonResponse({'result':page})
            
            
