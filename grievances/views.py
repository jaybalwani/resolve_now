from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Grievance, Message, User
from .forms import UserRegistrationForm, GrievanceForm, MessageForm

def is_admin(user):
    return user.role == User.ADMIN

def is_hr_or_admin(user):
    return user.role == User.ADMIN or user.role == User.HR

def home(request):
    return render(request, 'grievances/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'grievances/register.html', {'form': form})

@login_required
def submit_grievance(request):
    if request.method == 'POST':
        form = GrievanceForm(request.POST, request.FILES)
        if form.is_valid():
            grievance = form.save(commit=False)
            grievance.user = request.user
            grievance.save()
            return redirect('grievance_list')
    else:
        form = GrievanceForm()
    return render(request, 'grievances/submit_grievance.html', {'form': form})

@login_required
def grievance_list(request):
    if request.user.role == User.EMPLOYEE:
        grievances = Grievance.objects.filter(user=request.user)
    else:
        grievances = Grievance.objects.all()
    return render(request, 'grievances/grievance_list.html', {'grievances': grievances})

@login_required
def grievance_detail(request, pk):
    grievance = get_object_or_404(Grievance, pk=pk)
    messages = grievance.messages.all()
    if request.method == 'POST':
        if 'message' in request.POST:
            form = MessageForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.grievance = grievance
                message.user = request.user
                message.save()
                return redirect('grievance_detail', pk=pk)
        elif 'delete_grievance' in request.POST and is_hr_or_admin(request.user):
            grievance.delete()
            return redirect('grievance_list')
    else:
        form = MessageForm()
    return render(request, 'grievances/grievance_detail.html', {'grievance': grievance, 'messages': messages, 'form': form})

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    grievances = Grievance.objects.all()
    users = User.objects.all()
    return render(request, 'grievances/admin_dashboard.html', {
        'grievances': grievances,
        'users': users,
    })