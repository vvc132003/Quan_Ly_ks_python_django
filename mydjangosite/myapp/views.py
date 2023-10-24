from django.shortcuts import render
from .models import Product
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Phong, ThuePhong, KhachHang, DichVu, ThueDichVu, NhanVien, NhanPhong
from .form import ProductForm, ProductUpdateForm
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout

from datetime import datetime, timedelta  # Import mô-đun datetime và timedelta


# Create your views here.

def add_thuephong(request, maPhong):
    if 'username' in request.session and 'full_name' in request.session:
        username = request.session['username']
        full_name = request.session['full_name']
        return render(request, 'myapp/add/add_thuephong.html',
                      {'maPhong': maPhong, 'username': username, 'full_name': full_name})
    else:
        return redirect('login')


def savethuephong(requestk, maPhong):
    if requestk.method == 'POST':
        hoVaTenDem = requestk.POST.get('hoVaTenDem')
        soDienThoai = requestk.POST.get('soDienThoai')
        email = requestk.POST.get('email')
        cccd = requestk.POST.get('cccd')
        diaChi = requestk.POST.get('diaChi')
        maNhanVien = requestk.POST.get("maNhanVien")
        tienDatCoc = requestk.POST.get("tienDatCoc")
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
            tienDatCoc=tienDatCoc,
            nhanVien_id=maNhanVien
        )
        nhan_phong = NhanPhong(
            thuePhong=thue_phong,
            ngayNhanPhong=timezone.now(),
        )
        thue_phong.save()
        nhan_phong.save()
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


def login(request):
    return render(request, 'myapp/rooms/login.html', {})


def process_login(request):
    if request.method == 'POST':
        tai_khoan = request.POST['taiKhoan']
        mat_khau = request.POST['matKhau']
        try:
            employee = NhanVien.objects.get(taiKhoan=tai_khoan)
            if employee.matKhau == mat_khau:
                request.session['username'] = employee.maNhanVien
                request.session['full_name'] = employee.hoVaTenDem
                return redirect('list_rooms')
            else:
                return render(request, 'myapp/rooms/login.html',
                              {'error_message': 'Tên đăng nhập hoặc mật khẩu không đúng'})
        except NhanVien.DoesNotExist:
            try:
                khachHang = KhachHang.objects.get(taiKhoan=tai_khoan)
                if khachHang.matKhau == mat_khau:
                    request.session['username'] = khachHang.maKhachHang
                    request.session['full_name'] = khachHang.hoVaTenDem
                    return redirect('product_list')
                else:
                    return render(request, 'myapp/rooms/login.html',
                                  {'error_message': 'Tên đăng nhập hoặc mật khẩu không đúng'})
            except KhachHang.DoesNotExist:
                return render(request, 'myapp/rooms/login.html', {'error_message': 'Tài khoản không tồn tại'})
    return render(request, 'myapp/rooms/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')  # You


def list_rooms(request):
    phongs = Phong.objects.all()  # Lấy danh sách các phòng
    if 'username' in request.session and 'full_name' in request.session:
        username = request.session['username']
        full_name = request.session['full_name']
        return render(request, 'myapp/rooms/list_rooms.html',
                      {'username': username, 'full_name': full_name, 'rooms': phongs})
    # Nếu người dùng chưa đăng nhập, hiển thị danh sách phòng
    return render(request, 'myapp/rooms/login.html')


def homee(request):
    phongs = Phong.objects.filter(tinhTrangPhong='còn trống')
    return render(request, 'myapp/rooms/homee.html', {'rooms': phongs})
