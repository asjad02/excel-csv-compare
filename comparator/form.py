from tkinter import *
import pandas as pd
import pd.Dataframe as Df


# Function to set focus (cursor)
def focus1(event):
    # set focus on the course_field box
    csv_path_field.focus_set()


# Function to set focus
def focus2(event):
    # set focus on the sem_field box
    output_path_field.focus_set()

# Function for clearing the
# contents of text entry boxes
def clear():
    # clear the content of text entry box
    excel_path_field.delete(0, END)
    csv_path_field.delete(0, END)
    output_path_field.delete(0, END)

# Function to take data from GUI
# window and compare
def compare():
    def compare_dataframes(excel_pd, csv_pd, output_file_location):
    #     prefer :: https://datatofish.com/compare-values-dataframes/
    # ToDo save the new delta csv in the output file loc

    # ToDo will prefer logger class !!
    if (excel_path_field.get() == "" or
            csv_path_field.get() == "" or
            output_path_field.get() == ""):
        print("Please fill all the column")

    else:
        excel_file = excel_path_field.get()
        csv_file = csv_path_field.get()
        output_file_location = output_path_field.get()
        excel_pd = pd.read_excel(excel_file, index_col=0)
        csv_pd = pd.read_csv(csv_file, index_col=0)

        compare_dataframes(excel_pd, csv_pd, output_file_location)

        excel_path_field.focus_set()

#       maybe no need to clear ?
#         clear()

# Function to take data from GUI
# window and write to an excel file



if __name__ == "__main__":
    # create a GUI window
    root = Tk()

    # set the background colour of GUI window
    root.configure(background='light green')

    # set the title of GUI window
    root.title("Excel Csv Comparator")

    # set the configuration of GUI window
    root.geometry("500x300")

    excel()

    # create a Form label
    heading = Label(root, text="Comparator", bg="light green")

    # create a Name label
    excel_path = Label(root, text="Excel File path", bg="light green")

    # create a Course label
    csv_path = Label(root, text="Csv File Path", bg="light green")

    # create a Semester label
    output_path = Label(root, text="Output Path", bg="light green")

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    heading.grid(row=0, column=1)
    excel_path.grid(row=1, column=0)
    csv_path.grid(row=2, column=0)
    output_path.grid(row=3, column=0)

    # create a text entry box
    # for typing the information
    excel_path_field = Entry(root)
    csv_path_field = Entry(root)
    output_path_field = Entry(root)

    # bind method of widget is used for
    # the binding the function with the events

    # whenever the enter key is pressed
    # then call the focus1 function
    # excel_path_field.bind("<Return>", focus1)

    # whenever the enter key is pressed
    # then call the focus2 function
    csv_path_field.bind("<Return>", focus1)

    # whenever the enter key is pressed
    # then call the focus3 function
    output_path_field.bind("<Return>", focus2)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    excel_path_field.grid(row=1, column=1, ipadx="100")
    csv_path_field.grid(row=2, column=1, ipadx="100")
    output_path_field.grid(row=3, column=1, ipadx="100")

    # create a Submit Button and place into the root window
    submit = Button(root, text="Submit", fg="Black",
                    bg="Red", command=compare())
    submit.grid(row=8, column=1)

    # start the GUI
    root.mainloop()
