import tkinter as tk
from tkinter import messagebox as mb
import pickle


#==============================HEX_VARIABLES===============================        
def Hex(hex_num):
    # [0]-BLACK, [1]-GRAY, [2]-BROWN, [3]-BLUE, [4]-WHITE, [5]-LT/GRAY, [6]-GREEN
    Hex = ['#000000', '#2c2c2c', '#532E21', '#1c5366', '#ffffff', '#808080', '#00ff00']
    return Hex[hex_num]

#=============================================================#
#=======================___SYSTEM___==========================#
#=============================================================#

class window(tk.Tk):
    def __init__(self, title):
        super().__init__()

        # VARIABLES
        self.__screen_width = self.winfo_screenwidth()
        self.__screen_height = self.winfo_screenheight()
        self.__mainfont = ("System", 20)

        # ==========WINDOW_FRAME==========
        self.title(title)
        self.main_frame = tk.Frame(self, bg=Hex(1)) 
        self.main_frame.pack(fill="both", expand=True)





    def custom_title_bar(self, title):
        self.main_frame.destroy() 
        self.is_maximized = False
        self.normal_geometry = "800x500+100+100"  # default size
        self.geometry(self.normal_geometry)
        self.bind("<Map>", self.restore_window)
    

        #=====================__EVENT_HANDLERS__====================#


        # Create custom title bar
        title_bar = tk.Frame(self, bg=Hex(0), relief="raised", bd=0)
        title_bar.pack(fill="x")

        # Title text
        title_label = tk.Label(title_bar, text=title, bg=Hex(0), fg="blue", font = ("System", 12))
        title_label.pack(side="left", padx=10)

        # Maximize/Restore button
        def toggle_maximize():
            if not self.is_maximized:
                # Save current size before maximizing
                self.normal_geometry = self.geometry()

                # Maximize to screen
                self.geometry(f"{self.__screen_width}x{self.__screen_height}+0+0")

                self.is_maximized = True
            else:
                # Restore previous size
                self.geometry(self.normal_geometry)
                self.is_maximized = False

        # Minimize button
        def minimize():
            self.update_idletasks()
            self.overrideredirect(False)   # temporarily restore window manager
            self.iconify()

        # Make window draggable
        def start_move(event):
            if self.is_maximized:
                toggle_maximize()  # restore first
            self.x = event.x
            self.y = event.y

        def move_window(event):
            if not self.is_maximized:  # only allow dragging when not maximized
                x = event.x_root - self.x
                y = event.y_root - self.y
                self.geometry(f"+{x}+{y}")

        title_bar.bind("<Button-1>", start_move)
        title_bar.bind("<B1-Motion>", move_window)

        close_btn = tk.Button(title_bar, text="X", bg = Hex(0), fg = "red", command=self.destroy, bd=0, font = ("System", 12) )
        close_btn.pack(side="right")  

        max_btn = tk.Button(title_bar, text="□", bg = Hex(0), fg = Hex(4), command=toggle_maximize, bd=0, font = ("System", 12))
        max_btn.pack(side="right")   

        min_btn = tk.Button(title_bar, text="_", bg = Hex(0), fg = Hex(4), command=minimize, bd=0, font = ("System", 12))
        min_btn.pack(side="right")





        #=============__MAIN_FRAME__=============

        self.main_frame = tk.Frame(self, bg=Hex(1))
        self.main_frame.pack(fill="both", expand=True)









    #_____RESTORE_WINDOW_____#
    def restore_window(self, event=None):
        if self.state() == "normal":
            self.overrideredirect(True)


    # _____WINDOW_CANVAS_____#
    def canvas(self):       
        canvas = tk.Canvas(
            self.main_frame,
            width = self.__screen_height*0.9,
            height = self.__screen_height*0.9,
            bg = Hex(2),
            highlightthickness = 5
        )
        canvas.grid(row = 0, column = 0, padx = (15, 0), pady = 20)

    # _____WINDOW_PANEL_____#
    def panel(self):    
        self.panel = tk.Frame(self.main_frame, bg=Hex(1))
        self.panel.grid(row=0, column=1, sticky= 'ns', padx=(0, 10), pady=10)
        panel_label = tk.Label(
            self.panel,
            text = "Game Settings-",
            bg = Hex(1),
            fg = Hex(4),
            font = ("Times New Roman", int(self.__screen_height/20))
        )
        panel_label.pack(padx=10, pady=10)
        return self.panel


#============================================================================#
# ===============================SETTINGS_MENU===============================#
#============================================================================#

class settings:

    #=========================___SS_MENU___==========================#
    @staticmethod
    def SS_menu(destination, options, function, main_font=("System", 20), prefix=None, stripper = None):
        if not options:
            raise ValueError("options list cannot be empty")


        row = tk.Frame(destination, bg=Hex(1))
        row.pack(padx=10, pady=(0, 8), fill="x")

        tk.Label(
            row,
            text=prefix,
            bg=Hex(1),
            fg=Hex(5),
            font=main_font
        ).pack(side="left")

        # Keep original order
        available_options = options.copy()
        

        menu_var = tk.StringVar()
        current_selection = available_options[0]
        menu_var.set(current_selection)

        def rebuild_menu():
            menu["menu"].delete(0, "end")

            for option in options:
                if option != current_selection:  # exclude selected item
                    menu["menu"].add_command(
                        label=option.split(stripper)[0] if stripper else option,
                        command=lambda value=option: update_menu(value)
                    )
        # Update menu function
        def update_menu(new_selection):
            nonlocal current_selection
            menu_var.set(new_selection) 
            current_selection = new_selection

            rebuild_menu()
            function(new_selection) 

            # Remove new selection
            if new_selection in available_options:
                available_options.remove(new_selection)

            # Put old selection back in correct position
            if old_selection not in available_options:
                index = options.index(old_selection)
                available_options.insert(index, old_selection)
            old_selection = current_selection

            # Rebuild menu
            menu["menu"].delete(0, "end")
            for option in available_options:
                menu["menu"].add_command(
                    label=option,
                    command=lambda value=option: update_menu(value)
                )    

            # Call user function
            function(new_selection)

        menu = tk.OptionMenu(
            row,
            menu_var,
            current_selection,
            *[(opt.split(stripper)[0] if stripper else opt) for opt in available_options[1:]],
            command=update_menu
        )

        menu.config(font=('System', 12), bg=Hex(0), fg=Hex(4))
        menu.pack(side="left", padx=(6, 0), fill="x", expand=True)
     


    #=========================___SS_TEXT_BkOX___==========================#
    @staticmethod
    def SS_text_box(destination, data_loc, main_font=("System", 20), prefix=None):
        row = tk.Frame(destination, bg=Hex(1))
        row.pack(padx=10, pady=(0, 8), fill="x")

        tk.Label(
            row,
            text=prefix,
            bg=Hex(1),
            fg=Hex(5),
            font=main_font
        ).pack(side="left")

        text_box_var = tk.StringVar()

        entry = tk.Entry(
            row,
            bg=Hex(0),
            fg=Hex(4),
            textvariable=text_box_var,
            font=main_font
        )

        def save_entry(event=None):
            global player_data, current_player
            try:
                with open(f'{data_loc}.pkl', 'rb') as f:
                    player_data = pickle.load(f)
            except Exception as e:           
                print("Failed to load player data:", e)

            name = text_box_var.get().strip()
            if name:
                player_data[name] = 0
                current_player = name
                print(player_data)
                try:
                    with open(f'{data_loc}.pkl', 'wb') as f:
                        pickle.dump(player_data, f)
                except Exception as e:
                    print("Failed to save player data:", e)

            text_box_var.set("")

        entry.pack(side="left", padx=(6, 0), fill="x", expand=True)
        entry.bind("<Return>", save_entry)
        entry.bind("<Return>", entry.delete(0, tk.END))


def main():
    Window = window("Mr.p is a doofus")
    Window.custom_title_bar("Tkinter_App-(rock_paper_scissors)")
    Window.canvas()
    panel = Window.panel()
    deck_size = tk.IntVar()
    def set_deck_size(selection):
        number = int(selection.replace(" cards", ""))
        deck_size.set(number)
        print(deck_size.get())
    settings.SS_menu(   
        panel,
        ['12 cards', '18 cards', '30 cards', '42 cards', '60 cards'],
        set_deck_size,
        prefix="Deck Size:",
        stripper = " cards"
    )
    settings.SS_text_box(panel, "player_data", prefix="Player Name:")
    Window.mainloop()

if __name__ == "__main__":
    print("This isnt meant to be run as a main, but oh well here ya go")
    main()
