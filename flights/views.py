from django.shortcuts import render
from django.views.generic.edit import FormView
from django.db.models import F, Value, Func, DateTimeField
from .forms import MainForm
from .models import Flight

class ConcatTime(Func):
    function = 'CONCAT'
    template = '%(expressions)s'

class Main(FormView):
    template_name = 'add-new-request.html'
    form_class = MainForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['flights'] = Flight.objects.annotate(
        departure_datetime=Func(
            F('departure_date'),
            Value(' '),
            F('departure_time'),
            function='CONCAT',
            output_field=DateTimeField()
        )
    ).all()
        
        return context

    def form_valid(self, form):
        form.save()
        return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
