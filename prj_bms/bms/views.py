from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin
from django.views import generic
from .models import Category, Brand, Shop, Invoice, Quantity, Shift , BmsUser
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in

import datetime


@receiver(user_logged_in)
def sig_user_logged_in(sender, user, request, **kwargs):
    request.session['isLoggedIn'] = True
    request.session['isAdmin'] = True
    request.session['email'] = user.email
    request.session['username'] = user.username
    username  = request.session.get('username')
    request.session['userid'] = user.id
    request.session['isBmsUser'] = True

    # request.session['emp_id'] = EmpProfile.objects.filter(username_id__exact = request.user.id).values('emp_id')[0]['emp_id']
    
    isLoggedIn = request.session.get('isLoggedIn',False)
    isAdmin = request.session.get('isAdmin',False)
    email = request.session.get('email','')
    emp_id = request.session.get('emp_id')
    request.session.save()

    return render(
        request,
        'registration/login.html',
        context = {'isLoggedIn':isLoggedIn,'isAdmin':isAdmin,'email':email, 'emp_id':emp_id},
    )






class ShopListView(generic.ListView):
    context_object_name = 'shop_list'
    model = Shop
    queryset = Shop.objects.all()
    template_name = 'stocks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        isAdmin = self.request.session['isAdminUser']
        context = { "isAdmin" : isAdmin}
        userid = self.request.user.id
        context['user'] = self.request.user
        context['bms_users'] = BmsUser.objects.all()
        context['shop_list'] = self.model.objects.filter(shop_admin = userid)
        return context
 
     
class ShopDetailView( generic.DetailView):
    model = Shop
    template_name = "shop_details.html"
    
    def shop_detail_view(request, primary_key):
        shop = get_object_or_404(Shop, pk=primary_key)
        return render(request, context={'shop': shop})


class AdminView(LoginRequiredMixin, generic.ListView):
    model = BmsUser
    template_name = "home_page.html"
    login_url = '/login/'

    # def get(self, request):
        

    
    def get_context_data(self, **kwargs):
        
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        isAdmin = self.request.session['isAdminUser']
        print(isAdmin)
        context = { "isAdmin" : isAdmin}

            
        # Add in a QuerySet of all the books
        context['bms_users'] = BmsUser.objects.all()
        context['bms_suadmin'] = BmsUser.objects.filter(user_role="S")
        return context

class AdminDetailsView(generic.DetailView):
    def get(self, request, *args, **kwargs):
        list = Shop.objects.filter(shop_admin=kwargs['pk'])
        user= get_object_or_404(BmsUser, pk=kwargs['pk'])
        context= {'shop_list':list, 'b_user':user}
        return render (request, "subadmin_page.html", context)
    # model = BmsUser
    # template_name = "subadmin_page.html"
    # # login_url = '/login/'
     
    # def get_context_data(request, primary_key):
    #     sub = get_object_or_404(BmsUser, pk=primary_key)
    #     print(primary_key)
    #     shop_list = Shop.objects.filter(shop_admin = primary_key)
    #     print(shop_list)
    #     return render(request, context={'sub': sub, 'shop_list':shop_list, })


def HomeView(request, id=None):
    # user = get_object_or_404(User, id=id) 
    # user = get_object_or_404(User) 
    request.session['userid'] = request.user.id
    id = request.session.get('userid')
    isAdminUser = False  # create the user seesion for admin true
    request.session['isAdminUser'] = isAdminUser
    print(id)
    try:
        bms_role=BmsUser.objects.filter(username = id).values('user_role')[0]['user_role']
        request.session['isBmsUser'] = True
    except:
        request.session['isBmsUser'] = True
        # context = {'isLoggedIn':isLoggedIn,}

        return HttpResponseRedirect("/error/")

    if bms_role =='A':
        print("You are admin")
        request.session['isBmsUser'] = True
        request.session['isAdminUser'] = True
        return HttpResponseRedirect("/home/")
    else:
        # bms_role_s=BmsUser.objects.all().filter(username = id, user_role = 'S').values('user_role')[0]['user_role']
        if bms_role =='S':
            print ("you are subadmin ")
            request.session['isBmsUser'] = True
            return HttpResponseRedirect("/shop/")
        else:
            request.session['isBmsUser'] = True
            print("You are shopkeeper")




















    # if request.method == "POST":
    #     emp.delete()
    #     return HttpResponseRedirect("/employee/")
    # context = { "emp" : emp }
    # template = "ems/delete-view.html"
    # return render(request, template, context )