{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "dde62180",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv\n",
    "from tkinter import Tk, Frame, Label, Entry, Button, messagebox, font\n",
    "from datetime import datetime\n",
    "\n",
    "class BubblesApp(Tk):\n",
    "    def __init__(self):\n",
    "        super().__init__()\n",
    "\n",
    "        self.title(\"BUBBLES\")\n",
    "        #set starting window size\n",
    "        self.geometry(\"400x200\")  \n",
    "\n",
    "        # Configure fonts\n",
    "        label_font = font.Font(family=\"Helvetica\", size=12, weight=\"bold\")\n",
    "        entry_font = font.Font(family=\"Helvetica\", size=12)\n",
    "        button_font = font.Font(family=\"Helvetica\", size=12, weight=\"bold\")\n",
    "        \n",
    "        #frame sizes\n",
    "        frame = Frame(self)\n",
    "        frame.pack(padx=20, pady=20)\n",
    "\n",
    "        # Start Time\n",
    "        start_time_label = Label(frame, text=\"Start Time (seconds):\")\n",
    "        start_time_label.grid(row=0, column=0, padx=10, pady=10)\n",
    "\n",
    "        self.start_time_entry = Entry(frame, width=20)\n",
    "        self.start_time_entry.grid(row=0, column=1, padx=10, pady=10)\n",
    "\n",
    "        # Flag Name\n",
    "        flag_name_label = Label(frame, text=\"Flag Name:\")\n",
    "        flag_name_label.grid(row=1, column=0, padx=10, pady=10)\n",
    "\n",
    "        self.flag_name_entry = Entry(frame, width=20)\n",
    "        self.flag_name_entry.insert(0, \"BUBBLE\")  # Default value\n",
    "        self.flag_name_entry.grid(row=1, column=1, padx=10, pady=10)\n",
    "\n",
    "        # Button\n",
    "        flag_button = Button(frame, text=\"FLAG\", command=self.generate_csv, font=button_font)\n",
    "        flag_button.grid(row=2, column=0, columnspan=2, pady=20)\n",
    "\n",
    "        # Light gray colour for background\n",
    "        frame.configure(bg=\"#f0f0f0\") \n",
    "        # Slightly darker gray colour background\n",
    "        self.configure(bg=\"#e0e0e0\")   \n",
    "\n",
    "    def generate_csv(self):\n",
    "        start_time_str = self.start_time_entry.get()\n",
    "\n",
    "        try:\n",
    "            start_time_seconds = int(start_time_str)\n",
    "        except ValueError:\n",
    "            messagebox.showerror(\"Invalid Input\", \"Please enter a valid number\")\n",
    "            return\n",
    "        \n",
    "        #fixed offset number\n",
    "        epoch_offset = 2082844800\n",
    "        start_time = datetime.fromtimestamp(start_time_seconds - epoch_offset)\n",
    "        now = datetime.utcnow()\n",
    "        current_time_seconds = (now - start_time).seconds\n",
    "\n",
    "        # Subtract 82800 seconds\n",
    "        adjusted_time_seconds = current_time_seconds - 82800\n",
    "\n",
    "        flag_name = self.flag_name_entry.get()\n",
    "        \n",
    "        #saving file on desktop\n",
    "        desktop_path = os.path.join(os.path.expanduser(\"~\"), \"Desktop\")\n",
    "        file_path = os.path.join(desktop_path, \"Bubbles.csv\")\n",
    "\n",
    "        file_exists = os.path.isfile(file_path)\n",
    "        \n",
    "        #csv data\n",
    "        csv_data = [\n",
    "            [\"Time (seconds)\", \"Concentration\"],\n",
    "            [adjusted_time_seconds, flag_name]\n",
    "        ]\n",
    "\n",
    "        try:\n",
    "            #appending \n",
    "            with open(file_path, 'a', newline='') as csvfile:  \n",
    "                writer = csv.writer(csvfile)\n",
    "                if not file_exists or os.stat(file_path).st_size == 0:  \n",
    "                    #header\n",
    "                    writer.writerow(csv_data[0]) \n",
    "                    #row\n",
    "                writer.writerow(csv_data[1])  \n",
    "        #messagebox\n",
    "        except Exception as e:\n",
    "            messagebox.showerror(\"Error\", f\"Failed to write CSV file: {str(e)}\")\n",
    "            return\n",
    "        \n",
    "        # Commenting out the messagebox to prevent it from showing every time\n",
    "        # messagebox.showinfo(\"CSV Generated\", f\"Data appended to CSV file:\\n{file_path}\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app = BubblesApp()\n",
    "    app.mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "52ea570b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}