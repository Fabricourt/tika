from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from booking.models import About, Lessee, Truck, Lessor, Onhire, Booktruck
from django.contrib.admin.views.decorators import staff_member_required
from contact.forms import ContactForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

#index
def index(request):
  abouts = About.objects.order_by('-reload').filter(is_published=True)[:1]
  booktrucks = Booktruck.objects.order_by('-timestamp').filter(is_published=True)

  if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent')
            return redirect('contact')
      
  else:
        form = ContactForm()
    
  
  context = {
    'form': form,
    'abouts': abouts,
    'booktrucks': booktrucks, 
  }
  return render(request, 'booking/index.html', context)





#about
def about(request):
  abouts = About.objects.order_by('-reload').filter(is_published=True)[:1]

  context = {
      'abouts': abouts,
  }
  return render(request, 'booking/about.html', context)






#dashboard
@staff_member_required
def dashboard(request):
    trucks = Truck.objects.order_by('-timestamp').filter(is_published=True)
    lessees = Lessee.objects.order_by('-timestamp').filter(is_published=True)
    lessors = Lessor.objects.order_by('-timestamp').filter(is_published=True)
    onhires = Onhire.objects.order_by('-hire_date').filter(is_published=True)
    booktrucks = Booktruck.objects.order_by('-booking_date').filter(is_published=True)
    
    context = {
      'trucks' : trucks,
      'lessees' : lessees,
      'lessors' : lessors,
      'onhires' : onhires,
      'booktrucks' : booktrucks,

    }
    return render(request, 'booking/dashboard.html', context)


#register
def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being used')
          return redirect('register')
        else:
          # Looks good
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
          # Login after register
          # auth.login(request, user)
          # messages.success(request, 'You are now logged in')
          # return redirect('index')
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('login')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register')
  else:
    return render(request, 'booking/register.html')

#login
def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('index')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'booking/login.html')

#logout
def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')

#login
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'booking/profile.html', context)


