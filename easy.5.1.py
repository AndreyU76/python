def path_remove(path_to_remove):
    ui_sure = input('{} {} {}'.format('Вы уверены, что хотите удалить ', path_to_remove, '? Y/N'))
 
    if ui_sure == 'y' or ui_sure == 'Y':
        try:
            os.removedirs(path_to_remove)
            print('Вы успешно удалили ' + path_to_remove)
        except (TypeError, FileNotFoundError):
            print('Не верно указан путь')
    else:
        print('Операция отменена')
 
if __name__ == "__main__":
    for i in range(1, 10):
    path_remove('{}_{}'.format('dir', i))
 
