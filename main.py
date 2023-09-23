import tkinter as tk
import requests

# Create the main window
root = tk.Tk()
root.title("Motivational Quotes")

# Define the API URL
api_url = "https://api.quotable.io/random"


# Function to fetch and display a random quote
def fetch_and_display_quote():
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            quote = data["content"]
            author = data["author"]
            quote_label.config(text=f'"{quote}"\n- {author}')
        else:
            quote_label.config(text="Failed to fetch a quote.")
    except requests.exceptions.RequestException as e:
        quote_label.config(text="Failed to fetch a quote. Error: " + str(e))

    # Schedule the function to run again after 5 seconds (5000 milliseconds)
    root.after(5000, fetch_and_display_quote)


# Create and configure the label
quote_label = tk.Label(root, text="", wraplength=400, font=("Helvetica", 12))
quote_label.pack(pady=20)

# Start fetching and displaying quotes automatically
fetch_and_display_quote()

# Start the main loop
root.mainloop()