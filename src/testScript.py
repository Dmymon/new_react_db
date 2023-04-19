import tkinter as tk

class PathCreatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Path Creator")

        self.class_label = tk.Label(master, text="Class")
        self.class_label.grid(row=0, column=0)

        self.class_version_label = tk.Label(master, text="Version:")
        self.class_version_label.grid(row=1, column=0)
        self.class_version_entry = tk.Entry(master)
        self.class_version_entry.grid(row=1, column=1)

        self.class_name_label = tk.Label(master, text="Name:")
        self.class_name_label.grid(row=2, column=0)
        self.class_name_entry = tk.Entry(master)
        self.class_name_entry.grid(row=2, column=1)

        self.type_label = tk.Label(master, text="Type")
        self.type_label.grid(row=3, column=0)

        self.type_version_label = tk.Label(master, text="Version:")
        self.type_version_label.grid(row=4, column=0)
        self.type_version_entry = tk.Entry(master)
        self.type_version_entry.grid(row=4, column=1)

        self.type_name_label = tk.Label(master, text="Name:")
        self.type_name_label.grid(row=5, column=0)
        self.type_name_entry = tk.Entry(master)
        self.type_name_entry.grid(row=5, column=1)

        self.krembo_label = tk.Label(master, text="Krembo")
        self.krembo_label.grid(row=6, column=0)

        self.krembo_version_label = tk.Label(master, text="Version:")
        self.krembo_version_label.grid(row=7, column=0)
        self.krembo_version_entry = tk.Entry(master)
        self.krembo_version_entry.grid(row=7, column=1)

        self.krembo_name_label = tk.Label(master, text="Name:")
        self.krembo_name_label.grid(row=8, column=0)
        self.krembo_name_entry = tk.Entry(master)
        self.krembo_name_entry.grid(row=8, column=1)

        self.support_label = tk.Label(master, text="Support")
        self.support_label.grid(row=9, column=0)

        self.support_listbox = tk.Listbox(master)
        self.support_listbox.grid(row=10, column=0, columnspan=2)

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_path)
        self.submit_button.grid(row=11, column=1)

    def submit_path(self):
        class_version = self.class_version_entry.get()
        class_name = self.class_name_entry.get()
        type_version = self.type_version_entry.get()
        type_name = self.type_name_entry.get()
        krembo_version = self.krembo_version_entry.get()
        krembo_name = self.krembo_name_entry.get()
        support_selected = self.support_listbox.get(tk.ACTIVE)

        # Do something with the entered values
        print("Submitted path:")
        print("Class version:", class_version)
        print("Class name:", class_name)
        print("Type version:", type_version)
        print("Type name:", type_name)
        print("Krembo version:", krembo_version)
        print("Krembo name:", krembo_name)
        print("Selected support:", support_selected)


root = tk.Tk()
my_gui = PathCreatorGUI(root)
root.mainloop()