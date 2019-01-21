-- note: sql có phân biệt chữ thường chữ hoa khi so sánh

select * 
from sinh_vien
where ma_khoa='CN' and gioi_tinh = 1
-- lấy người tên là Tuấn
select * from sinh_vien
where ten ='Tuấn';

-- tìm tên là "Mạnh Tuấn"
select * from sinh_vien
where ten='Tuấn' and ho like '%Mạnh%';

-- tùy chọn lấy thông tin
select ho,ten, ma_so
from sinh_vien

-- lấy người có mã số là C0007
select *
from sinh_vien
where ma_so ='C0007';

-- lấy khoảng thông tin
select *
from sinh_vien
where ma_so between 'C0005' and 'C0012';

--truy vấn nhiều bảng có liên kết với nhau 1
select *
from sinh_vien s join khoa k on s.ma_khoa = k.ma_so;select *

--truy vấn nhiều bảng có liên kết với nhau 2
select s.ma_so, s.ho, s.ten, s.gioi_tinh, s.ma_khoa, k.ten
from sinh_vien s join khoa k on s.ma_khoa = k.ma_so;