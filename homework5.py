peremennaya = False #элемент который можео изменить в кортеде
immutable_var = (99, 22, "Bur" " go", peremennaya, "fafnir" )
print(immutable_var)
peremennaya = True
print(immutable_var)
#immutable_var[0] = 0 - нельзя изменить числовое значение, или строку в кортеже,
mutable_list = [ 55, "F", peremennaya, 77]
mutable_list[1] = 0
print(mutable_list)
