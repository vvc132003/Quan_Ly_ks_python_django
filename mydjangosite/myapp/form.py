from django import forms
from .models import Product, ThuePhong, KhachHang


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']


class LoginForm(forms.Form):
    taiKhoan = forms.CharField(
        label="Tài khoản",
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    matKhau = forms.CharField(
        label="Mật khẩu",
        max_length=255,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
