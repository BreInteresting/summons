'''
The purpose of this application is that during D&D, the players and the DM can track the 
status of a summon or companion. Allowing users to record the ability scores, hit points, 
duration of summon, abilities, attacks, and roll dice when needed from Saves, Check, and 
damage when attacking.
Program: SummonsCompaionTracker.py
Author: Bri Manning
Date: 2/5/2024
Version 1.0
'''
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

def new_campaign():
    campaign_name = simpledialog.askstring("New Campaign", "Enter campaign name:")
    if campaign_name:
        messagebox.showinfo("New Campaign", f"Created campaign: {campaign_name}")
        new_summon()

def new_summon():
    summon_window = tk.Toplevel(main_window)
    summon_window.title("New Summon")

    name_label = tk.Label(summon_window, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(summon_window)
    name_entry.pack()

    type_label = tk.Label(summon_window, text="Type:")
    type_label.pack()
    type_entry = tk.Entry(summon_window)
    type_entry.pack()

    description_label = tk.Label(summon_window, text="Description:")
    description_label.pack()
    description_entry = tk.Entry(summon_window)
    description_entry.pack()

    hp_label = tk.Label(summon_window, text="Hit Points:")
    hp_label.pack()
    hp_entry = tk.Entry(summon_window)
    hp_entry.pack()

    speed_label = tk.Label(summon_window, text="Speed:")
    speed_label.pack()
    speed_entry = tk.Entry(summon_window)
    speed_entry.pack()

    abilities_label = tk.Label(summon_window, text="Abilities:")
    abilities_label.pack()

    ability_frame = tk.Frame(summon_window)
    ability_frame.pack()

    ability_labels = ["Strength:", "Dexterity:", "Constitution:", "Intelligence:", "Wisdom:", "Charisma:"]
    ability_entries = []

    for label in ability_labels:
        ability_label = tk.Label(ability_frame, text=label)
        ability_label.pack(side=tk.LEFT)
        ability_entry = tk.Entry(ability_frame)
        ability_entry.pack(side=tk.LEFT)
        ability_entries.append(ability_entry)

    attack_label = tk.Label(summon_window, text="Attacks:")
    attack_label.pack()

    attacks_frame = tk.Frame(summon_window)
    attacks_frame.pack()

    attacks = []

    def add_attack():
        attack_name = attack_entry.get()
        if attack_name:
            attack_window = tk.Toplevel(summon_window)
            attack_window.title(attack_name)

            name_label = tk.Label(attack_window, text="Attack Name:")
            name_label.pack()
            name_entry = tk.Entry(attack_window)
            name_entry.pack()

            damage_label = tk.Label(attack_window, text="Damage:")
            damage_label.pack()
            damage_entry = tk.Entry(attack_window)
            damage_entry.pack()

            def save_attack():
                attack = {
                    "Name": name_entry.get(),
                    "Damage": damage_entry.get()
                }
                attacks.append(attack)
                messagebox.showinfo("Attack Details", f"Attack created: {attack}")
                attack_window.destroy()

            save_button = tk.Button(attack_window, text="Save", command=save_attack)
            save_button.pack()

            attack_entry.delete(0, tk.END)

    attack_entry = tk.Entry(summon_window)
    attack_entry.pack()
    attack_button = tk.Button(summon_window, text="Add Attack", command=add_attack)
    attack_button.pack()

    def submit_summon():
        summon = {
            "Name": name_entry.get(),
            "Type": type_entry.get(),
            "Description": description_entry.get(),
            "Hit Points": hp_entry.get(),
            "Speed": speed_entry.get(),
            "Abilities": {label.strip(":"): entry.get() for label, entry in zip(ability_labels, ability_entries)},
            "Attacks": attacks
        }
        messagebox.showinfo("Summon Details", f"Summon created:\n{summon}")
        summon_window.destroy()
        new_campaign()

    submit_button = tk.Button(summon_window, text="Submit", command=submit_summon)
    submit_button.pack()

def load_campaign():
    messagebox.showinfo("Load Campaign", "Placeholder for loading campaigns")

def delete_campaign():
    messagebox.showinfo("Delete Campaign", "Placeholder for deleting campaigns")

main_window = tk.Tk()
main_window.title("Main Menu")

new_campaign_button = tk.Button(main_window, text="New Campaign", command=new_campaign)
new_campaign_button.pack()

load_campaign_button = tk.Button(main_window, text="Load Campaign", command=load_campaign)
load_campaign_button.pack()

delete_campaign_button = tk.Button(main_window, text="Delete Campaign", command=delete_campaign)
delete_campaign_button.pack()

main_window.mainloop()