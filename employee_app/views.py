from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Employee, Department, Language


class EmployeeListView(ListView):
    model = Employee
    context_object_name = 'employees'


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'employee_app/employee_create.html'
    fields = ('first_name', 'last_name', 'age', 'department', 'programming_language')


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_app/employee_detail.html'
    context_object_name = 'employee'


class EmployeeUpdateView(UpdateView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'employee_app/employee_update.html'
    fields = ('first_name', 'last_name', 'age', 'department', 'programming_language')


class EmployeeDeleteView(DeleteView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'employee_app/employee_delete.html'
    success_url = reverse_lazy('employee_list_url')


class DepartmentListView(ListView):
    model = Department
    context_object_name = 'departments'
    template_name = 'employee_app/department_list.html'


class DepartmentCreateView(CreateView):
    model = Department
    template_name = 'employee_app/department_create.html'
    fields = ('name', 'floor')


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'employee_app/department_detail.html'
    context_object_name = 'department'


class DepartmentUpdateView(UpdateView):
    model = Department
    context_object_name = 'department'
    template_name = 'employee_app/department_update.html'
    fields = ('name', 'floor')


class DepartmentDeleteView(DeleteView):
    model = Department
    context_object_name = 'department'
    template_name = 'employee_app/department_delete.html'
    success_url = reverse_lazy('department_list_url')


class LanguageListView(ListView):
    model = Language
    context_object_name = 'languages'
    template_name = 'employee_app/language_list.html'


class LanguageCreateView(CreateView):
    model = Language
    template_name = 'employee_app/language_create.html'
    fields = ('name',)


class LanguageDetailView(DetailView):
    model = Language
    template_name = 'employee_app/language_detail.html'
    context_object_name = 'language'


class LanguageUpdateView(UpdateView):
    model = Language
    context_object_name = 'language'
    template_name = 'employee_app/language_update.html'
    fields = ('name',)


class LanguageDeleteView(DeleteView):
    model = Language
    context_object_name = 'language'
    template_name = 'employee_app/language_delete.html'
    success_url = reverse_lazy('language_list_url')
