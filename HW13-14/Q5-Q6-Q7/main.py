
import tkinter as tk
import re

from database import insert_values, fetch_album_names, fetch_song_names

def main() -> None:
    
    valid_entry_pattern = re.compile(r"[\w\d]\s?")
    
    window = tk.Tk()
    window.geometry("500x500")
    window.title("HW13-14-Q5-8")

    frame = tk.Frame(window)
    frame.columnconfigure(0, weight = 1)
    frame.columnconfigure(0, weight = 1)
    frame.columnconfigure(0, weight = 1)
    
    author_var = tk.StringVar()
    song_var = tk.StringVar()
    album_var = tk.StringVar()
    
    query_var = tk.StringVar()
    
    def enter_into_database() -> None:
        
        album_name = album_var.get()
        author_name = author_var.get()
        song_name = song_var.get()
        
        insert_values(album_name,
                      author_name,
                      song_name)
        
        album_entry.delete("0", tk.END)
        author_entry.delete("0", tk.END)
        song_entry.delete("0", tk.END)
        
        
        
    def search() -> None:
        result_textbox.delete("0.0", tk.END)
        
        pattern = re.compile(r"^" + query_var.get() + r".*$", re.IGNORECASE)
        
        songs_lst = [value[0] for value in fetch_song_names()]
        albums_lst = [value[0] for value in fetch_album_names()]
        
        result_textbox.insert("0.0", "Songs: ")
        for song in songs_lst:
            if pattern.findall(song):
                result_textbox.insert(tk.END, f"{song} ")

        result_textbox.insert("0.0", "Albums: ")
        for album in set(albums_lst):
            if pattern.findall(album):
                result_textbox.insert(tk.END, f"{album} ")
        
        
        
    
    STICKY = tk.E + tk.W
    PAD_VALUE = 10
    
    title_label = tk.Label(
                    frame,
                    text = "Albums and Songs Database",
                    font = ("Arial", 20, "bold")
                    )
    title_label.grid(
                    row = 0,
                    column = 1,
                    sticky = STICKY,
                    padx = PAD_VALUE,
                    pady = PAD_VALUE
                    )
    
    #############################################
    
    author_label = tk.Label(
                            frame,
                            text = "Author:",
                            )
    author_label.grid(
                    row = 1,
                    column = 0,
                    sticky = STICKY,
                    padx = PAD_VALUE,
                    pady = PAD_VALUE
                    )
    
    author_entry = tk.Entry(
                            frame,
                            textvariable = author_var
                            )
    author_entry.grid(
                    row = 1,
                    column = 1,
                    sticky = STICKY,
                    padx = PAD_VALUE,
                    pady = PAD_VALUE
                    )
    
    ########################################################
    
    album_label = tk.Label(
                            frame,
                            text = "Album:",
                            )
    album_label.grid(
                    row = 2,
                    column = 0,
                    sticky = STICKY,
                    padx = PAD_VALUE,
                    pady = PAD_VALUE
                    )
    
    album_entry = tk.Entry(
                            frame,
                            textvariable = album_var
                            )
    album_entry.grid(
                    row = 2,
                    column = 1,
                    sticky = STICKY,
                    padx = PAD_VALUE,
                    pady = PAD_VALUE
                    )
    
    #######################################################
    
    song_label = tk.Label(
                            frame,
                            text = "Song:",
                            )
    song_label.grid(
                    row = 3,
                    column = 0,
                    sticky = STICKY,
                    padx = PAD_VALUE,
                    pady = PAD_VALUE
                    )
    
    song_entry = tk.Entry(
                            frame,
                            textvariable = song_var
                            )
    song_entry.grid(
                    row = 3,
                    column = 1,
                    sticky = STICKY,
                    padx = PAD_VALUE,
                    pady = PAD_VALUE
                    )
    
    ############################################################
    
    submit_btn = tk.Button(
                    frame,
                            text = "Submit",
                            command = enter_into_database,
                            state = "disabled"
                            )
    submit_btn.grid(
                    row = 4,
                    column = 1,
                    sticky = STICKY,
                    padx = PAD_VALUE,
                    pady = PAD_VALUE
                    )
    
    ########################################################################
    
    def check_values(*args) -> None:
        
        author_lst = valid_entry_pattern.findall(author_var.get())
        album_lst = valid_entry_pattern.findall(album_var.get())
        song_lst = valid_entry_pattern.findall(song_var.get())
        
        query = query_var.get()
        
        if author_lst and album_lst and song_lst:
            submit_btn.config(state = 'normal')
        else:
            submit_btn.config(state = 'disabled')
            
        if len(query) >= 1:
            search_btn.config(state = "normal")
        else:
            search_btn.config(state = "disabled")
    
    author_var.trace_add("write", check_values)
    album_var.trace_add("write", check_values)
    song_var.trace_add("write", check_values)
    
    #####################################################################################
    
    query_label = tk.Label(
                            frame,
                            text = "Query:"
                            )
    query_label.grid(
                    row = 5,
                    column = 0,
                    sticky = STICKY,
                    padx = PAD_VALUE,
                    pady = PAD_VALUE
                    )
    
    query_entry = tk.Entry(
                            frame,
                            textvariable = query_var
                            )
    query_entry.grid(
                    row = 5,
                    column = 1,
                    sticky = STICKY,
                    padx = PAD_VALUE,
                    pady = PAD_VALUE
                    )
    
    search_btn = tk.Button(
                            frame,
                            text = "Search",
                            command = search,
                            state = "disabled"
                            )
    search_btn.grid(row = 6,
                    column = 1,
                    sticky = STICKY,
                    padx = PAD_VALUE,
                    pady = PAD_VALUE)
    
    result_textbox = tk.Text(
                            frame,
                            width = 20,
                            height = 5
                            )
    result_textbox.grid(
                        row = 7,
                        column = 1,
                        sticky = STICKY,
                        padx = PAD_VALUE,
                        pady = PAD_VALUE
                        )
    
    query_var.trace_add("write", check_values)
    
    frame.pack()

    window.mainloop()

if __name__ == "__main__":
    main()