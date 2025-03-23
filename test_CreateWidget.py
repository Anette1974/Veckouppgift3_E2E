import re
from playwright.sync_api import Page, expect

"""
US1: 
Som en användare 
vill jag kunna skapa en widget 
så att jag kan starta en timer

[ac1:1] Det ska gå att klicka på knappen "Add timer" och då ska det skapas upp en ny timer widget

[tc1:1]
1. Kontrollera att det finns en knapp med texten "Add timer", klicka på knappen "Add timer"
2. Kontrollera att den förvalda texten är Break
3. Kontrollera att en widget skapats med default tiden 15.00
4. Kontrollera att det finns en knapp som heter "Start"
5. Kontrollera att det finns en knapp som heter "Pause" efter att man klickat på "Start"
6. Kontrollera att det finns en knapp som heter "Reset"
"""

def test_has_title(page: Page):
    page.goto("https://lejonmanen.github.io/timer-vue/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Timer app"), timeout=500)

#[ac1:1]
def test_create_widget(page: Page):

    page.goto("https://lejonmanen.github.io/timer-vue/")
#1
    button_locator = page.get_by_role("button")
    timer_button = button_locator.get_by_text( re.compile("Add timer") )
    timer_button.click(timeout=500)
#2
    heading = page.get_by_role("heading").get_by_text( re.compile("Break")) # Hittar alla HTML-element på sidan som har rollen "heading"
    expect(heading).to_be_visible(timeout=500)
#3

#4
    button_locator = page.get_by_role("button") # Hittar alla element på sidan som är av roll "button".
    start_button = button_locator.get_by_text( re.compile("Start") ) # Filtrerar dessa knappar till bara de som innehåller texten "Start".
    expect(start_button).to_have_count(1, timeout=500) # Gör det möjligt att matcha texten med en regex, vilket betyder att den kan vara del av en längre text
    start_button.click() # Klickar på knappen Start
#5
    button_locator = page.get_by_role("button")
    pause_button = button_locator.get_by_text(re.compile("Pause"))
    expect(pause_button).to_have_count(1,timeout=500)
#6
    button_locator = page.get_by_role("button")
    reset_button = button_locator.get_by_text( re.compile("Reset") )
    expect(reset_button).to_have_count(1, timeout=500)
    reset_button.click()

    button_locator = page.get_by_role("button")
    start_button = button_locator.get_by_text(re.compile("Start"))
    expect(start_button).to_have_count(1, timeout=500)

