#  Barrowcroft, Dec 2023

from functools import partial
from typing import Any, Dict, List, Optional

from customtkinter import CTk, CTkButton, CTkFrame  # type: ignore


class CTkButtonGroup(CTkFrame):
    """CTkButtonGroup

    The button group class that will contain a group of buttons
    """

    @property
    def buttons(self) -> List[CTkButton]:
        """buttons

        The 'buttons' property exposes all of the buttons in the group

        Returns:
            List[CTkButton]: list of buttons
        """
        return self._buttons

    def __init__(
        self,
        master: CTk | CTkFrame,
        *args: Any,
        commands: List[Dict[str, str | partial[None]]],
        gutter: Optional[int] = 5,
        arrangement: str = "VERTICAL",
        **kwargs: Any,
    ) -> None:
        """__init__

        Initalises the button group

        Args:
            master (_type_): frame into which this button group is placed
            commands (List[Dict[str, Callable]]): list of callables to be activated by button press
            gutter (Optional[int], optional): gutter between buttons. Defaults to 5
            arrangement (str, optional): arrangment of buttons. Defaults to "VERTICAL"
        """
        #  Initialise the CTkFrame

        super().__init__(master, *args, **kwargs)  # type: ignore

        #  Configure the frame

        self.configure(fg_color="transparent")  # type: ignore
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)

        #  Initialise the list of buttons

        self._buttons: List[CTkButton] = []

        _count = len(commands)

        #  Loop over commands creating buttons

        for _index, command in enumerate(commands):
            self._buttons.append(
                CTkButton(
                    self,
                    text=str(command["text"]),
                    command=command["command"],  # type: ignore
                )
            )

            #  Place the button according to the VERTICAL or HORIZONTAL arrangment

            if arrangement == "VERTICAL":
                _y_padding = (0, gutter) if _index < _count - 1 else (0, 0)
                self._buttons[_index].grid(  # type: ignore
                    row=_index, column=0, padx=0, pady=_y_padding, sticky="we"
                )

            if arrangement.upper() == "HORIZONTAL":
                _x_padding = (0, gutter) if _index < _count - 1 else (0, 0)

                self._buttons[_index].grid(  # type: ignore
                    row=0, column=_index, padx=_x_padding, pady=0, sticky="we"
                )
