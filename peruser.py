import anthropic
import json
import tkinter as tk
from tkinter import filedialog

gui = tk.Tk()
gui.title("Github Peruser")

user_input = tk.Text(gui, height=5, width=50)
user_input.pack(pady=10)

def generate_response():
    user_prompt = user_input.get("1.0", "end-1c")
    file_path = filedialog.askopenfilename(title="Select JSON file", filetypes=[("JSON files", "*.json")])
    with open(file_path, 'r') as file:
        json_txt = file.read()
    additional_rules = "You are an AI assistant to beginners in coding. Try to give short and simple sentences as answers. If the user asks you a doubt regarding something you can send in response the snippet of the code in which file it is located in and the line. Try to be a good helper to the user and improve their efficieny. Your output should be able to help user understand code. You can help the user also write the code."
    system_input = json_txt + "\n" + additional_rules
    client = anthropic.Anthropic(
        api_key="api_key",
    )
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1685,
        temperature=0.1,
        system=system_input,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": user_prompt + "\n"
                    }
                ]
            }
        ]
    )
    response_text = message.content[0].text
    response_output.config(state=tk.NORMAL)
    response_output.delete("1.0", tk.END)
    response_output.insert(tk.END, response_text)
    response_output.config(state=tk.DISABLED)
generate_button = tk.Button(gui, text="Generate Response", command=generate_response)
generate_button.pack(pady=10)
response_output = tk.Text(gui, height=10, width=50, state=tk.DISABLED)
response_output.pack(pady=10)
gui.mainloop()
