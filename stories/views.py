from django.shortcuts import render, get_object_or_404

from .models import Story


def index(request):
    stories = Story.objects.order_by('-pub_date').filter(is_published=True)
    context = {
        'stories': stories
    }
    return render(request, 'stories/stories.html', context)


def story(request, story_id):
    story = get_object_or_404(Story, pk=story_id)

    context = {
        'story': story
    }
    return render(request, 'stories/story.html', context)

    return render(request, 'stories/story.html')
