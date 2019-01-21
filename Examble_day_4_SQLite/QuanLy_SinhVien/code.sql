SELECT * FROM sinh_vien;
--cho biết các sinh viên của khoa CN
SELECT * 
FROM sinh_vien 
WHERE ma_khoa='CN';
--cho biết các sinh viên nam của khoa CN và sắp tăng theo tên
SELECT * 
FROM sinh_vien 
WHERE ma_khoa='CN' AND gioi_tinh=1
ORDER BY ten;
--tìm các sinh viên có tên là Tuấn
SELECT * 
FROM sinh_vien 
WHERE ten='Tuấn';
--tìm các sinh viên có tên là Mạnh Tuấn
SELECT * 
FROM sinh_vien 
WHERE ten='Tuấn' AND ho LIKE '%Mạnh%';
--
SELECT s.ma_so, s.ho, s.ten, s.ma_khoa, k.ten
FROM sinh_vien s JOIN khoa k ON s.ma_khoa=k.ma_so;
--xem điểm của sinh viên C0007
SELECT k.ma_sinh_vien, s.ho||' '||s.ten AS ho_ten, k.ma_mon_hoc, m.ten, k.diem
FROM ket_qua k JOIN sinh_vien s ON k.ma_sinh_vien=s.ma_so
	JOIN mon_hoc m ON m.ma_so=k.ma_mon_hoc
WHERE ma_sinh_vien='C0007';






