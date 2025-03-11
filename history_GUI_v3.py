from tkinter import *
from functools import partial
import all_constants as c
from datetime import date


class Converter:
    """
    Temperature conversion tool (°C to °F of °F to °C)
    """

    def __init__(self):
        """
        Temperature Converter GUI
        """

        self.all_calculations_list = ['10.0°F to is -12°C', '20.0°F to is -7°C',
                                      '30.0°F to is -1°C', '40.0°F to is 4°C',
                                      '50.0°F to is 10°C', '60.0°F to is 16°C']

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_history_button = Button(self.temp_frame,
                                        text="History / Export",
                                        bg="#CC6600", fg="#FFFFFF",
                                        font=("Arial", "14", "bold"),
                                        width=12, command=self.to_history)

        self.to_history_button.grid(row=1, padx=5, pady=5)

    def to_history(self):
        DisplayHistory(self, self.all_calculations_list)


class DisplayHistory:

    def __init__(self, partner, calculations):

        self.history_box = Toplevel()

        # disable help button
        partner.to_history_button.config(state=DISABLED)

        # If users press the cross at the top, closes and 'releases' the help button
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner)
                                  )

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # bg colour and text for calculations area
        if len(calculations) <= c.MAX_CALCULATIONS:
            calc_back = "#D5E8D4"
            calc_amount = "all your"
        else:
            calc_back = "#ffe6cc"
            calc_amount = (f"your recent calculations - "
                           f"showing {c.MAX_CALCULATIONS} / {len(calculations)}")

        # strings for long labels
        recent_intro_text = (f"Below are {calc_amount} calculations "
                             "calculations are shown to the nearest degree")

        # Create string from calculations list (newest calculations first)
        newest_first_string = ""
        newest_first_list = list(reversed(calculations))

        # Last item added in outside the for loop so that spacing is correct
        if len(newest_first_list) <= c.MAX_CALCULATIONS:

            for item in newest_first_list[:-1]:
                newest_first_string += item + "\n"

            newest_first_string += newest_first_list[-1]

        # If there is more than 5 items
        else:
            for item in newest_first_list[:c.MAX_CALCULATIONS - 1]:
                newest_first_string += item + "\n"

            newest_first_string += newest_first_list[c.MAX_CALCULATIONS - 1]

        export_instructions_txt = ("Please push <Export> to save you calculations in "
                                   "file. If filename already exists, it will be")

        # calculations = ""

        # Label list
        history_labels_list = [
            ["History / Export", ("Arial", "16", "bold"), None],
            [recent_intro_text, ("Arial", "11"), None],
            [newest_first_string, ("Arial", "14"), calc_back],
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
            ["Export", "#004C99", lambda: self.export_data(calculations), 0, 0],
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

    def export_data(self, calculations):
        # get current dat for the heading of the filename
        today = date.today()

        # Get dat, month and year as individual strings
        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%y")

        filename = f"temperatures_{year}_{month}_{day}"

        success_string = "Export Successful! The file is called" \
                         f"{filename}.txt"
        self.export_filename_label.config(fg="#12de12", text=success_string,
                                          font=("Arial", "13", "bold"))

        write_to = f"{filename}.txt"

        with open(write_to, "w") as text_file:
            text_file.write("***** Temperature Calculations *****\n")
            text_file.write(f"Generated: {day}/{month}/{year}\n\n")
            text_file.write("Here is your calculation history (oldest to Newest)...\n")

            # write the item to file
            for item in calculations:
                text_file.write(item)
                text_file.write("\n")

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
