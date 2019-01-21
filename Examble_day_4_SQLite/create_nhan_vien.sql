--script file
create table if not exists nhan_sinh_vien
(
    id integer primary key autoincrement,
    manv text not null unique,
    tennv text not null,
    luong real default 1000,
    id_phong integer
)
