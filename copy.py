import flet as ft
from db import main_db

def main(page: ft.Page):
    page.title = 'ToDo list'
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    task_list = ft.Column(spacing = 10)

    def create_task_row(task_id, task_text):
        task_field = ft.TextField(value = task_text,read_only= True, expand = True, on_submit= save_edit)

        def enable_edit(_):
            task_field.read_only = False
            task_field.update()
        
        def save_edit(_):
            main_db.update_task(task_id = task_id, new_task= task_field.value)
            task_field.read_only =True
            task_field.update()
            page.update()

        enable_button = ft.IconButton(icon= ft.Icons.EDIT, tooltip= 'Редактировать', on_click = enable_edit)

        save_button = ft.IconButton(icon = ft.Icons.SAVE_ALT_ROUNDED,on_click= save_edit)


        return ft.Row([task_field, enable_button,save_button])
    
    def load_task():
        task_list.controls.clear()
        for task_id, task_text in main_db.get_tasks():
            task_list.controls.append(create_task_row(task_id = task_id, task_text =task_text))
        page.update()


    
    def add_task(_):
        if task_input.value:
            task = task_input.value
            task_id = main_db.add_task(task)
            task_list.controls.append(create_task_row(task_id = task_id , task_text = task))
            task_input.value = ''
            page.update()


    task_input = ft.TextField(label = 'Введите задачу', expand = True, on_submit= add_task)
    add_button = ft.IconButton(icon=ft.Icons.ADD, tooltip= 'Добавить задачу',on_click= add_task )
    
    page.add(ft.Row([task_input,add_button, ]),task_list)

    load_task()

if __name__  == '__main__':
    main_db.init_db()
    ft.app(target = main)
