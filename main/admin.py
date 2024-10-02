from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (Category, Product, ProductSpecification, 
                     Services, Comments, Contact, 
                     UserContact, Team, NewsLetter)
# Register your models here.

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", )

    inlines = [
        ProductInline,
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price", 'view_image')
    list_editable = ("price", )

    def view_image(self, product):
        return mark_safe(f'<img src="{product.image.url}" width="60" height="60" />')
    
    view_image.short_description = "Image"



@admin.register(ProductSpecification)
class ProductSpecificationAdmin(admin.ModelAdmin):
    list_display = ("product", "text")


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "text", "created_at")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(UserContact)
class UserContactAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "subject")


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("fullname", "job")


admin.site.register(NewsLetter)