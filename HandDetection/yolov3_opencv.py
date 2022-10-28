import os
import random
import re

def split_train_test(train):
    list = []
    d = "C:/Users/cpreg/PycharmProjects/InfinityGrade/FotosTest/images"
    for path in os.listdir(d):
        if path.endswith(".txt"):
            full_path = os.path.join(d, path)
            print(full_path)
            list.append(full_path)

    random.shuffle(list)
    print(list)
    train_list = list[0:int(len(list)*(train/100))]
    test_list = list[len(train_list):]

    train_file = open("C:/Users/cpreg/PycharmProjects/InfinityGrade/FotosTest/train.txt", "w")
    for t1 in train_list:
        train_file.write(t1+'\n')
    train_file.close()

    test_file = open("C:/Users/cpreg/PycharmProjects/InfinityGrade/FotosTest/test.txt", "w")
    for t2 in test_list:
        test_file.write(t2+'\n')
    test_file.close()

def class_0(classe):
    d = "C:/Users/cpreg/PycharmProjects/InfinityGrade/FotosLocal/images"
    for path in os.listdir(d):
        if path.endswith(".txt"):
            full_path = os.path.join(d, path)
            f = open(full_path, "r")
            data = f.readlines()
            f.close()
            write_line = []
            for line in data:
                new_line = line.replace(classe + ' ', '0 ')
                write_line.append(new_line)
            print(write_line)
            if len(data) > 1:
                new_data = write_line[0]+write_line[1]
            else:
                new_data = new_line
            g = open(full_path, 'w')
            g.write(new_data)
            g.close()


if __name__=="__main__":
    classe = str(input('Introdueix Classe del LabelIMG: '))
    class_0(classe)

