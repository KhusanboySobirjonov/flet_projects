import flet as ft
import datetime


def main(page: ft.Page):
    page.window_min_width = 380
    page.window_min_height = 600
    page.window_max_width = 380
    page.window_max_height = 600
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "Kitobcha"

    def app_mode(e):
        if mode.icon == 'wb_sunny':
            page.appbar.bgcolor = "#00497d"
            page.theme_mode = ft.ThemeMode.DARK
            mode.icon = ft.icons.SHIELD_MOON
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            mode.icon = ft.icons.WB_SUNNY
            page.appbar.bgcolor = "#2196f3"
        page.update()

    mode = ft.IconButton(icon=ft.icons.WB_SUNNY, on_click=app_mode, tooltip="Ilova rejimi")

    page.appbar = ft.AppBar(
        title=ft.Text(
            "Kitob sahifalovchi", color=ft.colors.WHITE
        ),
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        actions=[
            mode,
        ],
    )

    program_guide = """    Dasturni ishlatish tartibi :
 1. Sahifalar sonini kiriting.
 2. Bitta sahifada nechta bet joylashishini belgilang.
 3. Bajarish tugmasini bosing.
 4. Chiqqan natijalarni nusxalab oling.
 5. Endi esa printerda shu betlarni chiqarsangiz ma'lumotlarni kitobcha shakliga keltira olasiz.
        """

    entry = ft.TextField(label="Sahifalar sonini kiriting", width=250)

    textbox1 = ft.TextField(label="Tashqi tomon", width=310, max_lines=3, min_lines=3, read_only=True)
    textbox2 = ft.TextField(label="Ichki tomon", width=310, max_lines=3, min_lines=3, read_only=True)
    textbox3 = ft.TextField(label="Dasturni ishlatish bo'yicha qo'llanma", width=360, max_lines=5, min_lines=5,
                            value=program_guide, read_only=True)

    combo = ft.Dropdown(
        label="Betlar soni",
        width=100,
        options=[
            ft.dropdown.Option("1"),
            ft.dropdown.Option("2"),
        ],
    )

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Ma'lumot kiritishda xatolik"),
        actions=[
            ft.TextButton("OK", on_click=close_dlg)
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def open_dlg_modal(title, txt):
        dlg_modal.title = ft.Text(title)
        dlg_modal.content = ft.Text(txt)
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    def copy_clipboard(content):
        if content:
            page.set_clipboard(content)
            open_dlg_modal("Bajarildi", "Matn vaqtinchalik xotiraga nusxalandi!")
        else:
            open_dlg_modal("Ogohlantirish", "Nusxalash uchun hech narsa yo'q.")

    copy_button1 = ft.IconButton(icon=ft.icons.CONTENT_COPY_OUTLINED, on_click=lambda e: copy_clipboard(textbox1.value))
    copy_button2 = ft.IconButton(icon=ft.icons.CONTENT_COPY_OUTLINED, on_click=lambda e: copy_clipboard(textbox2.value))

    label = ft.Text(f"©️ Andijon {datetime.datetime.now().year}")

    button = ft.ElevatedButton(text="Bajarish", width=200)

    def use_page(value, page_count):
        if not page_count.isdigit():
            open_dlg_modal("Ogohlantirish", "Sahifalar soni butun son bo'lishi kerak")
            textbox1.value = ''
            textbox2.value = ''
            return
        page_count = int(page_count)
        left = []
        right = []
        a = 0
        if value == '1':
            a = (page_count + 1) // 2
            left = list(range(1, page_count+1, 2))
            right = list(range(2, page_count+1, 2))
        else:
            a = (page_count + 3) // 4
            n = a * 4
            for i in range(a):
                left.extend([n - 2 * i, 2 * i + 1])
                right.extend([2 * i + 2, n - 2 * i - 1])

        open_dlg_modal("Bajarildi", f"Umumiy {a} ta qog'oz ishlatilinadi. Kitobni chop etish uchun.")

        textbox1.value = ','.join(str(i) for i in left)
        textbox2.value = ','.join(str(i) for i in right)

    button.on_click = lambda e: use_page(combo.value, entry.value)

    page.add(
        ft.Row(
            [
                entry,
                combo
            ]
        ),
        ft.Row(
            [
                textbox1,
                copy_button1
            ]
        ),
        ft.Row(
            [
                textbox2,
                copy_button2
            ]
        ),
        ft.Row(
            [
                textbox3
            ]
        ),
        ft.Row(
            [
                button
            ],
            alignment = ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                label
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

