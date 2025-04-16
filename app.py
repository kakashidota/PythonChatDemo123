import tkinter as tk
import pymongo

#Connect to MongoDb
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["PythonChat"]
messages_col = db["messages"]


# GUI
root = tk.Tk()
root.title("PythonChat")
root.geometry("300x300")


entry = tk.Entry(root, width=40)
entry.pack(pady=5)

def send_message():
    if entry.get():
        messages_col.insert_one({"text": entry.get()})
        entry.delete(0, tk.END)


send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)


message_label = tk.Label(root, text="Messages:", justify="left")
message_label.pack()

def fetch_messages():
    messages = messages_col.find().sort("_id")
    message_label.config(text="Messages:\n " + "\n".join(f"- {m['text']}" for m in messages))
    root.after(2000, fetch_messages)


fetch_messages()
root.mainloop()






# git status (frivilligt)
# git add .
# git commit -m"Added new code for mongo"
# git push