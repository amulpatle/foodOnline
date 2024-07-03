from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from vendor.models import Vendor
from menu.models import Category, FoodItem
from django.db.models import Prefetch
def marketplace(request):
    vendors = Vendor.objects.filter(is_approved=True,user__is_active=True)
    vendor_count = vendors.count()
    context = {
        'vendors':vendors,
        'vendor_count':vendor_count,
    }
    return render(request,'marketplace/listings.html',context)


def vendor_detail(reqeust,vendor_slug):
    vendor = get_object_or_404(Vendor,vendor_slug=vendor_slug)
    categories = Category.objects.filter(vendor=vendor).prefetch_related(
        Prefetch(
            'fooditems',
            queryset = FoodItem.objects.filter(is_availabe=True)
        )
    )
    
    context = {
        'vendor':vendor,
        'categories':categories,
    }
    return render(reqeust,'marketplace/vendor_detail.html',context)


def add_to_cart(request,food_id):
    return HttpResponse('Testing')