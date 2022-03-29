import zipfile


def print_dict(our_dict):
    print("*{:-^22}*".format('*'))
    print("*{:^22}*".format('Частота букв'))
    print("*{:^22}*".format('в романе "Война и мир"'))
    print("*{:-^22}*".format('*'))

    for char, statistics in our_dict.items():
        print("*{:^10}*{:^11}*".format(char, statistics))

    print("*{:-^22}*".format('*'))


def unzip_file(archive):
    zfile = zipfile.ZipFile(archive, 'r')
    for i_file_name in zfile.namelist():
        zfile.extract(i_file_name)

    zfile.close()


def collect_stats(file_name):
    if file_name.endswith('.zip'):
        unzip_file(file_name)
        file_name = ''.join((file_name[:-3], 'txt'))

    read_file = open(file_name, 'r', encoding='utf-8')
    text = read_file.read()
    read_file.close()

    text = text.lower()
    for letter in text:
        if letter.isalpha():
            if letter in word_dict.keys():
                word_dict[letter] += 1
            else:
                word_dict[letter] = 1

    return word_dict


def sort_values(our_dict):
    for i in sorted_values:
        for k in our_dict.keys():
            if our_dict[k] == i:
                sorted_dict[k] = our_dict[k]
                break

    return sorted_dict


word_dict = dict()


file_name = 'voina_i_mir.txt.zip'
stats = collect_stats(file_name)

sorted_values = reversed(sorted(word_dict.values()))
sorted_dict = dict()

stats = sort_values(stats)
print_dict(stats)
