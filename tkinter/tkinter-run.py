import tkinter as tk
from tkinter import ttk, messagebox
import requests
import time


# Function to update the status bar message
def update_status(message):
    status_label.config(text=message)
    root.update_idletasks()  # Forces a UI update


# Function to load movies from the API and populate the listbox
def load_movies():
    update_status("Loading movies...")
    try:
        time.sleep(1)  # Simulating a longer operation
        response = requests.get("http://localhost:5000/api/movies")
        response.raise_for_status()
        movies = response.json()

        # Clear the listbox
        movie_listbox.delete(0, tk.END)

        # Populate the listbox with movie titles
        for movie in movies:
            movie_listbox.insert(tk.END, movie["title"])
            movie_dict[movie["title"]] = movie["movie_id"]

        update_status("Ready")
    except Exception as e:
        update_status("Error loading movies")
        messagebox.showerror("Error", f"Error fetching movies: {e}")


# Function to fetch ratings for the selected movie
def get_movie_ratings(event):
    update_status("Fetching ratings...")
    try:
        # Get the currently selected movie title from the listbox
        selected_movie_index = movie_listbox.curselection()
        if not selected_movie_index:
            update_status("Ready")
            return

        selected_movie = movie_listbox.get(selected_movie_index)

        movie_id = movie_dict.get(selected_movie)
        response = requests.get(f"http://localhost:5000/api/movies/{movie_id}/ratings")
        response.raise_for_status()

        # Get the ratings array from the response
        movie = response.json()
        ratings = movie.get("ratings", [])

        # Clear previous ratings from the treeview
        for row in ratings_tree.get_children():
            ratings_tree.delete(row)

        # Populate the treeview with ratings
        if not ratings:
            ratings_tree.insert("", tk.END, values=("No ratings found", ""))
        else:
            for rating in ratings:
                rating_value = rating.get("rating", "N/A")
                review = rating.get("review", "No review")
                ratings_tree.insert("", tk.END, values=(rating_value, review))

        update_status("Ready")

    except Exception as e:
        update_status("Error fetching ratings")
        messagebox.showerror("Error", f"Error fetching ratings: {e}")


# Tkinter GUI setup
root = tk.Tk()
root.title("Movies and Ratings")
root.geometry("600x500")

movie_dict = {}  # Dictionary to hold movie title to movie_id mapping

# Main frame for content
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Movie list frame (left side)
movie_frame = tk.Frame(main_frame)
movie_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)

movie_label = tk.Label(movie_frame, text="Movies List")
movie_label.pack()

movie_listbox = tk.Listbox(movie_frame, height=20, width=30)
movie_listbox.pack()

load_button = tk.Button(movie_frame, text="Load Movies", command=load_movies)
load_button.pack(pady=5)

# Ratings table frame (right side)
ratings_frame = tk.Frame(main_frame)
ratings_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

ratings_label = tk.Label(ratings_frame, text="Movie Ratings")
ratings_label.pack()

# Treeview for displaying ratings
ratings_tree = ttk.Treeview(
    ratings_frame, columns=("Rating", "Review"), show="headings", height=20
)
ratings_tree.heading("Rating", text="Rating")
ratings_tree.heading("Review", text="Review")
ratings_tree.pack(fill=tk.BOTH, expand=True)

# Status bar (bottom of the window)
status_label = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_label.pack(side=tk.BOTTOM, fill=tk.X,ipady=10)  # Make the label span the full width and a little extra height

# Bind the Listbox selection event to get_movie_ratings function
movie_listbox.bind("<<ListboxSelect>>", get_movie_ratings)

# Start the Tkinter event loop
root.mainloop()
