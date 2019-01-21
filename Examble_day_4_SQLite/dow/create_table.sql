create table Ket_qua
(
    ma_sinh_vien char(5),
    ma_mon char(4),
    diem real default 0 check(between 0 and 10)
);