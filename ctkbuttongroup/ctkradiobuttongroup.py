#  Barrowcroft, Dec 2023

from typing import Any, Callable, Dict, List, Optional

from customtkinter import CTk, CTkFrame, CTkRadioButton, StringVar  # type: ignore


class CTkRadioButtonGroup(CTkFrame):
    """CTkRadioButtonGroup

    The radio button group class that will contain a group of radio buttons
    """

    def get(self) -> str:
        return self._radioButtonVar.get()

    def set(self, index: int):
        self._radioButtonVar[index].select()  # type: ignore

    @property
    def radioButtons(self) -> List[CTkRadioButton]:
        """radioButtons

        The 'radioButtons' property exposes all of the radio buttons in the group

        Returns:
            List[CTkRadioButton]: list of radio buttons
        """
        return self._radioButtons

    def __init__(
        self,
        master: CTk | CTkFrame,
        *args: Any,
        options: List[Dict[str, str]],
        command: Callable[[], None],
        gutter: Optional[int] = 5,
        arrangement: str = "VERTICAL",
        **kwargs: Any
    ) -> None:
        """__init__

        Initalises the check box group

        Args:
            master (_type_): frame into which this radio button group is placed
            options (List[Dict[str, str]]): list of options to display as radio buttons
            command (List[Dict[str, Callable]]): command activated by selecting radio button
            gutter (Optional[int], optional): gutter between radio buttons. Defaults to 5
            arrangement (str, optional): arrangment of radio buttons. Defaults to "VERTICAL"
        """
        #  Initialise the CTkFrame
        super().__init__(master, *args, **kwargs)  # type: ignore

        #  Configure the frame
        self.configure(fg_color="transparent")  # type: ignore
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)

        #  Initialise the list of radio buttons and associated variables

        self._radioButtonVar: StringVar = StringVar()
        self._radioButtons: List[CTkRadioButton] = []

        _count = len(options)

        #  Loop over options creating radio buttons

        for _index, option in enumerate(options):
            self.grid_columnconfigure(index=_index, weight=1)
            self._radioButtons.append(
                CTkRadioButton(
                    self,
                    text=option["text"],
                    value=option["value"],
                    variable=self._radioButtonVar,
                    command=command,
                )
            )

            #  Place the radio button according to the VERTICAL or HORIZONTAL arrangement

            if arrangement.upper() == "VERTICAL":
                _y_padding = (0, gutter) if _index < _count - 1 else (0, 0)

                self._radioButtons[_index].grid(  # type: ignore
                    row=_index, column=0, padx=0, pady=_y_padding, sticky="we"
                )
            if arrangement.upper() == "HORIZONTAL":
                _x_padding = (0, gutter) if _index < _count - 1 else (0, 0)

                self._radioButtons[_index].grid(  # type: ignore
                    row=0, column=_index, padx=_x_padding, pady=0, sticky="we"
                )
