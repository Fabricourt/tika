from django import forms
from .models import Booktruck

class BooktruckForm(forms.ModelForm):
    class Meta:
        model = Booktruck
        fields = (
            'user_id', 
            'first_name',
            'last_name',          
            'ministry_name',
            'email',
            'phone_number',
            'booking_date',
            'return_date',
            )
    
    def clean(self):
        form_booking_date = self.cleaned_data.get('booking_date')
        form_return_date = self.cleaned_data.get('return_date')
        between = Booktruck.objects.filter(booking_date__gte=form_booking_date, return_date__lte=form_return_date).exists()
        if between:
            raise forms.ValidationError("Period already between this date 1")
        super(BooktruckForm, self).clean()