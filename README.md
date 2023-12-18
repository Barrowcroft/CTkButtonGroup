# CTkButtonGroup (CTkCheckBoxGroup, CTkRadioButtonGroup, CTkSwitchGroup)

Four simple classes to facilitate the creation of groups of buttons, check boxes, radio buttons and switches.

Install using: pip install git+https://github.com/Barrowcroft/CTkButtonGroup.git

NOTE: CustomTkinter seems to cause problems with strict type checking - I have had to make liberal use of "# type: ignore".

### CTkButtonGroup

The button group is created with a list of dictionaries which contain a string 'text' and a callable 'command'. The 'text'' is used for the button caption and the 'command'' for the button command. The button can be aranged vertically or horizontally. For exampe:

```
# Create button definitions

_commands: List[Dict[str, Callable]] = [
    {"text": "Buton One", "command": partial(handleButton, 1)},
    {"text": "Buton Two", "command": partial(handleButton, 2)},
    {"text": "Buton Three", "command": partial(handleButton, 3)},
    {"text": "Buton Four", "command": partial(handleButton, 4)},
    {"text": "Buton Five", "command": partial(handleButton, 5)},
]

# Create button group

_buttons: CTkButtonGroup = CTkButtonGroup(
    _root, 
    commands=_commands, 
    gutter=5, 
    arrangement="VERTICAL"
)
_buttons.grid(row=0, column=0, padx=10, pady=10, sticky="nwe")
```

### CTkCheckBoxGroup

The check box group is created with a list of dictionaries which contain three strings, 'text', 'on-value' and 'off-value', and a 'command' which is executed when a check box is clicked. For example:

```
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
_checkBoxes.grid(row=0, column=1, padx=10, pady=10, sticky="nwe")
```

To retrieve the value of a check box use the 'get' method with the index of the check box. For example:

```
def handleCheckBox() -> None:
    for index in range(0, 5):
        print(f"CheckBox = {index} value = {_checkBoxes.get(index)}")
```

### CTkRadioButtonGroup

The radio button group is created with a list of dictionaries which contain two strings, 'text' and 'value', and a'command' which is executed when a radio button is clicked. For example:

```
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
_radioButtons.grid(row=0, column=2, padx=10, pady=10, sticky="nwe")
```

To retrieve the value of a radio button group use the 'get' method. For example:

```
def handleRadioButton() -> None:
    print(f"RadioButton Value = {_radioButtons.get()}")
```

### CTkSwitchGroup

The switch group is created with a list of dictionaries which contain three strings, 'text', 'on-value' and 'off-value', and a 'command' which is executed when a switch is changed. For example:

```
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
_switches.grid(row=0, column=3, padx=10, pady=10, sticky="nwe")
```

To retrieve the value of a switch use the 'get' method with the index of the check box. For example:

```
def handleSwitch() -> None:
    for index in range(0, 5):
        print(f"Switch = {index} value = {_switches.get(index)}")
```
