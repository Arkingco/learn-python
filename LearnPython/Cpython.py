import ctypes


class IntStruct(ctypes.Structure):
    _fields_ = [("ob_refcnt", ctypes.c_long),
                ("ob_type", ctypes.c_void_p),
                ("ob_size", ctypes.c_ulong),
                ("ob_digit", ctypes.c_long)]

    def __repr__(self):
        return ("IntStruct(ob_digit={self.ob_digit}, "
                "refcount={self.ob_refcnt})").format(self=self)


class ListStruct(ctypes.Structure):
    _fields_ = [("ob_refcnt", ctypes.c_long),
                ("ob_type", ctypes.c_void_p),
                ("ob_size", ctypes.c_ulong),
                ("ob_item", ctypes.c_long),  # PyObject** pointer cast to long
                ("allocated", ctypes.c_ulong)]

    def __repr__(self):
        return ("ListStruct(len={self.ob_size}, "
                "refcount={self.ob_refcnt})").format(self=self)


def Check_IntStruct(num):
    IntStruct.from_address(id(42))
    print(all(i == IntStruct.from_address(id(i)).ob_digit for i in range(4000)))


L = [1, 2, 3, 4, 5]
# 리스트의 포인터를 가져온다
Lstruct = ListStruct.from_address(id(L))

#  정수 포인터 배열을 L과 크기가 같게 만든다
PtrArray = Lstruct.ob_size * ctypes.POINTER(IntStruct)

# instantiate this type using the ob_item pointer
L_values = PtrArray.from_address(Lstruct.ob_item)

# ptr[0] dereferences the pointer
prt = [ptr[0] for ptr in L_values]

for i in prt:
    print(i)








