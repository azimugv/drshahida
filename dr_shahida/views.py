from django.shortcuts import render, redirect
from dr_shahida.models import BlogPost
from .translation import my_dict
from django.utils.translation import to_locale, get_language



our_lang = ['en', 'bn']


def get_lang(request):
    if 'lang' in request.COOKIES:
        ln = request.COOKIES['lang']
        if ln in our_lang:
            pass
        else:
            return 'en'
    else:
        x = to_locale(get_language())
        x = x.split('_')[0]
        if x in our_lang:
            ln = x
        else:
            ln = 'en'
    return ln

def set_lang(request, ln):
    language = ln
    addr = request.META.get('HTTP_REFERER')
    response = redirect(addr)
    response.set_cookie('lang', language)
    return response


# Changing language url http://127.0.0.1:8000/set_language/bn

def index(request):
    blog_posts = BlogPost.objects.filter(show_on_home='True')
    ln = get_lang(request)
    context = {
        'blog_posts': blog_posts,
        'lang': my_dict[ln],
        'selected_lang' : ln
    }

    

    return render(request, 'dr_shahida/index.html', context=context)



def testimonial(request):
    ln = get_lang(request)
    context = {
        'lang': my_dict[ln],
        'selected_lang' : ln
    }


    return render(request, 'dr_shahida/testimonial.html', context=context)



def contact(request):
    ln = get_lang(request)
    context = {
        'lang': my_dict[ln],
        'selected_lang' : ln
    }

    return render(request, 'dr_shahida/contact.html', context=context)


def blog(request):
    blog_posts = BlogPost.objects.all()
    ln = get_lang(request)
    context = {
        'blog_posts':blog_posts,
        'lang': my_dict[ln],
        'selected_lang' : ln
    }

    return render(request, 'dr_shahida/blog.html', context=context)

def blogdetailview(request,post_id):
    blog_post = BlogPost.objects.get(pk=post_id)
    blog_posts = BlogPost.objects.all()

    ln = get_lang(request)
    context = {
        'blog_post':blog_post, 
        'lang': my_dict[ln],
        'selected_lang' : ln
    }
    

    return render(request, 'dr_shahida/detail.html', context=context)