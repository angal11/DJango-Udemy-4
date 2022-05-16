from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView,\
    CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Teacher

from .forms import ContactForm

# Create your views here.
def home_view(request):
    return render(request,'classroom/home.html')

class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/Thankyou.html'


class TeacherCreateView(CreateView):
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:thankyou')

class TeacherListView(ListView):
    model = Teacher
    queryset = Teacher.objects.order_by('first_name')
    context_object_name = "teacher_list"

class TeacherDetailView(DetailView):
    # return only one model entry pk
    # model_detail.html
    model = Teacher
    #PK --> {{teacher}}

class TeacherUpdateView(UpdateView):
    #Share model form.html --- PK
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:list_teacher')

class TeacherDeleteView(DeleteView):
    # form --> confirm Delete button
    #default template name:
    # model_confirm_delete.html
    model = Teacher
    success_url = reverse_lazy('classroom:list_teacher')

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    success_url = reverse_lazy('classroom:thankyou')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

