from django.shortcuts import render, get_object_or_404
from .cart import Cart
from products.models import Product
from django.http import JsonResponse
from django.contrib import messages

#neshon dadan sabad kharid va mahsolat entekhab shode toye on
def cart_summary(request):
	
	cart = Cart(request)
	cart_products = cart.get_prods
	quantities = cart.get_quants
	totals = cart.cart_total()
	p_totals = cart.product_total()
	return render(request, "cart/cart_summary.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "p_totals":p_totals })




def cart_add(request):
	
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))

		# chek kardan mahsol toye database
		product = get_object_or_404(Product, id=product_id)
		cart.add(product=product, quantity=product_qty)

		# tedad mahsolate toye sabad kharid
		cart_quantity = cart.__len__()
  
		response = JsonResponse({'qty': cart_quantity})
		messages.success(request, ("محصول به سبد خرید اضافه شد"))
		return response


#delete a product in sabad kharid
def cart_delete(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		product_id = int(request.POST.get('product_id'))
		cart.delete(product=product_id)
		response = JsonResponse({'product':product_id})
		messages.success(request, ("از سبدخرید حذف شد..."))
		return response

#update and edit sabad kharid
def cart_update(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))
		cart.update(product=product_id, quantity=product_qty)
		response = JsonResponse({'qty':product_qty})
		messages.success(request, ("سبد خرید بروزرسانی شد..."))
		return response
