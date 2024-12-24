from django.shortcuts import render
from .models import *

def home(request):
    home_banner = HomeBanner.objects.first()  # Replace with actual query
    home_about = HomeAbout.objects.first()
    our_services = OurServiceData.objects.all()
    products = OurProduct.objects.all()
    competitive_images = CompetitiveAdvantageImg.objects.all()
    competitive_info = CompetitiveAdvantageInfo.objects.all()
    how_we_work_items = HowWeWork.objects.all()
    why_choose_us = WhyChooseUs.objects.all()
    blog_post = BlogPost.objects.all()
    collaborations = GlobalCollaboration.objects.all()
    offices = GlobalCollaborationOffice.objects.all()
    context = {
        'home_banner': home_banner,
        'home_about': home_about,
        'our_services': our_services,
        'products': products,
        'competitive_images': competitive_images,
        'competitive_info': competitive_info,
        'how_we_work_items': how_we_work_items,
        'why_choose_us': why_choose_us,
        'blog_post': blog_post,
        'collaborations': collaborations,
        'offices': offices,
    }
    return render(request, 'index.html',context)
