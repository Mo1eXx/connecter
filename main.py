import flet as ft
from ipName import open_text

all_ip = open_text('test.txt')

persons = []

for ip in all_ip:
    person = {}
    person['name'] = str(ip)
    person['ip'] = ip
    persons.append(person)


class TextSearch(ft.TextField):
    def __init__(self, persons, text_view):
        super().__init__(label='Search', expand=True)
        self.persons = persons
        self.text_view = text_view
        self.on_change = self.update_text_view

    def update_text_view(self, e):
        self.text_view.selected_row = None
        search_term = self.value.lower()
        filtered_persons = [
            person for person in self.persons
            if search_term in person['name'].lower() or
               search_term in person['ip'].lower()
        ]
        self.text_view.my_build(filtered_persons)
        self.text_view.update()


class BaseButton(ft.IconButton):
    def __init__(self, icon, on_click=None):
        super().__init__(icon=icon, on_click=on_click)
        self.icon = icon
        self.on_click = on_click


class TextView(ft.ListView):
    def __init__(self, persons, button=None):
        super().__init__()
        self.persons = persons
        self.button = button
        self.my_build(self.persons)
        self.selected_row = None

    def my_build(self, persons):
        self.controls.clear()
        scrollable = ft.Container(
            content=ft.Column(
                controls=[
                    self.create_persons_row(person) for person in persons
                ],
                scroll=ft.ScrollMode.ALWAYS
            ),
            height=300
        )
        self.controls.append(scrollable)

    def create_persons_row(self, person):
        person_name = ft.Text(
            person['name'],
            expand=True
        )
        person_ip = ft.Text(
            person['ip'],
            expand=True
        )
        row = ft.Container(ft.Row(
            [
                person_name,
                person_ip,
                self.button
            ]
        ))
        container = ft.Container(
            row,
            on_hover=lambda e, r=row: self.on_hover(e, r),
        )
        container.on_click = lambda e, с=container: self.on_click(e, с)
        return container

    def on_click(self, e, container):

        if self.selected_row is not None:
            self.selected_row.bgcolor = ft.colors.TRANSPARENT
            self.selected_row.update()
        self.selected_row = container
        self.selected_row.bgcolor = ft.colors.SURFACE_VARIANT
        self.selected_row.update()

    def on_hover(self, e, row):
        if e.data == 'true':
            if self.selected_row is not row:
                row.bgcolor = ft.colors.BLACK38
        else:
            if self.selected_row is not row:
                row.bgcolor = ft.colors.TRANSPARENT
        row.update()

    def get_selected_ip(self):
        if self.selected_row is not None:
            index = self.controls.index(self.selected_row)
            return self.persons[index]['ip']
        return None


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 600
    page.window.height = 400
    page.window.center()
    page.title = 'UPF List'
    button_disk = BaseButton(
        icon=ft.icons.FOLDER_SHARED,
    )
    text_view = TextView(persons, button_disk)
    text_search = TextSearch(persons, text_view)

    def on_keyboard_button_click(e):
        ip = text_view.get_selected_ip()
        if ip:
            page.add(ft.Text(f'Connecting to {ip}'))

    def on_connect_button_click(e):
        ip = text_view.get_selected_ip()
        if ip:
            page.add(ft.Text(f'Connecting to {ip}'))

    connect_button = BaseButton(
        icon=ft.icons.CONNECTED_TV,
        on_click=on_connect_button_click
    )
    keyboard_button = BaseButton(
        icon=ft.icons.KEYBOARD,
        on_click=on_keyboard_button_click
    )
    page.add(
        ft.Row(
            [
                text_search,
                keyboard_button,
                connect_button
            ]
        ),
        text_view
    )


ft.app(target=main)
