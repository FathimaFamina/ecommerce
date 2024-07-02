from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import Product,Customer,Cart,Payment,OrderPlaced,Wishlist

from django.views import View
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
from django.db.models import Q
from django.conf import settings
import razorpay
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




# Create your views here.

def home(request):
    # this code is to show cart item number as banner 
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
        # end cart banner number code
    return render(request,"home.html",locals())
@login_required
def about(request):
    # this code is to show cart item number as banner 
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
        # end cart banner number code
    return render(request,"about.html",locals())
@login_required
def contact(request):
    # this code is to show cart item number as banner 
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
        # end cart banner number code
    return render(request,"contact.html",locals())


@method_decorator(login_required,name='dispatch')
class CategoryView(View):
    def get(self,request,val):
        # this code is to show cart item number as banner 
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
            # end cart banner number code
        products = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,'category.html',locals() )
    





@method_decorator(login_required,name='dispatch')
class CategoryTitle(View):
    def get(self,request,val):
        # this code is to show cart item number as banner 
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
            # end cart banner number code
        products = Product.objects.filter(title=val)
        title = Product.objects.filter(category=products[0].category).values('title')
        return render(request,'category.html',locals() )



@method_decorator(login_required,name='dispatch')
class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
        # this code is to show cart item number as banner 
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
            # end cart banner number code
        return render(request,'productdetail.html',locals())



@method_decorator(login_required,name='dispatch')
class profileView(View):
   def get(self,request):
    # this code is to show cart item number as banner 
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
        # end cart banner number code
    return render(request,'profile.html',locals())

   def post(self,request):
      return render(request,'profile.html',locals())


    
def register(request): 
   if request.method == 'POST' : 
      first_name=request.POST['first_name'] 
      last_name=request.POST['last_name'] 
      username=request.POST['username'] 
      email=request.POST['email'] 
      password1=request.POST['password1'] 
      password2=request.POST['password2'] 
       
      
 
 
      if password1 == password2 : 
         if User.objects.filter(username=username).exists(): 
             messages.info(request,'username is taken') 
             return redirect('register') 
         elif User.objects.filter(email=email).exists()  : 
            messages.info(request,'email is taken') 
            return redirect('register') 
         else:      
            user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name) 
            user.save(); 
            
            messages.success(request,"congratulation User Registered Successfully") 
      else: 
         messages.warning(request,'password is not matching  ') 
          
         return redirect('register') 
      return redirect('/')  
   else: 
      return render(request,'register.html')   
    
 
def  login(request): 
   if request.method == 'POST': 
      username=request.POST.get('username') 
      password=request.POST.get('password') 
       
     
 
      user =auth.authenticate(username=username,password=password) 
       
      if user is not None: 
         auth.login(request,user) 
         return redirect('/')  
      else: 
         messages.info(request,'invalid credentials') 
         return redirect('login') 
   else: 
      return render(request,'login.html') 
      
def logout(request): 
   auth.logout(request) 
   return redirect('login')  

@login_required
def CustomerProfile(request):
    # this code is to show cart item number as banner 
   totalitem = 0
   wishitem = 0
   if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
        # end cart banner number code
   if request.method == 'POST' : 
       user= request.user
       name =request.POST['name']
       locality =request.POST['locality'] 
       city =request.POST['city'] 
       mobile =request.POST['mobile'] 
       zipcode =request.POST['zipcode'] 
      

       customer = Customer.objects.create(user=user, name=name, locality=locality, city=city, mobile=mobile, zipcode=zipcode)
       print(user)
       customer.save()
        
       messages.success(request,"congratulation ! your details are saved successfully ")
         
   return render(request, 'profile.html',locals())

@login_required
def address(request):
    # this code is to show cart item number as banner 
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
        # end cart banner number code
    add = Customer.objects.filter(user = request.user)
    return render(request,'address.html',locals())
    


@login_required    
def UpdateAddress(request,id):
    # this code is to show cart item number as banner 
    totalitem = 0
    wishitem =0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
        # end cart banner number code
    customer = Customer.objects.get(id=id)
    if request.method == 'POST':
        user = request.user
        name =request.POST['name']
        locality = request.POST['locality']
        city = request.POST['city']
        mobile = request.POST['mobile']
        zipcode = request.POST['zipcode']

        customer.name=name
        customer.locality = locality
        customer.city = city
        customer.mobile = mobile
        customer.zipcode = zipcode
        customer.save()

        messages.success(request, "Your address has been updated successfully.")
        return redirect('profile')

    return render(request, 'update_address.html',{"user":customer})




@login_required
def change_password(request):
    # this code is to show cart item number as banner 
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
        # end cart banner number code
    if request.method == 'POST':
        user = request.user
        current = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        
        check = user.check_password(current)
        
        if check:
            # Current password is correct
            if new_password == confirm_password:
                # Update the user's password
                user.set_password(new_password)
                user.save()
                return render( request,'success.html')
            else:
                # New password and confirm password don't match
                return render(request, 'change_password.html', {'error': 'New password and confirm password do not match.'})
        else:
            # Current password is incorrect
            return render(request, 'change_password.html', {'error': 'Incorrect current password.'})

       
    
    return render(request, 'change_password.html')


@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    
    if product_id:
        product = get_object_or_404(Product, id=product_id)
        Cart(user=user, product=product).save()
        return redirect("/cart")
    
    # Handle the case where no valid product_id is provided
    return HttpResponse("Invalid product ID")

@login_required
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount =0
    for p in cart:
       value = p.quantity * p.product.discounted_price
       amount= amount + value
    totalamount = amount + 40    
    # this code is to show cart item number as banner 
    totalitem = 0
    wishitem =0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
        # end cart banner number code
    return render( request,'addtocart.html',locals())


@method_decorator(login_required,name='dispatch')
class checkout(View):
    def get(self,request):
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount =0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = famount+value
        totalamount = famount + 40  
        razoramount = int(totalamount *100)
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))
        data = {'amount':razoramount,'currency': "INR",'receipt':'oder_rcptid_11'}
        payment_response = client.order.create(data=data)
        print(payment_response) 
        # {'id': 'order_M44kek6kGP9Exw', 'entity': 'order', 'amount': 70000, 'amount_paid': 0, 'amount_due': 70000, 'currency': 'INR', 'receipt': 'oder_rcptid_11', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1687240401}

        order_id = payment_response['id']
        order_status = payment_response['status']
        if order_status == 'created':
            payment = Payment(
                user = user,
                amount = totalamount,
                razorpay_orderid=order_id,
                razorpay_payment_status = order_status
            )
            payment.save()
        return render(request,'checkout.html',locals())
    

@login_required
def payment_done(request):
    order_id = request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')
    cust_id = request.GET.get('cust_id')
    print(cust_id)
    user = request.user
    
    try:
        customer = get_object_or_404(Customer, id=cust_id)
        
        try:
            payment = Payment.objects.get(razorpay_orderid=order_id)
            payment.paid = True
            payment.razorpay_payment_id = payment_id
            payment.save()
            
            # Save order details
            cart = Cart.objects.filter(user=user)
            for c in cart:
                OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity, payment=payment).save()
                c.delete()
            
            return redirect('orders')
        
        except Payment.DoesNotExist:
            # Handle the case when payment does not exist
            # For example, you can return an error response or redirect to an error page
            return HttpResponse('Payment does not exist')
    
    except Customer.DoesNotExist:
        # Handle the case when customer does not exist
        # For example, you can return an error response or redirect to an error page
        return HttpResponse('Customer does not exist')


@login_required
def orders(request):
    # this code is to show cart item number as banner 
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
        # end cart banner number code
    order_placed =OrderPlaced.objects.filter(user=request.user)
    return render(request,'orders.html',locals())
    


@login_required
def plus_cart(request):
    if request.method == 'GET' :

        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id)&Q(user=request.user))
        c.quantity += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount =0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        data = {
            'quantity':c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
    return JsonResponse(data)    



@login_required
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id)& Q(user = request.user))
        c.quantity-=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount =0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        data = {
            'quantity':c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
    return JsonResponse(data)    

@login_required
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id)& Q(user = request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount =0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        data = {
            'quantity':c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
    return JsonResponse(data)    





@login_required 
def plus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        product = get_object_or_404(Product, id=prod_id)
        wishlist, created = Wishlist.objects.get_or_create(user=request.user, product=product)
        
        if created:
            message = 'Wishlist Added Successfully'
        else:
            message = 'Product already in wishlist'
        
        data = {
            'message': message
        }
        return JsonResponse(data)

@login_required
def minus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        wishlist = Wishlist.objects.filter(user=request.user, product_id=prod_id).first()
        
        if wishlist:
            wishlist.delete()
            message = 'Wishlist removed Successfully'
        else:
            message = 'Product not found in wishlist'
        
        data = {
            'message': message
        }
        return JsonResponse(data)


@login_required   
def search(request):
    query = request.GET['search']
    # this code is to show cart item number as banner 
    totalitem = 0
    wishitem =0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
        # end cart banner number code
    product = Product.objects.filter(Q(title__icontains=query))
    return render(request,'search.html',locals())



@login_required
def show_wishlist(request):
    user = request.user
    # this code is to show cart item number as banner 
    totalitem = 0
    wishitem =0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
        # end cart banner number code
    product = Wishlist.objects.filter(user=user)
    return render(request,'wishlist.html',locals())



