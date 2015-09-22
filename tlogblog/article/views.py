from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect#to redirect user to a different site
from django.contrib.auth import authenticate,logout as django_logout # for authentication
from django.contrib.auth import login as auth_login
from django.core.context_processors import csrf 
from article.forms import ArticleForm
from article.forms import CommentForm
from article.forms import QuoteForm
from tlogblog.forms import MyRegistrationForm
from tlogblog.forms import UserAdminAuthenticationForm
from django.views.generic.list import ListView
from django.contrib.sitemaps import Sitemap
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from article.models import Article
from article.models import Quote

# Create your views here.
def articles(request):

    args = {}
    #args.update(csrf(request))

    args['articles'] = Article.objects.all()
    args['quote'] = Quote.objects.all()

    return render_to_response('articles.html', args)


##################################################################################
#default articlesview here
def articlesview(request):

    args = {}
    #args.update(csrf(request))

    args['articles'] = Article.objects.all()[:7]
    args['quote'] = Quote.objects.all()[:7]

    return render_to_response('articlesview.html', args)


def article(request, article_id = 1):#getting data individually
    return render(request,'article.html',{'article':Article.objects.get(id = article_id) })
###############################################################################################
#extending the model class 
#
@login_required
def create(request):
    if request.POST:
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/articles/')
    else:
        form = ArticleForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render(request,'create_article.html',args)
@login_required
def newquote(request):
    if request.POST:
        form = QuoteForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/articles/')
    else:
        form = QuoteForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render(request,'newquote.html',args)

#########################################################################################
#to register user.
def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success/')


    args = {}
    args.update(csrf(request)),
    args['form'] = MyRegistrationForm()

    return render(request,'register.html',args)



def register_success(request):
    return render(request,'register_success.html')

###################################################################################
########sitemap can be placed anywhere from the docs.
#sitemap class instance  here
class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.4

    def items(self):
        return Article.objects.filter()

    def lastmod(self, obj):
        return obj.pub_date



#####################################################################################
#for authentication........
def login(request):
    c = {}
    c.update(csrf(request))

    c['login_form'] = UserAdminAuthenticationForm()

    return render(request,'login.html',c)

######here.....
def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = authenticate(username = username,password = password) #says user now exists

    if user is not None:
        auth_login(request,user) #says user is now logged in
        return HttpResponseRedirect('/articles/')
    else:
        return HttpResponseRedirect('/accounts/invalid/')

def loggedin(request):
    return render(request,'loggedin.html',{'full_name':request.user.username}) 


def invalid_login(request):
    return render(request,'invalid_login.html')

@login_required
def logout(request):
    django_logout(request)
    return render(request,'logout.html')

################################################################################
#to list updated article for blog on sidebar....
class ArticleListView(ListView):

    model = Article
    template_name = 'article_list.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
'''
class UserSignupView(TemplateView):
  template_name = 'account/signup.html'

  def get_context_data(self, **kwargs):
    auth_token = unicode(csrf(self.request)['csrf_token'])
    context = super(UserSignupView,self).get_context_data(**kwargs)
    context['csrf_token'] = auth_token
    return context
'''


 