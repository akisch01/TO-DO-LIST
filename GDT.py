import tkinter as tk
from tkinter import messagebox

# Fonction pour ajouter une tâche
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Erreur", "Vous devez entrer une tâche.")

# Fonction pour supprimer une tâche
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Erreur", "Vous devez sélectionner une tâche.")

# Fonction pour marquer une tâche comme terminée
def mark_task_completed():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(tk.END, task + " - Terminé")
    except:
        messagebox.showwarning("Erreur", "Vous devez sélectionner une tâche.")

# Création de la fenêtre principale
window = tk.Tk()
window.title("Gestionnaire de Tâches")

# Champ de saisie pour ajouter une tâche
task_entry = tk.Entry(window, width=30)
task_entry.pack(pady=10)

# Boutons pour ajouter, supprimer, et marquer une tâche comme terminée
add_task_button = tk.Button(window, text="Ajouter Tâche", command=add_task)
add_task_button.pack(pady=5)

delete_task_button = tk.Button(window, text="Supprimer Tâche", command=delete_task)
delete_task_button.pack(pady=5)

mark_task_completed_button = tk.Button(window, text="Marquer comme Terminé", command=mark_task_completed)
mark_task_completed_button.pack(pady=5)

# Liste pour afficher les tâches
tasks_listbox = tk.Listbox(window, width=50, height=15)
tasks_listbox.pack(pady=10)

# Lancement de la boucle principale de l'application
window.mainloop()
