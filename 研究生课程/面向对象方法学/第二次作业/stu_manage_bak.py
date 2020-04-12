'''
简易学生管理系统
'''
import os
import datetime


def add_info_addr(info_addrs):
    '''
    添加户籍信息
    张三 620423199803023330 2010-9-9 甘肃省白银市经景泰县
    '''
    print('\n添加户籍信息（格式：姓名 身份证号 出生年月日（年-月-日） 住址）-- 使用空格隔开')
    info_list = list(map(str, input('>> ').split(' ')))
    info = {'name': str(info_list[0]), 'no': str(info_list[1]),
            'birthday': str(info_list[2]), 'addr': str(info_list[3])}
    info_addrs.append(info)
    print('\n- 添加成功：%s' % (info))


def add_info_student(info_students): 
    '''
    添加学籍信息
    1151002068 620423199803023330 信息工程学院 计算机科学与技术 2班
    '''
    print('\n添加学籍信息（格式：学号 身份证号 学院 专业 班级）-- 使用空格隔开')
    info_list = list(map(str, input('>> ').split(' ')))
    info = {'student': str(info_list[0]), 'no': str(info_list[1]), 'college': str(
        info_list[2]), 'profession': str(info_list[3]), 'class': str(info_list[4])}
    info_students.append(info)
    print('\n- 添加成功：%s' % (info))


def print_info_addrs(info_addrs):
    '''
    打印户籍信息
    '''
    tplt = '{:^10}\t{:^10}\t{:^15}\t{:10}\t{:^10}'
    print('\n户籍信息 >>>>>\n')
    print(tplt.format('序号', '姓名', '身份证号', '出生年月', '住址'))
    for index, info in enumerate(info_addrs):
        print(tplt.format(index + 1, info['name'],
                          info['no'], str(info['birthday']), info['addr']))


def print_info_students(info_students):
    '''
    打印学籍信息
    '''
    tplt = '{:^10}\t{:^10}\t{:^15}\t{:^15}\t{:^15}\t{:^15}'
    print('\n学籍信息 >>>>>\n')
    print(tplt.format('序号', '学号', '身份证号', '学院', '专业', '班级'))
    for index, info in enumerate(info_students):
        print(tplt.format(index + 1, info['student'], info['no'],
                          info['college'], info['profession'], info['class']))


def print_info_bases(info_addrs, info_students):
    '''
    打印基础信息
    '''
    tplt = '{:^10}\t{:^10}\t{:^20}\t{:^20}\t{:^15}\t{:^15}'
    print('\n基础信息 >>>>>\n')
    print(tplt.format('序号', '学号', '姓名', '年龄', '学院', '班级'))
    for index, info_student in enumerate(info_students):
        addr_index = get_info_base(
            info_student['no'], info_addrs)  # 根据身份证号获取学生户籍信息
        if addr_index is not -1:
            name = info_addrs[addr_index]['name']  # 学生姓名
            year = int(info_addrs[addr_index]
                       ['birthday'].split('-')[0])  # 获取出生年份
            age = datetime.datetime.now().year - year  # 计算年龄
        else:
            print('- 户籍信息查询错误')
            name = ''
            age = 0
        print(tplt.format(index + 1, info_student['student'], name,
                          age, info_student['profession'], info_student['class']))


def get_info_base(no, info_addrs):
    '''
    根据学生身份证号获取户籍信息
    '''
    for index, info in enumerate(info_addrs):
        if info['no'] == no:
            return index
    return -1


def int_input():
    '''
    输入整数异常捕获
    '''
    while True:
        try:
            select_index = int(input('请输入选项：'))
            return select_index
        except:
            print('\n- ！！！请输入整数序号\n')


def print_menu():
    '''
    打印菜单
    '''
    print('-'*50)
    print('简易学生管理系统'.center(25, chr(12288)))
    print('0.添加户籍信息')
    print('1.添加学籍信息')
    print('2.打印户籍信息')
    print('3.打印学籍信息')
    print('4.打印基础信息')
    print('5.退出')
    print('-'*50)


def select_menu(info_addrs, info_students):
    '''
    选择菜单
    '''
    index = int_input()
    if index is 0:
        add_info_addr(info_addrs)  # 添加户籍信息
        # add_info_student(info_students)  # 添加学籍信息
    elif index is 1:
        add_info_student(info_students)  # 添加学籍信息
        # add_info_addr(info_addrs)  # 添加户籍信息
    elif index is 2:
        print_info_addrs(info_addrs)  # 打印户籍信息
    elif index is 3:
        print_info_students(info_students)  # 打印学籍信息
    elif index is 4:
        print_info_bases(info_addrs, info_students)  # 打印基础信息
    elif index is 5:
        print('\n- GOOBYE\n')
        os._exit(0)
    else:
        print('\n- ！！！请输入正确的序号\n')
        select_menu(info_addrs, info_students)


def main():
    info_addrs = []  # 户籍信息
    info_students = []  # 学籍信息

    while True:
        print_menu()
        select_menu(info_addrs, info_students)


if __name__ == '__main__':
    main()
