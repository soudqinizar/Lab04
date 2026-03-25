import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2026 - Lab 04 - SpellChecker++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

    @property
    def print(self):
        return self.__print

    @property
    def textfield(self):
        return self.__textfield

    @property
    def lingue(self):
        return self.__lingue

    @property
    def ricerca(self):
        return self.__ricerca





        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here

        testoLingua = ft.Text("")
        def cambia_lingua(e):
            lingua = e.control.value
            testoLingua.value = f"Hai scelto: {lingua}"
            self.page.update()
            return lingua

        self.__lingue = ft.Dropdown(
            value="Scegli una lingua",
            options=[
                ft.dropdown.Option(key="italian", text="Italiano"),
                ft.dropdown.Option(key="english", text="Inglese"),
                ft.dropdown.Option(key="spanish", text="Spagnolo")
            ],
            on_change=cambia_lingua  # 👈 qui agganci l'evento
        )

        self.page.add(self.__lingue ,testoLingua)


        testoRicerca = ft.Text("")

        def tipoRicerca(e):
            ricerca = e.control.value
            testoRicerca.value = f"Hai scelto: {ricerca}"
            self.page.update()
            return ricerca

        self.__ricerca = ft.Dropdown(
            value="Scegli una delle seguenti opzioni",
            options=[
                ft.dropdown.Option(key="Default", text="Default"),
                ft.dropdown.Option(key="Linear", text="Linear"),
                ft.dropdown.Option(key="Dichotomic", text="Dichotomic")
            ],
            on_change= tipoRicerca  # 👈 qui agganci l'evento
        )

        self.__textfield = ft.TextField(label="Scrivi qualcosa")

        self._btnCorrezione = ft.ElevatedButton(text = "Clicca qui",
                                                on_click= self.__controller.check, width=200)

        row2 = ft.Row([self.__ricerca, testoRicerca, self.__textfield, self._btnCorrezione])

        self.page.add(row2)

        self.__print = ft.ListView(expand=True)
        self.page.add(self.__print)



        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
