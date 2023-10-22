from django.shortcuts import render
from .models import Product
from django.urls import reverse
from decimal import Decimal
from .models import Phong, ThuePhong, KhachHang, DichVu, ThueDichVu
from .models import NhanVien  # Import your custom user model
from .form import ProductForm, ProductUpdateForm, LoginForm
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

from datetime import datetime, timedelta  # Import mô-đun datetime và timedelta


# Create your views here.

def add_thuephong(request, maPhong):
    loggedInUser = request.session.get('loggedInUser', None)
    fullName = request.session.get('fullName', None)
    if loggedInUser is not None:
        return render(request, 'myapp/add/add_thuephong.html',
                      {'loggedInUser': loggedInUser, 'fullName': fullName, "maPhong": maPhong})
    else:
        return redirect('login')


def savethuephong(requestk, maPhong):
    if requestk.method == 'POST':
        hoVaTenDem = requestk.POST.get('hoVaTenDem')
        soDienThoai = requestk.POST.get('soDienThoai')
        email = requestk.POST.get('email')
        cccd = requestk.POST.get('cccd')
        diaChi = requestk.POST.get('diaChi')
        khach_hang = KhachHang.objects.create(
            hoVaTenDem=hoVaTenDem,
            soDienThoai=soDienThoai,
            email=email,
            cccd=cccd,
            diaChi=diaChi
        )
        thue_phong = ThuePhong(
            khachHang=khach_hang,
            phong_id=maPhong,
            ngayNhanPhong=timezone.now(),
            ngayTraPhong=timezone.now() + timezone.timedelta(hours=1),
            trangThai="Đang thuê",
            tongTien=0,
            tienDatCoc=0
        )
        thue_phong.save()
        Phong.objects.filter(maPhong=maPhong).update(tinhTrangPhong="có khách")
        return redirect('list_rooms')

    return render(requestk, 'myapp/add_thuephong.html', {"maPhong": maPhong})


def view_thue_phong(request, maPhong):
    # hiển thị thue phòng theo maphong và trang thai đang thue
    thue_phong = get_object_or_404(ThuePhong, phong__maPhong=maPhong, trangThai='Đang thuê')
    # hieent thị thông tin thue dich vụ thoe mathuephong
    thue_dich_vus = ThueDichVu.objects.filter(thuePhong=thue_phong)
    # hien thị các dịch vụ
    dich_vu_list = DichVu.objects.all()
    context = {
        'thue_phong': thue_phong,
        'thue_dich_vus': thue_dich_vus,
        'dich_vu_list': dich_vu_list,
    }
    return render(request, 'myapp/rooms/view_thue_phong.html', context)


def delete_thue_dich_vu(requestdelete, maThueDichVu, maPhong):
    thueDichVu = get_object_or_404(ThueDichVu, pk=maThueDichVu)
    if thueDichVu.soLuong > 0:
        thueDichVu.soLuong -= 1
        if thueDichVu.soLuong == 0:
            # If quantity becomes 0, delete the service rental
            thueDichVu.delete()
        else:
            gia = thueDichVu.dichVu.gia
            thanhTien = gia * thueDichVu.soLuong
            thueDichVu.thanhTien = thanhTien
            thueDichVu.save()
    return redirect(reverse('view_thue_phong', args=[maPhong]))


def update_thue_dich_vu(requestupdate, maThueDichVu, maPhong):
    try:
        thueDichVu = ThueDichVu.objects.get(pk=maThueDichVu)
        currentSoLuong = thueDichVu.soLuong
        thueDichVu.soLuong = currentSoLuong + 1
        gia = thueDichVu.dichVu.gia
        thanhTien = gia * thueDichVu.soLuong
        thueDichVu.thanhTien = thanhTien
        thueDichVu.save()
    except ThueDichVu.DoesNotExist:
        pass  # Handle the case where the ThueDichVu does not exist (if needed)
    return redirect(reverse('view_thue_phong', args=[maPhong]))


def add_thue_dich_vu(request):
    if request.method == "POST":
        maDichVu = request.POST.get("maDichVu")
        maThuePhong = request.POST.get("maThuePhong")
        maPhong = request.POST.get("maPhong")
        maNhanVien = request.POST.get("maNhanVien")

        thuePhong = get_object_or_404(ThuePhong, pk=maThuePhong)
        dichVu = get_object_or_404(DichVu, pk=maDichVu)
        nhanVien = get_object_or_404(NhanVien, pk=maNhanVien)

        thueDichVu = ThueDichVu(
            thuePhong=thuePhong,
            dichVu=dichVu,
            nhanVien=nhanVien,
            soLuong=1
        )

        # Calculate the total cost
        gia = dichVu.gia
        thanhTien = gia * thueDichVu.soLuong
        thueDichVu.thanhTien = thanhTien

        thueDichVu.save()

    return redirect(reverse('view_thue_phong', args=[maPhong]))


def login(request):
    return render(request, 'myapp/rooms/login.html')


def process_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            taiKhoan = form.cleaned_data['taiKhoan']
            matKhau = form.cleaned_data['matKhau']
            try:
                nhanvien = NhanVien.objects.get(taiKhoan=taiKhoan)
                if matKhau == nhanvien.matKhau:
                    user = authenticate(request, username=taiKhoan, password=matKhau)
                    if user is not None:
                        login(request, user)
                        request.session['loggedInUser'] = nhanvien.taiKhoan
                        request.session['fullName'] = nhanvien.hoVaTenDem
                    return redirect('list_rooms')
            except NhanVien.DoesNotExist:
                pass
    else:
        form = LoginForm()
    return render(request, 'myapp/rooms/login.html', {'form': form})


def add_product(requests):
    new_product = Product(name="Product Name", description="Product Description", price=29.99)
    new_product.save()
    return render(requests, 'myapp/product_added.html')


def product_list(requesto):
    products = Product.objects.all()
    return render(requesto, 'myapp/product_list.html', {'products': products})


def add_producta(requestk):
    if requestk.method == 'POST':
        form = ProductForm(requestk.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(requestk, 'myapp/from_add_product.html', {'form': form})


def delete_product(requesth, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if requesth.method == 'GET':
        product.delete()
        return redirect('product_list')
    return render(requesth, 'myapp/delete_product_confirm.html', {'product': product})


def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductUpdateForm(instance=product)
    return render(request, 'myapp/update_product.html', {'form': form, 'product': product})


def list_rooms(request):
    loggedInUser = request.session.get('loggedInUser', None)
    fullName = request.session.get('fullName', None)
    if loggedInUser is not None:
        phongs = Phong.objects.all()  # Lấy danh sách các phòng
        return render(request, 'myapp/rooms/list_rooms.html',
                      {'loggedInUser': loggedInUser, 'fullName': fullName, 'rooms': phongs})
    else:
        return redirect('login')
