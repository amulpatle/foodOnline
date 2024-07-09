from .models import Cart
from menu.models import FoodItem

def get_cart_counter(reqeust):
    cart_count = 0
    if reqeust.user.is_authenticated:
        try:
            cart_items = Cart.objects.filter(user=reqeust.user)
            if cart_items:
                for cart_item in cart_items:
                    cart_count += cart_item.quantity
            else:
                cart_count = 0
        except:
            cart_count = 0
    return dict(cart_count=cart_count )