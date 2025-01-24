from django import forms
from order.models import OrderModel

class OrderForm(forms.ModelForm):
    
    
    class Meta:
        model = OrderModel
        
        fields = [
            "status",
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs['class'] = 'form-select'
