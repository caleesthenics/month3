import flet as ft 
from datetime import datetime

def main(page: ft.Page):
    page.title = 'My first app!'

    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Hello world!")

    name_input = ft.TextField(label = 'vvedite imya:')

    age_input = ft.TextField(label = 'vvedite vozrast')

    error_text = ft.Text()

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

        else:
            error_text.value = 'Pole name ili age ne zapolneno'
        
        page.update()

    
    def theme_button(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()


    knopka2 = ft.IconButton(icon = ft.Icons.BRIGHTNESS_7,on_click = theme_button)
                            
    knopka = ft.Button('send', on_click = button) 

    page.add(greeting_text, name_input,age_input, knopka,knopka2, error_text)


ft.app(target = main)

