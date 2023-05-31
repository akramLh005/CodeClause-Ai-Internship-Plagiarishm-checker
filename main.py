
from tkinter import messagebox
import re
import math
import customtkinter

def calculate_cosine_similarity():
    unique_words = []
    match_percentage = 0

    user_input = query_textbox.get("1.0", "end-1c")
    lowercase_query = user_input.lower()

    word_list = re.sub("[^\w]", " ", lowercase_query).split()

    for word in word_list:
        if word not in unique_words:
            unique_words.append(word)


    with open("database_file.txt", "r") as file:
        database_file = file.read().lower()

    word_list_DB = re.sub("[^\w]", " ", database_file).split()

    for word in word_list_DB:
        if word not in unique_words:
            unique_words.append(word)

    query_tf = []
    database_tf = []

    for word in unique_words:
        query_tf_counter = 0
        database_tf_counter = 0

        for word2 in word_list:
            if word == word2:
                query_tf_counter += 1
        query_tf.append(query_tf_counter)

        for word2 in word_list_DB:
            if word == word2:
                database_tf_counter += 1
        database_tf.append(database_tf_counter)

    product = 0
    for i in range(len(query_tf)):
        product += query_tf[i] * database_tf[i]

    query_vector_magnitude = 0
    for i in range(len(query_tf)):
        query_vector_magnitude += query_tf[i] ** 2
    query_vector_magnitude = math.sqrt(query_vector_magnitude)

    DB_Vector = 0
    for i in range(len(database_tf)):
        DB_Vector += database_tf[i] ** 2
    DB_Vector = math.sqrt(DB_Vector)

    match_percentage = (float)(product / (query_vector_magnitude * DB_Vector)) * 100

    output = "Input text matches %0.02f%% with our database." % match_percentage
    messagebox.showinfo("Plagiarism checker Developed by Akram Lahmar ", output)


# Interface Custom Tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("800x500")
app.title("Plagiarism checker Developed by Akram Lahmar")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=100, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame_1, text="Enter your Text:")
label.pack(pady=10, padx=10)

query_textbox = customtkinter.CTkTextbox(master=frame_1, width=700, height=300)
query_textbox.pack(pady=10, padx=10)

calculate_button = customtkinter.CTkButton(master=frame_1, text="Check plagiarism", command=calculate_cosine_similarity)
calculate_button.pack(pady=10, padx=10)

app.mainloop()