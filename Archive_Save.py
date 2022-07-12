import os
import zipfile


def archiver(string, filename):
    l = string.split()
    path = 'C:' + '/'.join(l)
    jungle_zip = zipfile.ZipFile(path, 'w')
    jungle_zip.write(archived_file, compress_type=zipfile.ZIP_DEFLATED)

    jungle_zip.close()
    return archived_file


filename = input('Введите имя файла: \n')
string = input('Введите место расположения файла (название папок через пробел): ')

result_archiver = archiver(string, filename)



way = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): \n')
r_path = way.replace(" ", "/")
real_path = os.path.join(r_path, result_archiver)
path = str('C:/' + real_path)
check_file = os.path.exists(path)
if check_file:
    print('Файл с таким именем уже существует!')
    ans_q = input('Вы действительно хотите перезаписать файл? ').lower()
    if ans_q == 'да' or ans_q == 'yes':
        f = open(path, 'w')
        f.write(filename)
        print('Файл успешно перезаписан!')
    else:
        print('Файл не перезаписан')
else:
    f = open(path, 'w')
    f.write(filename)
    print('Файл успешно сохранён!')

