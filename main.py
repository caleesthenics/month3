import flet as ft 
from datetime import datetime

def main(page: ft.Page):
    page.title = 'My first app!'

    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Hello world!")


    error_text = ft.Text()

    gr_history = []

    # def update_history():
    #     history_controls = [ft.Text('istoriya privetstvii')]

    history_text = ft.Text(f'Istoriya privetstvii:')







    def button(_):
        name = name_input.value.strip()
        age = age_input.value
        time = datetime.now()
        hour = time.strftime('%H')
        

        if name and age :
            if int(hour) >= 6 and int(hour) < 12:
                greeting_text.value = f'{time.strftime("%Y-%m-%d %H:%M")} Dobroe utro {name}. Tebe {age} let'
                name_input.value = None
                age_input.value = None
                error_text.value = None
            
            elif int(hour) >= 12 and int(hour) < 18:
                greeting_text.value = f'{time.strftime("%Y-%m-%d %H:%M")} Dobrii den {name}. Tebe {age} let'
                name_input.value = None
                age_input.value = None
                error_text.value = None
            
            elif int(hour) >= 18 and int(hour) < 24:
                greeting_text.value = f'{time.strftime("%Y-%m-%d %H:%M")} Dobrii ve4er {name}. Tebe {age} let'
                name_input.value = None
                age_input.value = None
                error_text.value = None
            
            elif int(hour) >= 0 and int(hour) < 6:
                greeting_text.value = f'{time.strftime("%Y-%m-%d %H:%M")} Dobroi no4i {name}. Tebe {age} let'
                name_input.value = None
                age_input.value = None
                error_text.value = None
            
            gr_history.append(f'{time.strftime("%Y-%m-%d %H:%M")} - {name}')
            history_text.value = 'istoriya privetstviya:\n' + '\n'.join(gr_history) 

        else:
            error_text.value = 'Pole name ili age ne zapolneno'
        
        page.update()

    name_input = ft.TextField(label = 'vvedite imya:',on_submit = button)
    age_input = ft.TextField(label ='vvedite vozrast',on_submit = button)

    def theme_button(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    def history_remove(_):
        gr_history.clear
        history_text.value = 'Istoriya privetstviya'
        greeting_text.value = 'Hello World!'
        page.update()
        

    knopka2 = ft.IconButton(icon = ft.Icons.SUNNY,on_click = theme_button)

    knopka3 = ft.Button('remove', on_click = history_remove)

    knopka = ft.Button('send', on_click = button) 

    page.add(ft.Row([greeting_text], alignment = ft.MainAxisAlignment.CENTER),name_input,age_input,
             ft.Row([knopka,knopka2,knopka3],alignment= ft.MainAxisAlignment.CENTER),error_text,history_text
    )


ft.app(target = main)

