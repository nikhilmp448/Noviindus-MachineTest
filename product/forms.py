
from pyexpat import model
from django.forms import ModelForm
from product.models import Product


class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = (
            "name",
            "image",
            "price",
        )
    def __init__(self,*args,**kwargs):
        super(AddProductForm, self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"