from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from customer.models import *
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# user_authentication views.

@transaction.atomic
def user_registerView(request):
    #check if the current request from a user was performed using HTTp "POST" method
    if request.method == 'POST' and request.POST['fname'] and request.POST['lname']  and request.POST['phone'] and request.POST['address'] and request.POST['email'] and request.POST['password']:
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']
        password = request.POST['password']
        #create user
        user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name, password=password)
        #if user is created
        if user is not None:
            save_info = Customer(user=user, phone=phone, address=address)
            save_info.save()
            messages.success(request,'Account created successfully')
            return redirect('register')
        else:
            messages.error(request, 'Account not created')
            return redirect('register')
    else:
        messages.error(request,'All fields must be filled')
    
    return render(request, '../templates/user_authentication/register.html')

    
def user_loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_profile')          
        else:
            messages.error(request,'Wrong credentials')
    
    return render(request, '../templates/user_authentication/login.html')


@login_required(login_url='login')
def user_profileView(request):
    if request.user.is_authenticated:
        loginuser = request.user
        data = Customer.objects.filter(user=loginuser)
        return render(request, '../templates/user_authentication/user_profile.html', {'userdata':data})
    else:
        return redirect('/')
    #return render(request, '../templates/user_authentication/user_profile.html', {})


@login_required(login_url='login')
def add_budgetView(request):
    return render(request, '../templates/user_authentication/add.html', {})


@login_required(login_url='login')
def add_new_budgetView(request):
    return render(request, '../templates/user_authentication/add.html', {})

@login_required(login_url='login')
def add_new_budgetView(request):
    #check if a user is authenticated
    if request.user.is_authenticated:
        if request.method == 'POST' and request.POST['amount']:
           #fetching form values
            amount = int(request.POST['amount'])
            #fetching the instance of the current login user
            loginuser = request.user
            #fetching login user current balance
            current_balance = Customer.objects.values_list('balance', flat=True).get(user=loginuser)
            #check if there is an existing balance
            if current_balance:
                newbalance = amount + current_balance
                Customer.objects.filter(user=loginuser).update(balance=newbalance)
        messages.success(request,'Budget has been saved successfully')
        return redirect('add_budget')        
    else:
        return redirect('login')


@login_required(login_url='login')
def spendView(request):
    return render(request, '../templates/user_authentication/spend.html', {})
                  
        
@login_required(login_url='login')
def save_expensesView(request):
    #check if a user is authenticated
    if request.user.is_authenticated:
        #check if the method used to submit form is POST
        if request.method =='POST' and request.POST['title'] and request.POST['amount']:
            #fetch form values
            title = request.POST['title']
            amount =int(request.POST['amount'])
            #fetch the instance of the current user
            loginuser = request.user
            #fetch a login user's current balance
            current_balance = int(Customer.objects.values_list('balance', flat=True).get(user=loginuser))
            #check if amount is greater than current balance
            if amount > current_balance:
                message = ('Sorry, Low Balance. Available Balance: R ' + str(current_balance))
                messages.error(request, message)     
                return redirect('spend')  
            elif amount <= current_balance:
                newbalance = current_balance - amount
                Customer.objects.filter(user=loginuser).update(balance=newbalance)
                expenses = Expenses(user=loginuser, title=title, amount=amount)
                if expenses:
                    expenses.save()
        messages.success(request, 'Expenses have been saved successfully')
        return redirect('spend')
    else:
        return redirect(login)

@login_required(login_url='login')
def all_expensesView(request):
    if request.user.is_authenticated:
        loginuser = request.user
        alldata = Expenses.objects.filter(user=loginuser)
        return render(request, '../templates/user_authentication/user_records.html', {'alldata':alldata})
    else:
        return redirect(login)


def logout_View(request):
    logout(request)
    return redirect('/')
        
