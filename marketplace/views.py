from django.shortcuts import get_object_or_404, render

from vendor.models import Vendor

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
    context = {
        'vendor':vendor,
    }
    return render(reqeust,'marketplace/vendor_detail.html',context)