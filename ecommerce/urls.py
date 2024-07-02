
from django.urls import path
from . import views
from .views import CategoryView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from .forms import MyPasswordResetform,MySetPasswordForm
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [

    path('', views.home),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name="contact"),
    path("category/<slug:val>",views.CategoryView.as_view(),name='category'),
    path("category-title/<val>",views.CategoryTitle.as_view(),name='category-title'),
    path("product-detail/ <int:pk>",views.ProductDetail.as_view(),name='product-detail'),
    path('profile/' ,views.CustomerProfile,name='profile'),
    path('address/' ,views.address,name='address'),
    path('updateaddress/<int:id>' ,views.UpdateAddress,name='updateaddress'),


    path('add-to-cart/',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.show_cart,name='showcart'),
    path('checkout/',views.checkout.as_view(),name='checkout'),
    path('paymentdone/',views.payment_done, name="payment_done"),
    path('orders/',views.orders,name='orders'),

    path('search/',views.search,name='search'),
    path('wishlist/',views.show_wishlist,name='showwishlist'),

    path('pluscart',views.plus_cart),
    path('minuscart',views.minus_cart),
    path('removecart',views.remove_cart),
    path('pluswishlist/',views.plus_wishlist),
    path('minuswishlist/',views.minus_wishlist),

    # authrntication section
    
    path('register',views.register ,name='register'), 
    path('login',views.login ,name='login'), 
    path('logout',views.logout,name='logout'),
    path('change_password', views.change_password, name='change_password'),
   
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'password_reset.html',form_class= MyPasswordResetform),name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'),name='password_reset_complete'),

    
   
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Dairy Products"
admin.site.site_title = "Dairy Products"
admin.site.site_index_title = "Welcome to Dairy Shop"