from tkinter import *
import tkinter.ttk as ttk
import psycopg2
import sqlite3
from mysql.connector import connect, Error


class Window:
    def __init__(self):
        self.connection = psycopg2.connect(user="postgres",
                                           # пароль, который указали при установке PostgreSQL
                                           password="2468ktveh",
                                           host="localhost",
                                           port="5432",
                                           database="postgres")
        self.cursor = self.connection.cursor()
        self.conn_sqlite = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
        self.cursor_sqlite = self.conn_sqlite.cursor()
        # Tkinter
        self.mainmenu = Menu(root)
        root.config(menu=self.mainmenu)
        self.mainmenu.add_command(label="Export DB1 to DB2", command=self.export_DB1_DB2)
        self.mainmenu.add_command(label="Export DB2 to DB3", command=self.export_DB2_DB3)
        self.left_frame = Frame(root, height=300, width=100)
        self.top_frame = Frame(root, height=300, width=300)
        self.right_frame = Frame(root, bg="white", height=300, width=868)
        self.bottom_frame = Frame(root, height=300, width=1068)
        self.id_label = Label(self.left_frame, text="ID:", font=("Times new roman", 24), fg="black")
        self.name_label = Label(self.left_frame, text="Name:", font=("Times new roman", 24), fg="black")
        self.firm_label = Label(self.left_frame, text="Firm:", font=("Times new roman", 24), fg="black")
        self.model_label = Label(self.left_frame, text="Model:", font=("Times new roman", 24), fg="black")
        self.size_label = Label(self.left_frame, text="Size:", font=("Times new roman", 24), fg="black")
        self.price_label = Label(self.left_frame, text="Price:", font=("Times new roman", 24), fg="black")
        self.material_label = Label(self.left_frame, text="Material:", font=("Times new roman", 24), fg="black")
        self.colour_label = Label(self.left_frame, text="Colour:", font=("Times new roman", 24), fg="black")
        self.status_label = Label(self.left_frame, text="Status:", font=("Times new roman", 24), fg="black")
        self.id_entry = Entry(self.top_frame, width=20, bd=3, font=("Times new roman", 20))
        self.name_entry = Entry(self.top_frame, width=20, bd=3, font=("Times new roman", 20))
        self.firm_entry = Entry(self.top_frame, width=20, bd=3, font=("Times new roman", 20))
        self.model_entry = Entry(self.top_frame, width=20, bd=3, font=("Times new roman", 20))
        self.size_entry = Entry(self.top_frame, width=20, bd=3, font=("Times new roman", 20))
        self.price_entry = Entry(self.top_frame, width=20, bd=3, font=("Times new roman", 20))
        self.material_entry = Entry(self.top_frame, width=20, bd=3, font=("Times new roman", 20))
        self.colour_entry = Entry(self.top_frame, width=20, bd=3, font=("Times new roman", 20))
        self.status_entry = Entry(self.top_frame, width=20, bd=3, font=("Times new roman", 20))
        self.create_button = Button(self.right_frame, text="Add", font=("Times new roman", 16), width=20,
                                    command=self.add_value)
        self.update_button = Button(self.right_frame, text="Update", font=("Times new roman", 16), width=20,
                                    command=self.update_value)
        self.delete_button = Button(self.right_frame, text="Delete", font=("Times new roman", 16), width=20,
                                    command=self.delete_value)
        # Таблица
        columns = ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9")
        self.data_tree = ttk.Treeview(self.bottom_frame, show="headings", columns=columns)
        self.data_tree.heading("#1", text="ID")
        self.data_tree.heading("#2", text="Name")
        self.data_tree.heading("#3", text="Firm")
        self.data_tree.heading("#4", text="Model")
        self.data_tree.heading("#5", text="Size")
        self.data_tree.heading("#6", text="Price")
        self.data_tree.heading("#7", text="Material")
        self.data_tree.heading("#8", text="Colour")
        self.data_tree.heading("#9", text="Status")
        for i in columns:
            self.data_tree.column("{0}".format(i), width=83)
        self.insert_in_tree()
        self.left_frame.grid(row=0, column=0, sticky=W)
        self.top_frame.grid(row=0, column=1, sticky=N)
        self.right_frame.grid(row=0, column=2, sticky=W)
        self.bottom_frame.grid(row=1, column=0, columnspan=3, sticky=W)
        self.id_label.grid(row=0, column=0, sticky=W)
        self.name_label.grid(row=1, column=0, sticky=W)
        self.firm_label.grid(row=2, column=0, sticky=W)
        self.model_label.grid(row=3, column=0, sticky=W)
        self.size_label.grid(row=4, column=0, sticky=W)
        self.price_label.grid(row=5, column=0, sticky=W)
        self.material_label.grid(row=6, column=0, sticky=W)
        self.colour_label.grid(row=7, column=0, sticky=W)
        self.status_label.grid(row=8, column=0, sticky=W)
        self.id_entry.grid(row=0, column=0, sticky=W)
        self.name_entry.grid(row=1, column=0, pady=2)
        self.firm_entry.grid(row=2, column=0)
        self.model_entry.grid(row=3, column=0, pady=2)
        self.size_entry.grid(row=4, column=0, pady=2)
        self.price_entry.grid(row=5, column=0)
        self.material_entry.grid(row=6, column=0)
        self.colour_entry.grid(row=7, column=0)
        self.status_entry.grid(row=8, column=0, pady=5)
        self.create_button.grid(row=0, column=2)
        self.update_button.grid(row=1, column=2)
        self.delete_button.grid(row=2, column=2)
        self.data_tree.grid(row=0, column=0)

    def export_DB2_DB3(self):
        """Перенос данных с базы данных SQLite в MySQL с изменение статуса за определенной ID"""
        self.cursor_sqlite.execute("""UPDATE salon set status = 'Ready' where id = 3""")
        self.conn_sqlite.commit()
        self.cursor_sqlite.execute('SELECT * from salon')
        values = self.cursor_sqlite.fetchall()
        print(values)
        win_db3 = Toplevel(root)
        win_db3.title("MySQL")
        win_db3.geometry("215x230")
        columns = ("#1", "#2", "#3")
        data3_tree = ttk.Treeview(win_db3, show="headings", columns=columns)
        data3_tree.heading("#1", text="ID")
        data3_tree.heading("#2", text="Name")
        data3_tree.heading("#3", text="Status")
        for i in columns:
            data3_tree.column("{0}".format(i), width=70)
        try:
            with connect(
                    host="localhost",
                    user="root",
                    password="13579ktvehA",
                    database="salon",
            ) as connection:
                check = """DROP TABLE IF EXISTS salon"""
                temp = """CREATE TABLE salon(id INT PRIMARY KEY, name VARCHAR(100), status VARCHAR(100))"""
                with connection.cursor() as cursor:
                    cursor.execute(check)
                    connection.commit()
                with connection.cursor() as cursor:
                    cursor.execute(temp)
                    connection.commit()
                with connection.cursor() as cursor:
                    for i in values:
                        cursor.execute(
                            """INSERT INTO salon(id, name, status) VALUES({0}, '{1}', '{2}')""".format(int(i[0]), i[1],
                                                                                                       i[2]))
                        connection.commit()
                    cursor.execute("SELECT * from salon")
                    for i in sorted(cursor.fetchall()):
                        data3_tree.insert("", END, values=i)
            data3_tree.grid(row=0, column=0)
        except Error as e:
            print(e)

    def export_DB1_DB2(self):
        """Функция для експорта данных с базы данных PostgresSQL в базу данных SQLite"""
        self.cursor_sqlite.execute('DROP TABLE IF EXISTS salon')
        self.cursor_sqlite.execute("""CREATE TABLE salon (id INT, name text, status text)""")
        win_db2 = Toplevel(root)
        win_db2.geometry("215x230")
        win_db2.title("SQLite")
        columns = ("#1", "#2", "#3")
        data2_tree = ttk.Treeview(win_db2, show="headings", columns=columns)
        data2_tree.heading("#1", text="ID")
        data2_tree.heading("#2", text="Name")
        data2_tree.heading("#3", text="Status")
        for i in columns:
            data2_tree.column("{0}".format(i), width=70)
        self.cursor.execute('SELECT * from salon')
        arr_values = self.cursor.fetchall()
        export_values = [(arr_values[0][0], arr_values[0][1], arr_values[0][8]),
                         (arr_values[1][0], arr_values[1][1], arr_values[1][8]),
                         (arr_values[2][0], arr_values[2][1], arr_values[2][8]),
                         (arr_values[3][0], arr_values[3][1], arr_values[3][8])]
        for i in export_values:
            self.cursor_sqlite.execute("INSERT INTO salon VALUES ('{0}', '{1}', '{2}')".format(*i))
        self.conn_sqlite.commit()
        self.cursor_sqlite.execute('SELECT * from salon')
        for i in sorted(self.cursor_sqlite.fetchall()):
            data2_tree.insert("", END, values=i)
        data2_tree.grid(row=0, column=0)

    def add_value(self):
        """Функция добавление значений в таблицу"""
        global arr_for_insert
        arr_for_insert = [int(self.id_entry.get()), self.name_entry.get(), self.firm_entry.get(),
                          self.model_entry.get(), self.size_entry.get(), self.price_entry.get(),
                          self.material_entry.get(), self.colour_entry.get(), self.status_entry.get()]
        self.cursor.execute(
            """INSERT INTO salon (id, name, firm, model, size, price, material, colour, status) VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})""".format(
                *arr_for_insert))
        self.connection.commit()
        x = self.data_tree.get_children()
        for item in x:
            self.data_tree.delete(item)
        self.insert_in_tree()

    def delete_value(self):
        """Удаление строки по заданному ID"""
        global id_delete_entry
        win_delete = Toplevel(root)
        win_delete.geometry("200x150")
        id_delete_label = Label(win_delete, text="ID:", font=("Times new roman", 24), fg="black")
        id_delete_entry = Entry(win_delete, width=3, bd=3, font=("Times new roman", 20))
        accept_button = Button(win_delete, text="Accept", font=("Times new roman", 16), width=6,
                               command=self.accept_delete)
        id_delete_label.grid(row=0, column=0)
        id_delete_entry.grid(row=0, column=1)
        accept_button.grid(row=0, column=2)

    def accept_delete(self):
        """Подтверждение удаления строки"""
        global id_delete_entry
        delete_query = """Delete from salon where id = {0}""".format(int(id_delete_entry.get()))
        self.cursor.execute(delete_query)
        self.connection.commit()
        x = self.data_tree.get_children()
        for item in x:
            self.data_tree.delete(item)
        self.insert_in_tree()

    def update_value(self):
        """Окно изменения статуса по ID"""
        global id_update_entry, status_update_entry
        win_update = Toplevel(root)
        win_update.geometry("240x180")
        id_update_label = Label(win_update, text="ID:", font=("Times new roman", 24), fg="black")
        id_update_entry = Entry(win_update, width=3, bd=3, font=("Times new roman", 20))
        status_update_entry = Entry(win_update, width=6, bd=3, font=("Times new roman", 20))
        status_update_label = Label(win_update, text="Status:", font=("Times new roman", 24), fg="black")
        status_update_button = Button(win_update, text="Update", font=("Times new roman", 16), width=6,
                                      command=self.accept_update)
        id_update_label.grid(row=0, column=0)
        id_update_entry.grid(row=0, column=1)
        status_update_label.grid(row=1, column=0)
        status_update_entry.grid(row=1, column=1)
        status_update_button.grid(row=2, column=0, columnspan=2)

    def accept_update(self):
        """Подтверждение изменения статуса"""
        global id_update_entry, status_update_entry
        update_query = """Update salon set status = '{0}' where id = {1}""".format(status_update_entry.get(),
                                                                                   int(id_update_entry.get()))
        print(update_query)
        self.cursor.execute(update_query)
        self.connection.commit()
        x = self.data_tree.get_children()
        for item in x:
            self.data_tree.delete(item)
        self.insert_in_tree()

    def insert_in_tree(self):
        """Функия для занесения данных в таблицу"""
        self.cursor.execute('SELECT * from salon')
        for n in sorted(self.cursor.fetchall()):
            self.data_tree.insert("", END, values=n)


# Главное окно
root = Tk()
root.geometry("750x605")
obj = Window()
root.mainloop()
