CREATE TABLE KHOA
(
    ma_khoa char(2) primary key,
    ten text not null
);
CREATE TABLE MON_HOC
(
    ma_mon char(4) primary key,
    ten text not null
);
CREATE TABLE SINH_VIEN
(
    ma_sinh_vien char(5) primary key,
    ho text not null,
    ten text not null,
    gioi_tinh char(1) default 1,
    ngay_sinh char(10),
    mail text,
    di_dong text,
    cmnd text unique,
    hoc_bong int default 0 check(hoc_bong>=0),
    ma_khoa char(2),
    foreign key(ma_khoa) references KHOA(ma_khoa)
);
CREATE TABLE KET_QUA
(
    ma_sinh_vien char(5),
    ma_mon char(4),
    diem real default 0 check(diem between 0 and 10),
    primary key(ma_sinh_vien,ma_mon),
    foreign key(ma_sinh_vien) references SINH_VIEN(ma_sinh_vien),
    foreign key(ma_mon) references MON_HOC(ma_mon)
);