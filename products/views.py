from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm



# View for the public landing page
def landing_page(request):
    return render(request, 'products/landing.html')
# Retrieve all products and calculate inventory metrics for the dashboard
def product_list(request):
    products = Product.objects.all()
    
    total_products = products.count()
    in_stock_count = products.filter(quantity__gte=5).count()
    low_stock_count = products.filter(quantity__lt=5).count()
    
    context = {
        'products': products,
        'total_products': total_products,
        'in_stock_count': in_stock_count,
        'low_stock_count': low_stock_count,
    }
    return render(request, 'products/product_list.html', context)

# Handle creation of new stock entries including uploaded images
def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'products/product_form.html', {'form': form})

# Handle editing and updating existing product details or pictures
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'products/product_form.html', {'form': form})

# Handle confirmation and deletion of a product record
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})