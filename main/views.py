from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

from .models import *
# Create your views here.



class HomePageView(View):
    def get(self, request):

        last_product = Product.objects.last()

        query = request.GET.get('q')
        if query:
            products = Product.objects.filter(title__icontains=query)
        else:
            products = Product.objects.all()

        data = {
            'products': products,
            'last_product': last_product,
            'query': query
        }

        return render(request, "index.html", data)
    

class ShopPageView(View):
    def get(self, request):

        products = Product.objects.all()
        last_product = Product.objects.last()

        category = Category.objects.all()


        data = {
            'products': products,
            'last_product': last_product,
            'category': category,
        }

        return render(request, "product.html", data)
    

class ServicesView(View):
    def get(self, request):

        services = Services.objects.all()

        data = {
            "services": services,
            "title": "Services"
        }
        return render(request, "services.html", data)

    def post(self, request):

        email = request.POST.get('email')
        if email:
            NewsLetter.objects.create(email=email)
        return redirect(reverse('services'))


    

class ContactPageView(View):
    def get(self, request):

        data = {
            "title": "Contact",
            "contact": Contact.objects.first()
        }

        return render(request, "contact.html", data)

    def post(self, request):
        
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        content = request.POST.get("message")
    
        if firstname and lastname and email and subject and content:
            UserContact.objects.create(firstname=firstname, lastname=lastname, email=email, subject=subject, content=content)
            messages.success(request, "Habar yuborildi!")
            return redirect(reverse("contact"))


class SingleProductView(View):
    def get(self, request, product_slug):

        product = Product.objects.get(slug=product_slug)
        comments = product.comments.all()
        product_specif = ProductSpecification.objects.filter(product=product)

        data = {
            "product": product,
            "product_specif": product_specif,
            "comments": comments,
            "title": "Single",
        }

        return render(request, "single.html", data)

    @method_decorator(login_required)
    def post(self, request, product_slug):
        
        product = Product.objects.get(slug=product_slug)
        comment = request.POST.get('comment')

        if comment:
            Comments.objects.create(product=product, user=request.user, text=comment)

        return redirect('single', product_slug=product.slug)
    

class AboutPageView(View):
    def get(self, request):

        data = {
            "title": "About",
            "team": Team.objects.all() ,
            "last_product": Product.objects.last()
        }

        return render(request, "about.html", data)
    

class CategoryView(View):
    def get(self, request, category_id):
        
        category_product = Category.objects.get(id=category_id)
        product = Product.objects.filter(category=category_product)

        data = {
            "category": category_product,
            "products": product,
        }
        
        return render(request, "category.html", data)

