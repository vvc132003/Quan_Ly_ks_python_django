from django.shortcuts import render
from .models import Product
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Phong, ThuePhong, KhachHang, DichVu, ThueDichVu, NhanVien, NhanPhong, TraPhong
from .form import ProductForm, ProductUpdateForm
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout
from django.db.models import Sum
from django.utils.formats import number_format

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
        messages.success(requestk, "Thuê phòng thành công thành công!")
        return redirect('list_rooms')
    return render(requestk, 'myapp/add_thuephong.html', {"maPhong": maPhong})


def savedatphongphong(requestk, maPhong):
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
            trangThai="Đã đặt",
            tongTien=0,
            tienDatCoc=tienDatCoc,
            nhanVien_id=maNhanVien
        )
        thue_phong.save()
        Phong.objects.filter(maPhong=maPhong).update(tinhTrangPhong="đã đặt")
        messages.success(requestk, "Đặt phòng thành công thành công!")
        return redirect('homee')
    return render(requestk, 'myapp/add_thuephong.html', {"maPhong": maPhong})


def add_traphong(request):
    if request.method == "POST":
        ma_thue_phong = request.POST.get("maThuePhong")
        ma_phong = request.POST.get("maPhong")
        tong_tien = request.POST.get("tongTien")
        ma_nhan_vien = request.POST.get("maNhanVien")
        gia_tien = request.POST.get("giaTien")
        tien_dat_coc = request.POST.get("tienDatCoc")
        tong_tien_khach_hang = float(tong_tien) + float(gia_tien) - float(tien_dat_coc)
        tra_phong = TraPhong(thuePhong=ThuePhong.objects.get(maThuePhong=ma_thue_phong),
                             nhanVien=NhanVien.objects.get(maNhanVien=ma_nhan_vien), tongTien=tong_tien_khach_hang,
                             ngayTraPhong=datetime.now())
        tra_phong.save()
        ThuePhong.objects.filter(maThuePhong=ma_thue_phong).update(tongTien=tong_tien, trangThai="Đã trả")
        # Tạo logic cập nhật roomService.updatesuachua(maPhong) ở đây
        Phong.objects.filter(maPhong=ma_phong).update(tinhTrangPhong="chưa dọn")
        messages.warning(request, "Thanh toán thành công!")
        return redirect("list_rooms")
    else:
        return render(request, 'error_page.html', {'error_message': 'Invalid Request'})


def view_thue_phong(request, maPhong):
    # Lấy thông tin thuê phòng theo mã phòng và trạng thái "Đang thuê"
    thue_phong = get_object_or_404(ThuePhong, phong__maPhong=maPhong, trangThai='Đang thuê')
    # Lấy thông tin thuê dịch vụ theo mã thuê phòng
    thue_dich_vus = ThueDichVu.objects.filter(thuePhong=thue_phong)
    # Tính tổng tiền từ các dịch vụ
    total_cost = thue_dich_vus.aggregate(total=Sum('thanhTien'))['total'] or 0
    # total_cost_vnd = number_format(total_cost, force_grouping=True)
    # Tổng tiền của thuê phòng và dịch vụ
    total_payment = thue_phong.phong.giaTien + total_cost - thue_phong.tienDatCoc
    total_payment_vnd = number_format(total_payment, force_grouping=True)
    # Lấy danh sách các dịch vụ
    dich_vu_list = DichVu.objects.all()
    gia_tien_phong = thue_phong.phong.giaTien
    tien_dat_coc = thue_phong.tienDatCoc
    gia_tien_phong_formatted = number_format(gia_tien_phong, force_grouping=True)
    tien_dat_coc_formatted = number_format(tien_dat_coc, force_grouping=True)
    context = {
        'thue_phong': thue_phong,
        'thue_dich_vus': thue_dich_vus,
        'dich_vu_list': dich_vu_list,
        'totalCost': total_cost,
        'totalPayment': total_payment_vnd,
        'gia_tien_phong': gia_tien_phong_formatted,
        'tien_dat_coc': tien_dat_coc_formatted,
    }
    return render(request, 'myapp/rooms/view_thue_phong.html', context)


def don_phong(request, maPhong):
    Phong.objects.filter(maPhong=maPhong).update(tinhTrangPhong="còn trống")
    messages.info(request, "Dọn phòng thành công!")
    return redirect('list_rooms')


# def sua_phong(request, maPhong):
#     Phong.objects.filter(maPhong=maPhong).update(tinhTrangPhong="Đang sửa chữa")
#     messages.error(request, "Đang sửa chữa!")
#     return redirect('list_rooms')


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
                    return redirect('homee')
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
    return render(request, 'myapp/rooms/login.html')


def homee(request):
    if request.method == 'GET':
        maPhong = request.GET.get('maPhong')
        if 'username' in request.session and 'full_name' in request.session:
            username = request.session['username']
            full_name = request.session['full_name']
            if maPhong:
                phongs = Phong.objects.filter(maPhong=maPhong)
            else:
                phongs = Phong.objects.all()

            return render(request, 'myapp/rooms/home.html',
                          {'username': username, 'full_name': full_name, 'rooms': phongs})
        else:
            return render(request, 'myapp/rooms/login.html')
    return render(request, 'myapp/rooms/search_form.html')


def nhan_phong(request, maPhong):
    thue_phong_list = ThuePhong.objects.filter(phong__maPhong=maPhong, trangThai='Đã đặt')
    context = {'thuePhongList': thue_phong_list}
    return render(request, 'myapp/rooms/nhanphong.html', context)


def addnhanphong(request):
    if request.method == 'POST':
        maPhong = request.POST.get('maPhong')
        maThuePhong = request.POST.get('maThuePhong')
        cccd = request.POST.get('cccd')
        khachHang = KhachHang.objects.filter(cccd=cccd).first()
        if khachHang is not None:
            thuePhong = ThuePhong.objects.get(maThuePhong=maThuePhong)
            nhan_phong = NhanPhong(
                thuePhong=thuePhong,
                ngayNhanPhong=timezone.now(),
            )
            nhan_phong.save()
            Phong.objects.filter(maPhong=maPhong).update(tinhTrangPhong="có khách")
            ThuePhong.objects.filter(maThuePhong=maThuePhong).update(trangThai="Đang thuê")
            messages.success(request, 'Nhận phòng thành công!')
            return redirect('list_rooms')
        else:
            messages.error(request, 'CCCD không hợp lệ. Vui lòng kiểm tra lại!')
            return redirect(reverse('nhan_phong', args=[maPhong]))

    # Xử lý trường hợp không phải là POST request
    return render(request, {})
