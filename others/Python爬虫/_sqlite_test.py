#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   sqlite3.py
@Time    :   2020/08/25 10:26:44
@Author  :   Aiken 
@Version :   1.0
@Contact :   ybqu@cnu.edu.cn
@License :   
@Desc    :   None
'''

# here put the import lib
import sqlite3


def main():
    # 1. 打开或创建数据库文件
    conn = sqlite3.connect('test.db')

    cursor = conn.cursor()

    # 2. 创建表
    # sql = '''
    #     create table company
    #         (id int primary key not null,
    #         name text not null,
    #         age int not null,
    #         address char(50),
    #         salary real)
    # '''

    # 3. 插入数据
    # sql = '''
    #     insert into company (id, name, age, address, salary)
    #         values (2, '李四', 30, '北京', 10000)
    # '''

    # 4. 查询数据
    # sql = '''
    #     select * from company
    # '''
    # data = cursor.execute(sql)
    # for raw in data:
    #     print(raw)

    # 5. 删除数据
    # sql = '''
    #     delete from company where id='1'
    # '''

    # 6. 修改数据
    sql = '''
        update company set name='张三' where id='2'
    '''

    cursor.execute(sql)
    conn.commit()
    conn.close()

    

if __name__ == "__main__":
    main()