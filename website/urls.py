from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name = 'index'),
	path('contact',views.contact, name = 'contact'),
	path('about',views.about,name = 'about'),
	path('pricing',views.pricing,name = 'pricing'),
	path('service',views.service,name = 'service'),
	path('blog',views.blog,name = 'blog'),
	path('blog_detail',views.blog_detail,name = 'blog_detail'),
	path('appointment',views.appointment,name = 'appointment'),
]