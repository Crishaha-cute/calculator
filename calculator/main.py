from importlib.metadata import pass_none

from tkinter import Label

import flet as ft

def main(page: ft.Page):
    page.window.width = 360
    page.window.height = 740
    page.bgcolor = "blue"
    page.window.resizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    num1 = ft.TextField(width=100, height=40, text_size=14, border_radius=5, border_width=2, label_style=ft.TextStyle(size=15), border_color="white",text_align = ft.TextAlign.CENTER)
    num2 = ft.TextField( width=100, height=40, text_size=14, border_radius=5, border_width=2, label_style=ft.TextStyle(size=15), border_color="white",text_align = ft.TextAlign.CENTER)

    def add(e):
        try:
            n1 = float(num1.value)
            n2 = float(num2.value)
            result = n1 + n2
            page.add(ft.Text(f"Sum is: {result}", size=20, color="black", font_family="Arial", weight=ft.FontWeight.BOLD))
        except ValueError:
            page.add(ft.Text("Invalid Input", size=20, color="black", font_family="Arial", weight=ft.FontWeight.BOLD))
    page.update()

    def sub(e):
        try:
            n1 = float(num1.value)
            n2 = float(num2.value)
            result = n1 - n2
            page.add(ft.Text(f"Difference is: {result}", size=20, color="black", font_family="Arial",
                             weight=ft.FontWeight.BOLD))
        except ValueError:
            page.add(
                ft.Text("Invalid Input", size=20, color="black", font_family="Arial", weight=ft.FontWeight.BOLD))
        page.update()

    def div(e):
        try:
            n1 = float(num1.value)
            n2 = float(num2.value)
            result = n1 / n2
            page.add(ft.Text(f"Quotient is: {result}", size=20, color="black", font_family="Arial",
                             weight=ft.FontWeight.BOLD))
        except ValueError:
            page.add(
                ft.Text("Invalid Input", size=20, color="black", font_family="Arial", weight=ft.FontWeight.BOLD))
        page.update()

    def clear(e):
        num1.value = ""
        num2.value = ""
        page.update()



    page.add(
    ft.Text("SIMPLE CALCULATOR", size=25, color="white", font_family="Arial", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
    num1,
    num2,
        ft.Row(
            [
                ft.ElevatedButton("+", on_click=add, width=40, height=30, bgcolor="green", color="black"),
                ft.ElevatedButton("-", on_click=sub, width=40, height=30, bgcolor="green",color="black"),
                ft.ElevatedButton("/", on_click=div, width=40, height=30, bgcolor="green",
                                  color="black"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        ),
    ft.ElevatedButton("Clear",on_click=clear,width=100,height=50, bgcolor="white",color="blue"),
    )
ft.app(main)
