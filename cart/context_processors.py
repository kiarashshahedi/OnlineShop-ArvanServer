from .cart import Cart

#Create context proccessors FOR working Cart in All pages/parts of Our shopping site
def cart(request):
    #returns the default data from our Cart
    return {'cart': Cart(request)}