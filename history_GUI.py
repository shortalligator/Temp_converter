from tkinter import *
from functools import partial


class Converter:
    """
    Temperature conversion tool (°C to °F of °F to °C)
    """

    def __init__(self):
        """
        Temperature Converter GUI
        """

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_history_button = Button(self.temp_frame,
                                        text="History / Export",
                                        bg="#CC6600", fg="#FFFFFF",
                                        font=("Arial", "14", "bold"),
                                        width=12, command=self.to_history)

        self.to_history_button.grid(row=1, padx=5, pady=5)

    def to_history(self):
        DisplayHistory(self)


class DisplayHistory:

    def __init__(self, partner):
        # set up dialogue box and background colour

        green_back = "#D5E8D4"
        peach_back = "#ffe6cc"

        self.history_box = Toplevel()

        # disable help button
        partner.to_history_button.config(state=DISABLED)

        # If users press the cross at the top, closes and 'releases' the help button
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner)
                                  )

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # strings for long labels
        recent_intro_text = ("Below are you recent calculations - showing "
                             "3 / 3 calculations. All calculations are shown "
                             "to the nearest degree")

        export_instructions_txt = ("Please push <Export> to save you calculations in "
                                   "file. If filename already exists, it will be")

        calculations = ""

        # Label list
        history_labels_list = [
            ["History / Export", ("Arial", "16", "bold"), None],
            [recent_intro_text, ("Arial", "11"), None],
            ["calculations_list", ("Arial", "14"), green_back],
            [export_instructions_txt, ("Arial", "11"), None]
        ]

        history_label_ref = []
        for count, item in enumerate(history_labels_list):
            make_label = Label(self.history_box, text=item[0], font=item[1],
                               bg=item[2], wraplength=300, justify="left",
                               pady=10, padx=20)
            make_label.grid(row=count)

            history_label_ref.append(make_label)

        # Retrieve export instruction label so that we can
        # configure it to show the filename if the user exports the file
        self.export_filename_label = history_label_ref[3]

        # make frame to hold buttons (2 columns)
        self.history_button_frame = Frame(self.history_box)
        self.history_button_frame.grid(row=4)

        # button list (button text | bg colour | command | column
        button_details_list = [
            ["Export", "#004C99", "", 0, 0],
            ["Close", "#666666", partial(self.close_history, partner), 0, 1],
        ]

        for btn in button_details_list:
            self.make_button = Button(self.history_button_frame,
                                      font=("Arial", "12", "bold"),
                                      text=btn[0], bg=btn[1],
                                      fg="#FFFFFF", width=12,
                                      command=btn[2]
                                      )
            self.make_button.grid(row=btn[3], column=btn[4], padx=10, pady=10)

    def close_history(self, partner):
        """
        Closes help dialogue box and enables help button
        """
        # Put help button back to normal
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
