import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column, Switch
from flet_core.control_event import ControlEvent

def main(page: ft.Page):
    page.title = "Sign in"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 350
    page.window_height = 350
    page.window_min_width = 350
    page.window_min_height = 350
    # page.window_resizable = False

    app_mode: Switch = Switch(label="Light theme", value=False, label_position=ft.LabelPosition.LEFT)
    username: TextField = TextField(label="Username", text_align=ft.TextAlign.LEFT, width=300)
    password: TextField = TextField(label="Password", text_align=ft.TextAlign.LEFT, width=300, password=True, can_reveal_password=True)
    robot: Checkbox = Checkbox(label="I'm not a robot", value=False)
    submit: ElevatedButton = ElevatedButton(text="Sign in", width=200, disabled=True)


    def validate(e: ControlEvent) -> None:
        if all([username.value, password.value, robot.value]):
            submit.disabled = False
        else:
            submit.disabled = True

        page.update()

    def close_dlg(e: ControlEvent):
        dlg_modal.open = False
        page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Login or password error!"),
        actions=[
            ft.TextButton("OK", on_click=close_dlg)
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def open_dlg_modal():
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    def submit_data(e: ControlEvent) -> None:
        print("Username:", username.value)
        print("Password:", password.value)
        if username.value == "uzbek_coder_2022" and password.value == 'qwerty':
            page.clean()
            page.add(
                Row(
                    controls=[Text(value=f"Welcome : {username.value}", size=20)],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            )
        else:
            open_dlg_modal()
            username.value = ''
            password.value = ''


    def validate_mode(e: ControlEvent) -> None:
        value = app_mode.value
        if value:
            app_mode.value = True
            app_mode.label = "Dark theme"
            page.theme_mode = ft.ThemeMode.DARK
        else:
            app_mode.value = False
            app_mode.label = "Light theme"
            page.theme_mode = ft.ThemeMode.LIGHT

        page.update()

    app_mode.on_change = validate_mode
    robot.on_change = validate
    username.on_change = validate
    password.on_change = validate
    submit.on_click = submit_data

    page.add(
        Row(
            controls=[
                Column(
                    [
                        app_mode
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        Row(
            controls=[
                Column(
                    [
                        username,
                        password
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        Row(
            controls=[
                Column(
                    [
                        robot
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        Row(
            controls=[
                Column(
                    [
                        submit
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

if __name__ == "__main__":
    ft.app(target=main)