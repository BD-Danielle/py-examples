# ch9_6.py 
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
math_sydi_phys1 = math ^ physics
print(f"沒有同時參加數學和物理夏令營的成員 : {math_sydi_phys1}")
math_sydi_phys2 = math.symmetric_difference(physics)
print(f"沒有同時參加數學和物理夏令營的成員 : {math_sydi_phys2}")




