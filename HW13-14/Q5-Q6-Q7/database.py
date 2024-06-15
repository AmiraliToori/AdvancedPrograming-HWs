
import sqlite3

import tkinter as tk

connect = sqlite3.connect("music.db")

c = connect.cursor()


with connect:
    c.execute('''PRAGMA foreign_keys = ON''')


def create_musics_table() -> None:
    with connect:
        c.execute('''CREATE TABLE IF NOT EXISTS Musics(
                    album_name TEXT,
                    author_name TEXT,
                    song_name TEXT)''')

def insert_values(album_name: str,
                  author_name: str,
                  song_name: str) -> None:
    try:
        with connect:
            c.execute('''INSERT INTO Musics VALUES(
                :album_name,
                :author_name,
                :song_name) ''',
                {"album_name": album_name,
                "author_name": author_name,
                "song_name": song_name})
            
    except:
        error_window = tk.Tk()
        error_window.geometry("100x100")
        error_window.title("Error")
        
        tk.Label(
                error_window,
                text = "Something went wrong, please try again.",
                padx = 10,
                pady = 10
                ).pack()
        
        tk.Button(
                error_window,
                text = "OK",
                command = error_window.destroy()
                ).pack()
        error_window.mainloop()


def fetch_album_names() -> list:
    with connect:
        c.execute('''SELECT (album_name) FROM Musics''')
    
    return c.fetchall()


def fetch_song_names() -> list:
    with connect:
        c.execute('''SELECT (song_name) FROM Musics''')
    
    return c.fetchall()


create_musics_table()

