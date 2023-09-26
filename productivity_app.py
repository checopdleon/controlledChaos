import tkinter as tk
from tkinter import ttk

class MainApp:
    def __init__(self, root):
        # Main window configurations
        root.title("Advanced Reminder App")
        root.geometry("800x600")

        # Create the main frame
        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create the left sidebar for project title cards
        self.sidebar = ttk.Frame(main_frame, width=150)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        # Create a scrollable canvas for the sidebar
        sidebar_canvas = tk.Canvas(self.sidebar)
        scrollbar = ttk.Scrollbar(self.sidebar, orient="vertical", command=sidebar_canvas.yview)
        scrollable_frame = ttk.Frame(sidebar_canvas)
        
        scrollable_frame.bind("<Configure>", lambda e: sidebar_canvas.configure(scrollregion=sidebar_canvas.bbox("all")))
        sidebar_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        sidebar_canvas.configure(yscrollcommand=scrollbar.set)
        
        sidebar_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Sample project titles for the sidebar
        for i in range(50):  # Just adding a lot to show the scrolling feature
            project_label = ttk.Label(scrollable_frame, text=f"Project {i+1}")
            project_label.pack(pady=5)

        # Create the tabs
        self.tabs = ttk.Notebook(main_frame)
        self.tabs.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.reminders_tab = ttk.Frame(self.tabs)
        self.calendar_events_tab = ttk.Frame(self.tabs)
        self.notes_tab = ttk.Frame(self.tabs)

        self.tabs.add(self.reminders_tab, text="Reminders")
        self.tabs.add(self.calendar_events_tab, text="Calendar Events")
        self.tabs.add(self.notes_tab, text="Notes")

# Initialize the main application
root = tk.Tk()
app = MainApp(root)
root.mainloop()