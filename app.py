import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import json

# ---------- Extra Features ----------

def get_zodiac(day, month):
    zodiac_signs = [
        ("♑Capricorn🐐", 19), ("♒Aquarius🌊", 18), ("♓Pisces🐟", 20),
        ("♈Aries🐏", 19), ("♉Taurus🐂", 20), ("♊Gemini🤵🏻👸🏻", 20),
        ("♋Cancer🦀", 22), ("♌Leo🦁", 22), ("♍Virgo🌾", 22),
        ("♎Libra⚖️", 22), ("♏Scorpio🦂", 21), ("♐Sagittarius🏹", 21),
        ("♑Capricorn🐐", 31)
    ]
    return zodiac_signs[month-1][0] if day <= zodiac_signs[month-1][1] else zodiac_signs[month][0]


def save_data(dob, name):
    with open("user_data.json", "w") as f:
        json.dump({
            "dob": dob.strftime("%Y-%m-%d"),
            "name": name
        }, f)


def load_data():
    try:
        with open("user_data.json", "r") as f:
            data = json.load(f)
            cal.set_date(data["dob"])
            name_entry.insert(0, data.get("name", ""))
    except:
        pass


def animate_button():
    btn.config(bg="#ff69b4")
    root.after(150, lambda: btn.config(bg="#D74894"))


# ---------- Function ----------
def calculate():
    try:
        name = name_entry.get().strip() or "User"

        dob_str = cal.get_date()
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
        today = datetime.now()

        age = relativedelta(today, dob)

        next_birthday = dob.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)

        days_left = (next_birthday - today).days
        nth = age.years + 1
        hours_lived = int((today - dob).total_seconds() // 3600)

        # ---------- NEW FEATURES ----------
        zodiac = get_zodiac(dob.day, dob.month)
        weekday = next_birthday.strftime("%A")

        save_data(dob, name)

        # Wishes
        msg = ""
        if today.month == dob.month and today.day == dob.day:
            msg = f"🎉 Happy Birthday {name}!🌹🎂🍬🎈🏮 Wishing you a Prosperous year filled with happiness, success and great health."
        elif (today - timedelta(days=1)).strftime("%m-%d") == dob.strftime("%m-%d"):
            msg = f"✨ Hope yesterday you had a wonderful birthday {name}! Wishing you an amazing year ahead💯💫"
        elif (today + timedelta(days=1)).strftime("%m-%d") == dob.strftime("%m-%d"):
            msg = f"🎂 Hey {name}, your special day is almost here! Wishing you a Fabulous Birthday in advance ❤️"

        result = f"""Age: {age.years}Years {age.months}Months {age.days}Days
Hours lived: {hours_lived}
Days left for next birthday: {days_left}
Next birthday: {nth}th

Zodiac: {zodiac}
Next Birthday Day: {weekday}

{msg}"""

        result_label.config(text=result)
        animate_button()

    except:
        result_label.config(text="❌ Invalid Date")


# ---------- UI ----------
root = tk.Tk()
root.title("Birthday Calculator")
root.geometry("420x520")
root.configure(bg="#FFB3DE")

# ---------- Center Frame ----------
center_frame = tk.Frame(root, bg="#FFB3DE")
center_frame.place(relx=0.5, rely=0.45, anchor="center")

# ---------- Heading ----------
title = tk.Label(
    center_frame,
    text="Birthday Calculator 🎂",
    font=("Segoe UI", 18, "bold"),
    bg="#FFB3DE",
    fg="#333"
)
title.pack(pady=8)

# ---------- Name Input ----------
name_label = tk.Label(
    center_frame,
    text="Enter Your Name",
    font=("Segoe UI", 10, "bold"),
    bg="#FFB3DE",
    fg="#333"
)
name_label.pack()

name_entry = tk.Entry(
    center_frame,
    font=("Segoe UI", 10),
    justify="center"
)
name_entry.pack(pady=5)

# ---------- Calendar ----------
cal = Calendar(
    center_frame,
    selectmode='day',
    year=2000,
    date_pattern="yyyy-mm-dd"
)
cal.pack(pady=5)

# ---------- Button ----------
btn = tk.Button(
    center_frame,
    text="Calculate",
    command=calculate,
    font=("Segoe UI", 11, "bold"),
    bg="#D74894",
    fg="white",
    relief="flat",
    padx=12,
    pady=5
)
btn.pack(pady=15)

# ---------- Output ----------
result_label = tk.Label(
    center_frame,
    text="",
    font=("Segoe UI", 10, "bold"),
    bg="#FFB3DE",
    fg="#222",
    justify="center",
    wraplength=360
)
result_label.pack(pady=5)

# ---------- Footer ----------
footer = tk.Label(
    root,
    text="Developed and Designed by Santhosh",
    font=("Segoe UI", 10, "bold"),
    bg="#FFB3DE",
    fg="#333"
)
footer.pack(side="bottom", pady=10)

# ---------- Init ----------
load_data()

# ---------- Run ----------
root.mainloop()