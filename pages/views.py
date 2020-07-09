from django.shortcuts import render

from stories.models import Story


def index(request):
    stories = Story.objects.order_by('-pub_date').filter(is_published=True)
    context = {
        'stories': stories
    }
    return render(request, 'pages/index.html', context)
