from django.shortcuts import render
from .models import *
from process.models import ProcessData
from metadata.models import UnifiedModel




def home(request):
    home_banner = HomeBanner.objects.first()
    banner_images = []
    if home_banner and not home_banner.is_video:
        banner_images = HomeBannerImage.objects.filter(home_banner=home_banner)

    context = {
        'home_banner': home_banner,
        'banner_images': banner_images,
        'home_about': HomeAbout.objects.first(),
        'our_services': OurServiceData.objects.all(),
        'feature_slider': FeatureSlider.objects.all(),
        'feature_slider_image': FeatureSliderImage.objects.all(),
        'products': OurProduct.objects.all(),
        'competitive_images': CompetitiveAdvantageImg.objects.all(),
        'competitive_info': CompetitiveAdvantageInfo.objects.all(),
        'how_we_work_items': HowWeWork.objects.all(),
        'why_choose_us': WhyChooseUs.objects.all(),
        'blog_post': BlogPost.objects.all(),
        'collaborations': GlobalCollaboration.objects.all(),
        'offices': GlobalCollaborationOffice.objects.all(),
        'process_data': ProcessData.objects.all(),
        'unified_model': UnifiedModel.objects.last()
    }
    return render(request, 'index.html', context)
