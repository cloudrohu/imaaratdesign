from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import home
from home import views 
from django.utils.translation import gettext_lazy as _

from django.views.generic import RedirectView
urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('logout/',RedirectView.as_view(url = '/admin/logout/')),



    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path(('contactus/'), views.contactus, name='contactus'),
    path(('faqs/'), views.faqs, name='faqs'),
    path(('product/'), views.product, name='product'),
    path(('brand/'), views.BRAND, name='brand'),
    path(('gallery/'), views.Gallery, name='gallery'),

    path(('about/'), views.aboutus, name='aboutus'),
    path(('our-team/'), views.Our_Team, name='our-team'),
    path(('vision-mission/'), views.Vision_Mission, name='vision-mission'),
    path(('director-desk/'), views.DirectorDesk, name='director-desk'),


    path(('architecture/'), views.Architecture, name='architecture'),
    path(('construction/'), views.Construction, name='construction'),
    path(('interior/'), views.Interior, name='interior'),
    path(('landscape/'), views.Landscape, name='landscape'),
    path(('turnkey/'), views.Turnkey, name='turnkey'),


    path(('blog/'), views.BLOG, name='blog'),
    path(('real-estate/'), views.REALESTATE, name='real-estate'),


    path(('project/'), views.project, name='project'),
                                                                                                                                                                                                 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
