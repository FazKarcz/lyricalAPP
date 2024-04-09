from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Comment
from song.models import Song


@login_required
def add_comment(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        comment = Comment(song=Song, user=request.user, content=content)
        comment.save()

    return render(request, 'add_comment.html', {'song': song})


# Create your views here.
