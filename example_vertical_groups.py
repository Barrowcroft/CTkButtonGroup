#  Barrowcroft, Dec 2023

from functools import partial
from typing import Dict, List

from customtkinter import CTk  # type: ignore

from ctkbuttongroup import (
    CTkButtonGroup,
    CTkCheckBoxGroup,
    CTkRadioButtonGroup,
    CTkSwitchGroup,
)

# Create button handler


def handleButton(index: int) -> None:
    print(f"Pressed button {index}\n")


# Create checkbox handler


def handleCheckBox() -> None:
    for index in range(0, 5):
        print(f"CheckBox = {index} value = {_checkBoxes.get(index)}")
    print()


# Create radiobutton handler


def handleRadioButton() -> None:
    print(f"RadioButton Value = {_radioButtons.get()}")
    print()


# Create switch handler


def handleSwitch() -> None:
    for index in range(0, 5):
        print(f"Switch = {index} value = {_switches.get(index)}")
    print()


# Create and configure the root window with grid layout(rows and columns).

_root = CTk()
_root.geometry("600x200")


# Create button definitions

_commands: List[Dict[str, str | partial[None]]] = [
    {"text": "Buton One", "command": partial(handleButton, 1)},
    {"text": "Buton Two", "command": partial(handleButton, 2)},
    {"text": "Buton Three", "command": partial(handleButton, 3)},
    {"text": "Buton Four", "command": partial(handleButton, 4)},
    {"text": "Buton Five", "command": partial(handleButton, 5)},
]

# Create button group

_buttons: CTkButtonGroup = CTkButtonGroup(
    _root, commands=_commands, gutter=5, arrangement="VERTICAL"
)
_buttons.grid(row=0, column=0, padx=10, pady=10, sticky="nwe")  # type: ignore

# Create check box definitions

_options: List[Dict[str, str]] = [
    {"text": "CheckBox One", "on-value": "checked", "off-value": "unchecked"},
    {"text": "CheckBox Two", "on-value": "checked", "off-value": "unchecked"},
    {"text": "CheckBox Three", "on-value": "checked", "off-value": "unchecked"},
    {"text": "CheckBox Four", "on-value": "checked", "off-value": "unchecked"},
    {"text": "CheckBox Five", "on-value": "checked", "off-value": "unchecked"},
]

# Create check box group

_checkBoxes: CTkCheckBoxGroup = CTkCheckBoxGroup(
    _root, options=_options, command=handleCheckBox, gutter=10
)
_checkBoxes.grid(row=0, column=1, padx=10, pady=10, sticky="nwe")  # type: ignore

# Create radio button definitions

_options: List[Dict[str, str]] = [
    {"text": "RadioButton One", "value": "One"},
    {"text": "RadioButton Two", "value": "Two"},
    {"text": "RadioButton Three", "value": "Three"},
    {"text": "RadioButton Four", "value": "Four"},
    {"text": "RadioButton Five", "value": "Five"},
]


# Create radio button group

_radioButtons: CTkRadioButtonGroup = CTkRadioButtonGroup(
    _root,
    options=_options,
    command=handleRadioButton,
    gutter=10,
    arrangement="VERTICAL",
)
_radioButtons.grid(row=0, column=2, padx=10, pady=10, sticky="nwe")  # type: ignore

# Create switch definitions

_options: List[Dict[str, str]] = [
    {"text": "Switch One", "on-value": "on", "off-value": "off"},
    {"text": "Switch Two", "on-value": "on", "off-value": "off"},
    {"text": "Switch Three", "on-value": "on", "off-value": "off"},
    {"text": "Switch Four", "on-value": "on", "off-value": "off"},
    {"text": "Switch Five", "on-value": "on", "off-value": "off"},
]


# Create switch group

_switches: CTkSwitchGroup = CTkSwitchGroup(
    _root, options=_options, command=handleSwitch, gutter=5, arrangement="VERTICAL"
)
_switches.grid(row=0, column=3, padx=10, pady=10, sticky="nwe")  # type: ignore

# Continue the input loop

_root.mainloop()  # type: ignore
