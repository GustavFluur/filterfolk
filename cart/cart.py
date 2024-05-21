from product.models import Product


class Cart():
	
	def __init__(self, request):
		self.session = request.session
		self.request = request
		cart = self.session.get('session_key')

		if 'session_key' not in request.session:
			cart = self.session['session_key'] = {}

		self.cart = cart

	def add(self, product, quantity):
			product_id = str(product.id)
			product_qty = str(quantity)

			if product_id in self.cart:
				pass
			else:
				self.cart[product_id] = int(product_qty)

			self.session.modified = True

			if self.request.user.is_authenticated:
				# Get the current user profile
				current_user = Profile.objects.filter(user__id=self.request.user.id)
				# Convert {'3':1, '2':4} to {"3":1, "2":4}
				carty = str(self.cart)
				carty = carty.replace("\'", "\"")
				# Save carty to the Profile Model
				current_user.update(old_cart=str(carty))


	def __len__(self):
			return len(self.cart)


	def get_cart_items(self):
			# Get ids from cart
			product_ids = self.cart.keys()
			# Use ids to lookup products in database model
			products = Product.objects.filter(id__in=product_ids)

			# Return those looked up products
			return products