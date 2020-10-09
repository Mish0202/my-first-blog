from django.shortcuts import render, get_object_or_404
def post_list(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
    


# Create your views here.
