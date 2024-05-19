from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Category
from django.views.decorators.cache import cache_page
from .forms import ProductForm, SearchForm, ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.db.models import Q
from .models import Review
from custom_loggin.models import MyUser

#home page that shows list of products
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.select_related('category').all()
    sale = Product.objects.select_related('category').filter(in_sale=True) 


    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    paginator = Paginator(products, 12)  # Show 12 products per page
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page.
        products = paginator.page(paginator.num_pages)

    return render(request, 'products/home-product-list.html', {'category': category, 'categories': categories, 'products': products, 'sale': sale})

#after clicking on a product on home page shows details of that product
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()
    form = ReviewForm()
    images = product.images.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            product.update_ratings()
            return redirect('product_detail', pk=pk)

    return render(request, 'products/product_details.html', {'product': product, 'reviews': reviews, 'form': form, 'images': images})

#adding product on website(for admins)
@login_required(login_url='login')  # Require authentication to access this view
def add_product(request):
    # Check if the logged-in user is the superuser
    if not request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to add products.")

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, 'Product added successfully!')
            return redirect('product_list')  # Redirect to the product list page
        else:
            messages.error(request, 'Error adding the product. Please check the form.')
    else:
        form = ProductForm()

    return render(request, 'products/add_product.html', {'form': form})

#about page of site and company owner
def about(request):
    return render(request, 'products/about.html')

#order the products in list of names called category page
def category(request, foo):
    #replacing Hyphens with space
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'products/category.html', {'products':products, 'category':category})
    except:
        messages.success(request, 'This Category Doesnt Exist !')
        return redirect('product_list')

#summary of categories
def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'products/category_summary.html', {"categories":categories})

#search
def search_view(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
            return render(request, 'products/search_results.html', {'results': results, 'query': query})
    else:
        form = SearchForm()
    return render(request, 'products/search.html', {'form': form})

def detail_view(request, pk):
    # Retrieve the item using the primary key (pk)
    item = get_object_or_404(Product, pk=pk)
    return render(request, 'detail.html', {'item': item})

#rating:
def add_review(request, pk):
    if request.method == 'POST':
        # Process the form submission and save the review to the database
        # This is just a placeholder, you need to replace it with your actual implementation
        # For example:
        product = Product.objects.get(pk=pk)
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        review = Review.objects.create(product=product, user=request.user, rating=rating, comment=comment)
        return redirect('product_detail', pk=pk)
    else:
        # Handle GET requests if necessary
        pass
    
    
#all products with filter option
def all_products(request):
    products = Product.objects.select_related('category').all()
    sale = Product.objects.select_related('category').filter(in_sale=True) 
    categories = Category.objects.all()
    
    return render(request, 'products/all_products.html', {'category': category, 'categories': categories, 'products': products, 'sale': sale})

#FILTER PRODUCTS BY AVIABLE AND OFF :
def Discounted(request, category_slug=None):
    category = None
    discounted = request.GET.get('discounted')
    available = request.GET.get('available')
    categories = Category.objects.all()

    products = Product.objects.all()
    
    if discounted:
        products = products.filter(in_sale=True)
    if available:
        products = products.filter(inventory__gt=0)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        
    return render(request, 'products/all_products.html', {'category': category, 'categories': categories,'products': products})

#discounted on navbar 
def Discounted(request, category_slug=None):
    category = None
    discounted = request.GET.get('discounted')
    available = request.GET.get('available')
    categories = Category.objects.all()

    products = Product.objects.all()
    
    if discounted:
        products = products.filter(in_sale=True)
    if available:
        products = products.filter(inventory__gt=0)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        
    return render(request, 'products/discounted.html', {'category': category, 'categories': categories,'products': products})

#FILTER BY CATEGORY
def filter_by_category(request):
    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'products/all_products.html', {'products': products, 'categories': categories})


def best_selling_product(request):
    best_selling_product = Product.objects.annotate(total_orders=Count('order')).order_by('-total_orders').first()
    return render(request, 'best_selling_product.html', {'best_selling_product': best_selling_product})
