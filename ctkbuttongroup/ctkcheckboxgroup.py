#  Barrowcroft, Dec 2023

from typing import Any, Callable, Dict, List, Optional

from customtkinter import CTk, CTkCheckBox, CTkFrame, StringVar  # type: ignore


class CTkCheckBoxGroup(CTkFrame):
    """CTkCheckBoxGroup

    The check box group class that will contain a group of check boxes
    """

    def set(self, index: int, state: bool) -> None:
        if state:
            self._checkBoxes[index].select()
        else:
            self._checkBoxes[index].deselect()

    def get(self, index: int) -> int | str:
        return self._checkBoxes[index].get()

    @property
    def checkBoxes(self) -> List[CTkCheckBox]:
        """checkBoxes

        The 'checkBoxes' property exposes all of the check boxes in the group

        Returns:
            List[CTkCheckBox]: list of check boxes
        """
        return self._checkBoxes

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
            master (_type_): frame into which this check box group is placed
            options (List[Dict[str, str]]): list of options to display as check boxes
            command (List[Dict[str, Callable]]): command activated by selecting check box
            gutter (Optional[int], optional): gutter between check boxes. Defaults to 5
            arrangement (str, optional): arrangment of check boxes. Defaults to "VERTICAL"
        """
        #  Initialise the CTkFrame

        super().__init__(master, *args, **kwargs)  # type: ignore

        #  Configure the frame

        self.configure(fg_color="transparent")  # type: ignore

        #  Initialise the list of check boxes and associated variables

        self._checkBoxVars: List[StringVar] = []
        self._checkBoxes: List[CTkCheckBox] = []

        _count = len(options)

        #  Loop over options creating check boxes

        for _index, option in enumerate(options):
            self._checkBoxVars.append(StringVar())
            self._checkBoxes.append(
                CTkCheckBox(
                    self,
                    text=option["text"],
                    onvalue=option["on-value"],
                    offvalue=option["off-value"],
                    variable=self._checkBoxVars[_index],
                    command=command,
                )
            )

            #  Place the check box according to the VERTICAL or HORIZONTAL arrangement

            if arrangement.upper() == "VERTICAL":
                _y_padding = (0, gutter) if _index < _count - 1 else (0, 0)

                self._checkBoxes[_index].grid(  # type: ignore
                    row=_index, column=0, padx=0, pady=_y_padding, sticky="we"
                )

            if arrangement.upper() == "HORIZONTAL":
                _x_padding = (0, gutter) if _index < _count - 1 else (0, 0)

                self._checkBoxes[_index].grid(  # type: ignore
                    row=0, column=_index, padx=_x_padding, pady=0, sticky="we"
                )
