import Anstract_Base_Class # kế thừa từ module Anstract base class

if __name__=="__main__":
    '''
        module nào đang chạy thì module đó là __main__
        khi nào chương trình này chạy một mình thì mới chạy vào trong main này để chạy
        chạy chương trình nào thì tên name chính là __main__, các cái còn lại là tên của module nó
    
        => phân biệt khu vực đang chạy
    '''

    chu_nhat = Anstract_Base_Class.HINH_CHU_NHAT(10,3)

    print("Hinh Chu Nhat")
    chu_nhat.inthongtin()