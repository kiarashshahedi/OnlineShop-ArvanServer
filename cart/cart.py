from products.models import Product
from custom_loggin.models import MyUser


class Cart():
    
	def __init__(self, request):
     
		self.session = request.session		
		self.request = request						# Get request
		cart = self.session.get('session_key')		# Get the current session key if it exists
		
		if 'session_key' not in request.session:	# If the user is new, no session key!  Create one!
			cart = self.session['session_key'] = {}
   		
		self.cart = cart							# Make sure cart is available on all pages of site


	def add(self, product, quantity):
     
		product_id = str(product.id)
		product_qty = str(quantity)
		if product_id in self.cart:
			pass

		else:
			self.cart[product_id] = int(product_qty)

		self.session.modified = True

		if self.request.user.is_authenticated:										# Deal with logged in user			
			current_user = MyUser.objects.filter(user__id=self.request.user.id)     # Get the current user profile			
			carty = str(self.cart)   												# Convert {'3':1, '2':4} to {"3":1, "2":4}
			carty = carty.replace("\'", "\"")			
			current_user.update(old_cart=str(carty))    							# Save carty to the MyUser Model


	def cart_total(self):
		
		product_ids = self.cart.keys()				               # Get product IDS		
		products = Product.objects.filter(id__in=product_ids)      # lookup those keys in our products database model		
		quantities = self.cart				                       # Get quantities		
		total = 0				                                   # Start counting at 0
		
		for key, value in quantities.items():
			# Convert key string into into so we can do math
			key = int(key)
			for product in products:
				if product.id == key:
					if product.in_sale:
						total = total + (product.sale_price * value)
					else:
						total = total + (product.price * value)

		return total


	#show counts of cart buton in navbar 
	def __len__(self):
     
		return len(self.cart)


	#find product for showing in cart page
	def get_prods(self):
		
		product_ids = self.cart.keys()                           # Get ids from cart (pk of products)		
		products = Product.objects.filter(id__in=product_ids)    # Use ids to lookup products in database model		
		return products                                           # Return those looked up products


	def get_quants(self):
     
		quantities = self.cart
		return quantities


	def update(self, product, quantity):
     
		product_id = str(product)
		product_qty = int(quantity)
		ourcart = self.cart						# Get cart
		ourcart[product_id] = product_qty		# Update Dictionary/cart

		self.session.modified = True
		thing = self.cart
		return thing

	def delete(self, product):
     
		product_id = str(product)
		if product_id in self.cart:				# Delete from dictionary/cart
			del self.cart[product_id]
		self.session.modified = True  
        
        
	def product_total(self):
		product_ids = self.cart.keys()                              
		products = Product.objects.filter(id__in=product_ids)      
		quantities = self.cart                                       
		product_totals = {}  # Dictionary to store total price for each product
		
		for key, value in quantities.items():
			key = int(key)
			for product in products:
				if product.id == key:
					if product.in_sale:
						product_totals[key] = product.sale_price * value
					else:
						product_totals[key] = product.price * value

		return product_totals
