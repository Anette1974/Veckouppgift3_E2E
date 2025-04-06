import re

import pytest
from playwright.sync_api import Page, expect

"""
US2: 
Som en användare
vill jag kunna byta plats på widgets 
så att jag får dem i en speciell ordning

[ac2:1] Det ska gå att skapa två widgets och byta plats på dem.

[tc2:1]
1. Skapa upp två widgets
2. Byt namn på den sista för att kunna skilja dem åt
3. Kontrollera att det finns en knapp med ikonen av en pil som pekar uppåt som går att trycka på.
4. När man tryckt på knappen med ikonen av en pil uppåt ska den widgeten lägga sig högst upp
"""

#[ac2:1]
def test_move_widget(page: Page):
    page.goto("https://lejonmanen.github.io/timer-vue/")

#1. Skapa upp två widgets
    # Kontrollera att det finns en knapp med texten "Add timer", klicka på knappen "Add timer två gånger"
    button_locator = page.get_by_role("button")
    timer_button = button_locator.get_by_text(re.compile("Add timer"))
    timer_button.click(timeout=2000)
    timer_button.click(timeout=2000)

#2. Byt namn på den sista för att kunna skilja dem åt
    # Klicka på sista rubriken "Break" för att aktivera redigering
    break_headings = page.get_by_role("heading").get_by_text(re.compile("Break"))
    last_heading = break_headings.nth(break_headings.count() - 1)
    last_heading.click()

    # Vänta på att inputfältet visas
    input_fields = page.locator('input[placeholder="Title"]')
    last_input = input_fields.nth(input_fields.count() - 1)

    # Fyll i det med ny text och verifiera
    last_input.fill("Widget no 2")
    expect(last_input).to_have_value("Widget no 2")

#3. Kontrollera att det finns en knapp med ikonen av en pil som pekar uppåt som går att trycka på.
#4. När man tryckt på knappen med ikonen av en pil uppåt ska den widgeten lägga sig högst upp
    last_widget = page.locator(".widget").last
    last_widget.locator(".icon.up").click()
