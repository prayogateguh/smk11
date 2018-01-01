from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from taggit.models import Tag

from .forms import CommentForm, PostForm
from .models import Comment, Post


def index(request):
    return render(request, 'html5up/base.html', {})

def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published',)

    # list of active comments for this post
    comments = post.comments.filter(active=True)
    new_comment = ''
    if request.method == 'POST':
        # a comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # create comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # assign the current post to the comment
            new_comment.post = post
            # save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    # related post based on its tags
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]

    return render(request, 'news/post/detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form, 'new_comment': new_comment, 'similar_posts': similar_posts,})

def post_list(request, tag_slug=None):
    posts = Post.published.all()
    
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    return render(request, 'news/post/list.html', {'posts': posts, 'tag': tag})

@permission_required('berita.can_post_news')
def add_post(request):
    if request.method == 'POST':
        posting = PostForm(request.POST, request.FILES or None)
        if posting.is_valid():
            obj = posting.save(commit=False)
            obj.author = request.user
            obj.save()
            posting.save_m2m()
        return HttpResponseRedirect('/berita/')
    else:
        posting = PostForm()
        return render(request, 'news/post/add.html', {'posting': posting,})

@permission_required('berita.can_post_news')
def del_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('berita:all_posts')

    return render(request, 'news/post/del_post.html', {'post': post,})

@permission_required('berita.can_post_news')
def all_posts(request):
    posts = Post.published.all()
    drafts = Post.drafted.all()

    return render(request, 'news/post/all_posts.html', {'posts': posts, 'drafts': drafts,})

@permission_required('berita.can_post_news')
def edit_post(request, pk):

    post = get_object_or_404(Post, pk=pk)
    title = post.title

    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    if request.POST and form.is_valid():
        form.save()

        # Save was successful, so redirect to another page
        return redirect('berita:all_posts')

    return render(request, 'news/post/edit.html', {'form': form, 'title': title,})
