from django.shortcuts import render


def get_about_edu_org_page(request):
    return render(request, 'app_about_us/about_edu_org.html', {})
