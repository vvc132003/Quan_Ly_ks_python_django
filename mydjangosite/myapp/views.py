from _ast import arg

from django.shortcuts import render
from .models import Product
from django.urls import reverse
from django.contrib import messages
from .models import Phong, ThuePhong, KhachHang, DichVu, ThueDichVu, NhanVien, NhanPhong, TraPhong, Tang
from .form import ProductForm, ProductUpdateForm
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.db.models import Sum
from django.utils.formats import number_format
from django.core.mail import send_mail
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.db.models import Count, Sum
from django.db.models.functions import ExtractMonth
from django.http import JsonResponse


# Create your views here.


def thongke(request):
    thong_ke = ThuePhong.objects.annotate(month=ExtractMonth('ngayNhanPhong')) \
        .values('month') \
        .annotate(so_lan_thue=Count('maThuePhong'), doanh_thu=Sum('tongTien')) \
        .order_by('month')
    thang = [entry['month'] for entry in thong_ke]
    so_lan_thue = [entry['so_lan_thue'] for entry in thong_ke]
    doanh_thu = [entry['doanh_thu'] for entry in thong_ke]
    thong_ke_dich_vu = ThueDichVu.objects.values('dichVu__tenDichVu').annotate(
        tongThanhTien=Sum('thanhTien'),
        tongSoLuong=Sum('soLuong')
    ).order_by('-tongThanhTien')
    data = {
        'thang': thang,
        'so_lan_thue': so_lan_thue,
        'doanh_thu': [str(entry) for entry in doanh_thu],


    }
    return render(request, 'myapp/dichvu/revenue_chart.html', {'data': data, 'thong_ke_dich_vu': thong_ke_dich_vu})


def add_thuephong(request, maPhong):
    phongs = Phong.objects.filter(maPhong=maPhong).first()
    if 'username' in request.session and 'full_name' in request.session:
        username = request.session['username']
        full_name = request.session['full_name']
        return render(request, 'myapp/add/add_thuephong.html',
                      {'phongs': phongs, 'username': username,
                       'full_name': full_name})
    else:
        return redirect('login')


def savethuephong(requestk):
    if requestk.method == 'POST':
        maPhong = requestk.POST.get('maPhong')
        hoVaTenDem = requestk.POST.get('hoVaTenDem')
        soDienThoai = requestk.POST.get('soDienThoai')
        email = requestk.POST.get('email')
        cccd = requestk.POST.get('cccd')
        diaChi = requestk.POST.get('diaChi')
        maNhanVien = requestk.POST.get("maNhanVien")
        tienDatCoc = requestk.POST.get("tienDatCoc")
        ngayNhanPhong = requestk.POST.get("ngayNhanPhong")
        gioNhanPhong = requestk.POST.get("gioNhanPhong")
        ngayTraPhong = requestk.POST.get("ngayTraPhong")
        gioTraPhong = requestk.POST.get("gioTraPhong")
        khach_hang = KhachHang.objects.create(
            hoVaTenDem=hoVaTenDem,
            soDienThoai=soDienThoai,
            email=email,
            cccd=cccd,
            diaChi=diaChi,
            trangThai="đang hoạt động"
        )
        phong = Phong.objects.get(maPhong=maPhong)
        thue_phong = ThuePhong(
            khachHang=khach_hang,
            phong=phong,
            ngayNhanPhong=ngayNhanPhong,
            ngayTraPhong=ngayTraPhong,
            gioNhanPhong=gioNhanPhong,
            gioTraPhong=gioTraPhong,
            trangThai="Đang thuê",
            tongTien=0,
            tienDatCoc=tienDatCoc,
            nhanVien_id=maNhanVien,
            trangThaiThanhToan="chưa thanh toán"
        )
        nhan_phong = NhanPhong(
            thuePhong=thue_phong,
            ngayNhanPhong=ngayNhanPhong,
            gioNhanPhong=gioNhanPhong,
        )
        thue_phong.save()
        nhan_phong.save()
        Phong.objects.filter(maPhong=maPhong).update(tinhTrangPhong="có khách")
        subject = 'Thuê phòng'
        message = f'Bạn đã thuê phòng {maPhong}, Ngày thuê: {ngayNhanPhong}.'
        from_email = 'vvc132003@gmail.com'
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        messages.success(requestk, "Thuê phòng thành công thành công!")
        return redirect('list_rooms')
    return render(requestk, 'myapp/add_thuephong.html', {})


def savedatphongphong(requestk):
    if requestk.method == 'POST':
        maPhong = requestk.POST.get('maPhong')
        hoVaTenDem = requestk.POST.get('hoVaTenDem')
        soDienThoai = requestk.POST.get('soDienThoai')
        email = requestk.POST.get('email')
        cccd = requestk.POST.get('cccd')
        diaChi = requestk.POST.get('diaChi')
        maNhanVien = requestk.POST.get("maNhanVien")
        tienDatCoc = requestk.POST.get("tienDatCoc")
        ngayNhanPhong = requestk.POST.get("ngayNhanPhong")
        ngayTraPhong = requestk.POST.get("ngayTraPhong")
        gioNhanPhong = requestk.POST.get("gioNhanPhong")
        gioTraPhong = requestk.POST.get("gioTraPhong")
        khach_hang = KhachHang.objects.create(
            hoVaTenDem=hoVaTenDem,
            soDienThoai=soDienThoai,
            email=email,
            cccd=cccd,
            diaChi=diaChi,
            trangThai="đang hoạt động"
        )
        phong = Phong.objects.get(maPhong=maPhong)
        thue_phong = ThuePhong(
            khachHang=khach_hang,
            phong=phong,
            ngayNhanPhong=ngayNhanPhong,
            ngayTraPhong=ngayTraPhong,
            gioNhanPhong=gioNhanPhong,
            gioTraPhong=gioTraPhong,
            trangThai="Đã đặt",
            tongTien=0,
            tienDatCoc=tienDatCoc,
            nhanVien_id=maNhanVien,
            trangThaiThanhToan="chưa thanh toán"
        )
        thue_phong.save()
        Phong.objects.filter(maPhong=maPhong).update(tinhTrangPhong="đã đặt")
        subject = 'Thuê phòng'
        message = f'Bạn đã thuê phòng {maPhong}, Ngày đặt: {ngayNhanPhong}.'
        from_email = 'vvc132003@gmail.com'
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        messages.success(requestk, "Đặt phòng thành công thành công!")
        return redirect('homee')
    return render(requestk, 'myapp/add_thuephong.html', {})


from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io


def inhoadon(request, ma_thue_phong):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{ma_thue_phong}.pdf"'
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.drawString(100, 750, "Invoice")
    p.drawString(100, 730, f"Thue Phong: {ma_thue_phong}")
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


def add_traphong(request):
    if request.method == "POST":
        ma_thue_phong = request.POST.get("maThuePhong")
        ma_phong = request.POST.get("maPhong")
        tong_tien = request.POST.get("tongTien")
        ma_nhan_vien = request.POST.get("maNhanVien")
        gia_tien = request.POST.get("giaTien")
        tien_dat_coc = request.POST.get("tienDatCoc")
        maKhachHang = request.POST.get("maKhachHang")
        hinhThucThanhToan = request.POST.get("hinhThucThanhToan")

        tong_tien_khach_hang = float(tong_tien) + float(gia_tien) - float(tien_dat_coc)
        tra_phong = TraPhong(thuePhong=ThuePhong.objects.get(maThuePhong=ma_thue_phong),
                             nhanVien=NhanVien.objects.get(maNhanVien=ma_nhan_vien), tongTien=tong_tien_khach_hang,
                             ngayTraPhong=datetime.now(), gioTraPhong=datetime.now().time())
        tra_phong.save()
        ThuePhong.objects.filter(maThuePhong=ma_thue_phong).update(tongTien=tong_tien, trangThai="Đã trả",
                                                                   trangThaiThanhToan="đã thanh toán",
                                                                   hinhThucThanhToan=hinhThucThanhToan
                                                                   )
        Phong.objects.filter(maPhong=ma_phong).update(tinhTrangPhong="chưa dọn")
        KhachHang.objects.filter(maKhachHang=maKhachHang).update(trangThai="hết hoạt động")
        messages.warning(request, "Thanh toán thành công!")
        return redirect('list_rooms')
    else:
        return render(request, 'error_page.html', {'error_message': 'Invalid Request'})


def view_thue_phong(request, maPhong):
    if 'username' in request.session and 'full_name' in request.session:
        username = request.session['username']
        # Lấy thông tin thuê phòng theo mã phòng và trạng thái "Đang thuê"
        thue_phong = get_object_or_404(ThuePhong, phong__maPhong=maPhong, trangThai='Đang thuê')
        # Lấy thông tin thuê dịch vụ theo mã thuê phòng
        thue_dich_vus = ThueDichVu.objects.filter(thuePhong=thue_phong)
        # Tính tổng tiền từ các dịch vụ
        total_cost = thue_dich_vus.aggregate(total=Sum('thanhTien'))['total'] or 0
        # Tổng tiền của thuê phòng và dịch vụ
        total_payment = thue_phong.phong.giaTien + total_cost - thue_phong.tienDatCoc
        total_payment_vnd = number_format(total_payment, force_grouping=True)
        # Lấy danh sách các dịch vụ
        dich_vu_list = DichVu.objects.filter(trangThai="còn bán")
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
            'username': username,
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
            subject = 'Dịch vụ được xoá'
            message = f'Dịch vụ {thueDichVu.dichVu.tenDichVu} đã được xoá khỏi phòng {maPhong} , chỉ còn lại {thueDichVu.soLuong} .'
            from_email = 'vvc132003@gmail.com'
            recipient_list = [thueDichVu.thuePhong.khachHang.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
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
        subject = 'Dịch vụ được thêm'
        message = f'Dịch vụ {thueDichVu.dichVu.tenDichVu} đã được thêm vào thuê phòng {maPhong} , tổng {thueDichVu.soLuong} .'
        from_email = 'vvc132003@gmail.com'
        recipient_list = [thueDichVu.thuePhong.khachHang.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
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
        gia = dichVu.gia
        thanhTien = gia * thueDichVu.soLuong
        thueDichVu.thanhTien = thanhTien
        thueDichVu.save()
        subject = 'Dịch vụ được thêm'
        message = f'Dịch vụ {dichVu.tenDichVu} đã được thêm vào thuê phòng {maPhong}.'
        from_email = 'vvc132003@gmail.com'
        recipient_list = [thuePhong.khachHang.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
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
        tai_khoan = request.POST.get('taiKhoan')
        mat_khau = request.POST.get('matKhau')
        nhanvien = NhanVien.objects.filter(taiKhoan=tai_khoan, trangThai="đang hoạt động").first()
        if nhanvien and nhanvien.matKhau == mat_khau:
            request.session['username'] = nhanvien.maNhanVien
            request.session['full_name'] = nhanvien.hoVaTenDem
            request.session['chucVu'] = nhanvien.chucVu
            return redirect('list_rooms')
        khachHang = KhachHang.objects.filter(taiKhoan=tai_khoan, trangThai="đang hoạt động").first()
        if khachHang and khachHang.matKhau == mat_khau:
            request.session['username'] = khachHang.maKhachHang
            request.session['full_name'] = khachHang.hoVaTenDem
            return redirect('homee')
        return render(request, 'myapp/rooms/login.html', {'error_message': 'Tên đăng nhập hoặc mật khẩu không đúng'})
    return render(request, 'myapp/rooms/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')  # You


# def list_rooms(request):
#     phongs = Phong.objects.all()
#     if 'username' in request.session and 'full_name' in request.session:
#         username = request.session['username']
#         full_name = request.session['full_name']
#         role = request.session.get('chucVu', None)
#         if role == "Quản Lý":
#             return render(request, 'myapp/rooms/list_rooms.html',
#                           {'username': username, 'full_name': full_name, 'rooms': phongs})
#         elif role == "Nhân Viên":
#             return render(request, 'myapp/rooms/list_rooms.html',
#                           {'username': username, 'full_name': full_name, 'rooms': phongs})
#     return render(request, 'myapp/rooms/login.html')


def list_rooms(request):
    tangs = Tang.objects.all()
    rooms_by_floor = {}
    for tang in tangs:
        rooms = Phong.objects.filter(tang=tang)
        rooms_by_floor[tang] = rooms
    if 'username' in request.session and 'full_name' in request.session:
        username = request.session['username']
        full_name = request.session['full_name']
        role = request.session.get('chucVu', None)
        if role == "Quản Lý":
            return render(request, 'myapp/rooms/list_rooms.html',
                          {'username': username, 'full_name': full_name, 'rooms_by_floor': rooms_by_floor})
        elif role == "Nhân Viên":
            return render(request, 'myapp/rooms/list_rooms.html',
                          {'username': username, 'full_name': full_name, 'rooms_by_floor': rooms_by_floor})
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
                phongs = Phong.objects.filter(tinhTrangPhong="còn trống")
            return render(request, 'myapp/rooms/home.html',
                          {'username': username, 'full_name': full_name, 'rooms': phongs})
        else:
            if maPhong:
                phongs = Phong.objects.filter(maPhong=maPhong)
            else:
                phongs = Phong.objects.filter(tinhTrangPhong="còn trống")
            return render(request, 'myapp/rooms/home.html', {'rooms': phongs})
    return render(request, 'myapp/rooms/search_form.html')


def nhan_phong(request, maPhong):
    thue_phong_list = ThuePhong.objects.filter(phong__maPhong=maPhong, trangThai='Đã đặt')
    context = {'thuePhongList': thue_phong_list}
    return render(request, 'myapp/rooms/nhanphong.html', context)


def addnhanphong(request):
    if request.method == 'POST':
        maPhong = request.POST.get('maPhong')
        ngayNhanPhong = request.POST.get('ngayNhanPhong')
        ngayTraPhong = request.POST.get('ngayTraPhong')
        maThuePhong = request.POST.get('maThuePhong')
        cccd = request.POST.get('cccd')
        khachHang = KhachHang.objects.filter(cccd=cccd, trangThai="đang hoạt động").first()
        if khachHang is not None:
            thuePhong = ThuePhong.objects.get(maThuePhong=maThuePhong)
            nhan_phong = NhanPhong(
                thuePhong=thuePhong,
                ngayNhanPhong=ngayNhanPhong,
            )
            nhan_phong.save()
            Phong.objects.filter(maPhong=maPhong).update(tinhTrangPhong="có khách")
            ThuePhong.objects.filter(maThuePhong=maThuePhong).update(trangThai="Đang thuê", ngayTraPhong=ngayTraPhong)
            messages.success(request, 'Nhận phòng thành công!')
            return redirect('list_rooms')
        else:
            messages.error(request, 'CCCD không hợp lệ. Vui lòng kiểm tra lại!')
            return redirect(reverse('nhan_phong', args=[maPhong]))
    return render(request, {})


def dichvu_list(requesto):
    dichvus = DichVu.objects.filter(trangThai="còn bán").order_by('-maDichVu')
    return render(requesto, 'myapp/dichvu/dichvu_list.html', {'dichvus': dichvus})


def add_dichvu(request):
    if request.method == 'POST':
        tenDichVu = request.POST.get('tenDichVu')
        moTa = request.POST.get('moTa')
        gia = request.POST.get('gia')
        image = request.POST.get('image')
        dichvus = DichVu(tenDichVu=tenDichVu, moTa=moTa, gia=gia, image=image, trangThai="còn bán")
        dichvus.save()
        return redirect('dichvu_list')
    return render(request, 'myapp/dichvu/add_dichvu.html')


def update_dichvu(request, maDichVu):
    dichvu = DichVu.objects.get(maDichVu=maDichVu)
    if request.method == 'POST':
        tenDichVu = request.POST.get('tenDichVu')
        moTa = request.POST.get('moTa')
        gia = request.POST.get('gia')
        image = request.POST.get('image')
        DichVu.objects.filter(maDichVu=maDichVu).update(tenDichVu=tenDichVu, moTa=moTa, gia=gia, image=image,
                                                        trangThai="còn bán")
        return redirect('dichvu_list')
    return render(request, 'myapp/dichvu/update_dichvu.html', {'dichvu': dichvu})


def delete_dichvu(requesth, maDichVu):
    if requesth.method == 'GET':
        DichVu.objects.filter(maDichVu=maDichVu).update(trangThai="hết bán")
        messages.success(requesth, 'Xoá thành dịch vụ thành công!')
        return redirect('dichvu_list')
    return render(requesth, 'myapp/delete_product_confirm.html', {})


def khachhang_list(requesto):
    khachhangs = KhachHang.objects.filter(trangThai="đang hoạt động").order_by('-maKhachHang')
    return render(requesto, 'myapp/khachhang/khachhang_list.html', {'khachhangs': khachhangs})


def delete_khachhang(requesth, maKhachHang):
    if requesth.method == 'GET':
        KhachHang.objects.filter(maKhachHang=maKhachHang).update(trangThai="hết hoạt động")
        messages.success(requesth, 'Xoá thành dịch vụ thành công!')
        return redirect('khachhang_list')
    return render(requesth, 'myapp/delete_product_confirm.html', {})


def nhanvien_list(requesto):
    nhanviens = NhanVien.objects.filter(trangThai="đang hoạt động").order_by('-maNhanVien')
    return render(requesto, 'myapp/nhanvien/nhanvien_list.html', {'nhanviens': nhanviens})


def delete_nhanvien(request, maNhanVien):
    if request.method == 'GET':
        NhanVien.objects.filter(maNhanVien=maNhanVien).update(trangThai="hết hoạt động")
        messages.success(request, 'Xoá thành nhân viên thành công!')
        return redirect('nhanvien_list')
    return render(request, 'myapp/delete_product_confirm.html', {})


def thuephong_list(requesto):
    thuephongs = ThuePhong.objects.all().order_by('-maThuePhong')
    return render(requesto, 'myapp/don/thuephong_list.html', {'thuephongs': thuephongs})


def traphong_list(requesto):
    traphongs = TraPhong.objects.all().order_by('-maTraPhong')
    return render(requesto, 'myapp/don/traphong_list.html', {'traphongs': traphongs})


def nhanphong_list(requesto):
    nhanphongs = NhanPhong.objects.all().order_by('-maNhanPhong')
    return render(requesto, 'myapp/don/nhanphong_list.html', {'nhanphongs': nhanphongs})


def chitietthue_dichvu(request, maThuePhong):
    thueDichVus = ThueDichVu.objects.filter(thuePhong_id=maThuePhong)
    return render(request, 'myapp/dichvu/thuedichvu_list.html', {'thueDichVus': thueDichVus})
