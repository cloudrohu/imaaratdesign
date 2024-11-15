from django.contrib import admin
import admin_thumbnails

from .models import *
# Register your models here.

@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    list_display = ['id']
    model = Images
    readonly_fields = ('id',)
    extra = 1





class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','image_tag','featured_project', 'Top_Deals_Of_The_Day','Top_Selling_Products','Recommended_For_You', 'slug', 'create_at','update_at',]
    list_editable = ['featured_project', 'Top_Deals_Of_The_Day','Top_Selling_Products','Recommended_For_You']
    inlines = [ProductImageInline,]

admin.site.register(Product,ProductAdmin)

admin.site.register(Images)
admin.site.register(Comment)



