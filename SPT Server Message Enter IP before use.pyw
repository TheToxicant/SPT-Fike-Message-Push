import tkinter as tk
import requests

def send_notification():
    # Get the notification text from the text box
    notification_text = notification_textbox.get("1.0", "end-1c")
    
    url = "http://Your IP Here:6969/fika/notification/push"
    headers = {
        "requestcompressed": "0"
    }
    payload = {
        "notification": notification_text,
        "notificationIcon": 0
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            result_label.config(text="Notification sent successfully!", fg="green")
        else:
            result_label.config(text=f"Failed to send notification. Status code: {response.status_code}", fg="red")
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"An error occurred: {e}", fg="red")

# Set up the main application window
app = tk.Tk()
app.title("Fika Notification Sender")

# Create a label and text box for the notification text
label = tk.Label(app, text="Enter your notification message:")
label.pack(pady=10)

notification_textbox = tk.Text(app, height=5, width=50)
notification_textbox.pack(pady=10)
notification_textbox.insert("1.0", "Hello from the Fika notification manager!")  # Default message

# Create a button to send the notification
send_button = tk.Button(app, text="Send Notification", command=send_notification)
send_button.pack(pady=10)

# Create a label to display the result (success or error)
result_label = tk.Label(app, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()
