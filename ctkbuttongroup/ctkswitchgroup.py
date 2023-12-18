#  Barrowcroft, Dec 2023

from typing import Any, Callable, Dict, List, Optional

from customtkinter import CTk, CTkFrame, CTkSwitch, StringVar  # type: ignore


class CTkSwitchGroup(CTkFrame):
    """CTkSwitchGroup

    The switch group class that will contain a group of switches
    """

    def set(self, index: int):
        self._switches[index].select()

    def get(self, index: int) -> int | str:
        return self._switches[index].get()

    @property
    def switches(self) -> List[CTkSwitch]:
        """switches

        The 'switches' property exposes all of the switches in the group

        Returns:
            List[CTkSwitch]: list of switches
        """
        return self._switches

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
            master (_type_): frame into which this switch group is placed
            options (List[Dict[str, str]]): list of options to display as switches
            command (List[Dict[str, Callable]]): command activated by selecting switch
            gutter (Optional[int], optional): gutter between switches. Defaults to 5
            arrangement (str, optional): arrangment of switches. Defaults to "VERTICAL"
        """
        #  Initialise the CTkFrame

        super().__init__(master, *args, **kwargs)  # type: ignore

        #  Configure the frame

        self.configure(fg_color="transparent")  # type: ignore

        #  Initialise the list of switches and associated variables

        self._switchVars: List[StringVar] = []
        self._switches: List[CTkSwitch] = []

        _count = len(options)

        #  Loop over options creating switches

        for _index, option in enumerate(options):
            self._switchVars.append(StringVar())
            self._switches.append(
                CTkSwitch(
                    self,
                    text=option["text"],
                    onvalue=option["on-value"],
                    offvalue=option["off-value"],
                    variable=self._switchVars[_index],
                    command=command,
                )
            )

            #  Place the switch button according to the VERTICAL or HORIZONTAL arrangement

            if arrangement.upper() == "VERTICAL":
                _y_padding = (0, gutter) if _index < _count - 1 else (0, 0)

                self._switches[_index].grid(  # type: ignore
                    row=_index, column=0, padx=0, pady=_y_padding, sticky="we"
                )

            if arrangement.upper() == "HORIZONTAL":
                _x_padding = (0, gutter) if _index < _count - 1 else (0, 0)

                self._switches[_index].grid(  # type: ignore
                    row=0, column=_index, padx=_x_padding, pady=0, sticky="we"
                )
