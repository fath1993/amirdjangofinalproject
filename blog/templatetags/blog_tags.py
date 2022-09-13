from django import template

from blog.models import Post, Category, Comment

register = template.Library()


@register.inclusion_tag('blog/blog-popular-posts.html')
def latest_posts():
    posts = Post.objects.filter(status=1).order_by('published_date')[:4]
    return {'posts': posts}


@register.simple_tag(name='comment_count')
def function(pid):
    post = Post.objects.get(pk=pid)
    return Comment.objects.filter(post=post.id, approved=True).count()


@register.inclusion_tag('blog/blog-post-categories.html')
def post_categories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}
