from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from product.models import Writer, Publication, Subject
from product.forms import WriterForm, PublicationForm



class Dashboard(View):
    def get(self, request):
        return render(request, 'dashboard/dashboard.html')

def writer_list(request):
    writers = Writer.objects.all()
    context ={
        'writers': writers
    }
    return render(request, 'dashboard/writer_list.html', context)



class WriterListView(ListView):
    model = Writer    # same as -> Writer.objects.all();  product/writer_list.html
    template_name = 'dashboard/writer_list.html'
    context_object_name = 'writers'

class WriterDetailView(DetailView):
    model = Writer         # Writer.objects.get(pk=pk)
    template_name = 'dashboard/writer_detail.html'
    context_object_name = 'writer'  # without context_object_name -> {{writer.name}}...in template


# FormView

# class WriterCreateView(FormView):
    # form_class = WriterForm
    # template_name = 'dashboard/writer_form.html'

    # def form_valid(self, form):
        # form.save()
        # return redirect('writer-list')

# CreateView

class WriterCreateView(CreateView):
    model = Writer
    form_class = WriterForm   # or -> fields = '__all__'

    template_name = 'dashboard/writer_form.html'

    # get_absolute_url(self): in model instead of  return redirect('writer-list')

class WriterEditView(UpdateView):
    model = Writer
    fields = '__all__'
    template_name = 'dashboard/writer_form.html'

class WriterDeleteView(DeleteView):
    model = Writer
    success_url = reverse_lazy('writer-list')  # reverse_lazy same as-> dashboard/writer/list
    template_name = 'dashboard/writer_confirm_delete.html'

class PublicationListView(ListView):
    model = Publication
    template_name = 'dashboard/publication_list.html'
    context_object_name = 'publications'

class PublicationDetailView(DetailView):
    model = Publication
    template_name = 'dashboard/publication_detail.html'
    context_object_name = 'publication'

class PublicationCreateView(CreateView):
    model = Publication
    form_class = PublicationForm
    template_name = 'dashboard/publication_form.html'


class PublicationEditView(UpdateView):
    model = Publication
    fields = '__all__'
    template_name = 'dashboard/publication_form.html'

class PublicationDeleteView(DeleteView):
    model = Publication
    success_url = reverse_lazy('publication-list')
    template_name = 'dashboard/publication_confirm_delete.html'



class SubjectListView(ListView):
    model = Subject
    template_name = 'dashboard/Subject_list.html'
    context_object_name = 'subjects'
