import flet as ft
import time

def main(page: ft.Page):
    page.title = 'Training Program'

    page.scroll = 'auto'

    progress = ft.ProgressBar(width=100,value = 0,visible= False)

    page.theme_mode = ft.ThemeMode.DARK

    page.window.width =460
    page.window.height = 600

    start_text = ft.Text('This program will help you increase your one-rep max in 12 weeks')

    programm_text = ft.Text('')
    programm_text1 = ft.Text('')
    programm_text2 = ft.Text('')
    programm_text3 = ft.Text('')

    error_text = ft.Text(color= ft.Colors.RED)

    week = []
    percent = []
    sets = []
    reps = []
    working_weight = []

    def round_to_five(weight):
        return round(weight / 5) * 5

    def program(_):
        error_text.value = ''
        try:
            current_weight = float(current_max.value)
        except:
            error_text.value = 'Please enter a number only'
            programm_text.value = ''
            programm_text1.value = ''
            programm_text2.value = ''
            programm_text3.value = ''
            page.update()
            return
        
        progress.visible = True

        programm_text.value = ''
        programm_text1.value = ''
        programm_text2.value = ''
        programm_text3.value = ''

        plan = [{"week": 1, "percent": 70, "sets": 5, "reps": 5},
        {"week": 2, "percent": 72.5, "sets": 5, "reps": 5},
        {"week": 3, "percent": 75, "sets": 4, "reps": 5},
        {"week": 4, "percent": 85, "sets": 3, "reps": 3},
        {"week": 5, "percent": 88, "sets": 4, "reps": 2},
        {"week": 6, "percent": 70, "sets": 3, "reps": 5},
        {"week": 7, "percent": 77.5, "sets": 5, "reps": 4},
        {"week": 8, "percent": 87.5, "sets": 3, "reps": 2},
        {"week": 9, "percent": 90, "sets": 3, "reps": 2},
        {"week": 10, "percent": 70, "sets": 3, "reps": 3},
        {"week": 11, "percent": 85, "sets": 2, "reps": 2},
        {"week": 12, "percent": 105, "sets": 1, "reps": 1},]
        
        programm_text.value = 'Training plan for 12 weeks:\n'

        for i,week_data in enumerate(plan[:6]):
            week = week_data["week"]
            percent = week_data["percent"]
            sets = week_data["sets"]
            reps = week_data["reps"]
            weight = round(current_weight * percent / 100, 1)
            working_weight = round_to_five(weight)
            programm_text1.value += (f"\nWeek №{week}."
            f"\n{percent}% of one-rep max"
            f"\nSets: {sets}, Reps: {reps}"
            f"\nWorking weight: {working_weight}kg")
            progress.value = (i + 1) / len(plan)
            time.sleep(0.5)
            page.update()
        
        for i,week_data in enumerate(plan[6:]):
            week = week_data["week"]
            percent = week_data["percent"]
            sets = week_data["sets"]
            reps = week_data["reps"]
            weight = round(current_weight * percent / 100, 1)
            working_weight = round_to_five(weight)
            programm_text2.value += (f"\nWeek №{week}."
            f"\n{percent}% of one-rep max"
            f"\nSets: {sets}, Reps: {reps}"
            f"\nWorking weight: {working_weight}kg")
            progress.value = (i + 7) / len(plan)
            time.sleep(0.5)
            page.update()
        
        programm_text3.value = (f'\nOn the last training session:'
        f'\nU can try 110% if 105% is done: {round_to_five(current_weight / 100 * 110)}Kg')
        
        current_max.value = ''
        error_text.value = ''
        progress.value = 1
        progress.visible = False
        page.update()
        
    def clear(_):
        if programm_text3.value != '':
            error_text.value = ''
            programm_text.value = ''
            programm_text1.value = ''
            programm_text2.value = ''
            programm_text3.value = ''
            progress.value = 0
        else:
            error_text.value = 'Generate first or wait until its finished'
            error_text.color = ft.Colors.RED
        page.update()
    
    def theme_button(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()
    
    def TXT(_):
        with open('Training.txt','w') as file:
            if programm_text3.value != '':
                file.write("Training plan for 12 weeks:\n")
                file.write(programm_text1.value + "\n")
                file.write(programm_text2.value + "\n")
                file.write(programm_text3.value + "\n")
                error_text.value = 'File saved as Training.txt'
                error_text.color = ft.Colors.WHITE
            else:
                error_text.value = 'Generate first to save it'
                error_text.color = ft.Colors.RED
            page.update()



    button = ft.ElevatedButton('Generate',on_click = program)
 
    button1 = ft.IconButton(icon = ft.Icons.SUNNY,on_click = theme_button)

    button2 = ft.ElevatedButton('Clear',on_click= clear)

    button3 = ft.ElevatedButton('Convert to TXT',on_click = TXT)

    current_max = ft.TextField(label = 'Input your current one-rep max',on_submit= program)


    page.add(ft.Row([start_text], alignment= ft.MainAxisAlignment.CENTER),
             ft.Row([current_max], alignment= ft.MainAxisAlignment.CENTER),
             ft.Row([button, button2,button3, button1], alignment= ft.MainAxisAlignment.CENTER),
             ft.Row([progress], alignment= ft.MainAxisAlignment.CENTER),
             ft.Row([error_text], alignment= ft.MainAxisAlignment.CENTER),
             ft.Row([programm_text], alignment= ft.MainAxisAlignment.CENTER),
             ft.Row([programm_text1,programm_text2], alignment= ft.MainAxisAlignment.CENTER),
             ft.Row([programm_text3], alignment= ft.MainAxisAlignment.CENTER))

ft.app(target = main)