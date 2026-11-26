import flet as ft

def main(page: ft.Page):
    prompt='''
    This is my first Flet deployement.
    Make sure the computer and mobile are connected to the same WiFi network.
    '''
    text = ft.Text(value=prompt, size=40,color="orange")
    
    page.add(text)

# ft.run(main)
ft.run(main, view=ft.AppView.WEB_BROWSER)