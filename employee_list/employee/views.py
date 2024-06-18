from django.shortcuts import render,redirect,get_object_or_404
from .models import EmployeeDetails
from .form import EmpForm
from django.http import Http404


def home(request):
    return render(request, 'employee_form.html', {'form': EmpForm()})

def data_upload(request):
    if request.method == 'POST':
        user_data = EmpForm(request.POST)
        if user_data.is_valid():
            user_data.save()
            return redirect('list_of_employee')

def list_of_employee(request):
    all_record = EmployeeDetails.objects.all().order_by('-id').values()
    total_record = EmployeeDetails.objects.count()
    return render(request, 'employee_list.html', {'all_record': all_record, 'total_record':total_record})

def detail_of_employee(request,id):
    single_record = EmployeeDetails.objects.get(id = id)
    return render(request, 'employee_detail.html', {'single_record':single_record})

def update_data(request,id):
    try:
        exit_record = get_object_or_404(EmployeeDetails, id = id)
        if request.method == "POST":
            modified_record = EmpForm(request.POST, instance = exit_record)
            if modified_record.is_valid():
                modified_record.save()
                return redirect('list_of_employee')
        else:
            old_data = EmpForm(instance = exit_record)
        return render(request, "employee_edit.html", {'old_data' : old_data, 'exit_record' : exit_record})
    except Http404:
        return render(request, 'error.html')
    
def delete_data(request, id):
    try:
        del_record = get_object_or_404(EmployeeDetails, id = id)
        del_record.delete()
        return redirect('list_of_employee')
    
    except Http404:
        return render(request, 'error.html')
   