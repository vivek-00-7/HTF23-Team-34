from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
# Create your views here.

@login_required
def dashboard(request):
    if request.method == 'POST':

        equipment_id = request.POST.get('equipment')
        print(equipment_id)
        booking_time = request.POST.get('booking_time')

        # Create a Booking object manually
        user = request.user  # Assuming the user is authenticated
        equipment = Equip.objects.get(pk=equipment_id)  # Replace with your Equipment model
        booking = Book(user=user, equipment=equipment, booking_time=booking_time, status='Pending')
        booking.save()
        return redirect('/booking_history')
    return render(request,'registration/dashboard.html',{'section':'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            return render(request,'registration/login.html',{'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'registration/register.html',{'user_form':user_form})    

def booking_history(request):
    return render(request,'registration/booking_history.html') 

