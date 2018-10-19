#Удовиченко Андрей

fruit_list = ['банан', 'апельсин', 'яблоко', 'груша']
another_list = ['киви', 'банан', 'персик', 'яблоко']
sort_list = list (set (fruit_list) & set (another_list))
print(sort_list)
