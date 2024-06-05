import os
import tkinter as tk
from tkinter import messagebox

income_file="income_data.txt"
expense_file="expense_data.txt"

def clear_files():
    if os.path.exists(income_file):
        os.remove(income_file)
    if os.path.exists(expense_file):
        os.remove(expense_file)
    with open(income_file, "w") as f:
        pass
    with open(expense_file, "w") as f:
        pass

def load_data(file_path):
    data=[]
    if os.path.exists(file_path) and os.path.getsize(file_path)>0:
        with open(file_path,'r') as f:
            for line in f:
                category,amount=line.strip().split(',')
                data.append({'Category': category,'Amount': float(amount)})
    return data

income_data=load_data(income_file)
expense_data=load_data(expense_file)

def save_data(data, file_path):
    with open(file_path, "w") as file:
        for entry in data:
            file.write(f"{entry['Category']},{entry['Amount']}\n")

def add_income(category, amount):
    if not category or amount is None:
        messagebox.showwarning("Input Error", "Please enter both category and amount.")
        return
    income_data.append({"Category": category,"Amount": amount})
    save_data(income_data,income_file)
    messagebox.showinfo("Success", "Income is Successfully Added")
    print("Current Income Data:", income_data)

def add_expense(category, amount):
    if not category or amount is None:
        messagebox.showwarning("Input Error", "Please enter both category and amount.")
        return
    expense_data.append({"Category": category, "Amount": amount})
    save_data(expense_data, expense_file)
    messagebox.showinfo("Success", "Expense is Successfully Added")
    print("Current Expense Data:", expense_data)

def calculate_budget():
    total_income=sum(i['Amount'] for i in income_data)
    total_expense=sum(i["Amount"] for i in expense_data)
    remaining_budget=total_income - total_expense
    messagebox.showinfo("Budget Calculation", 
                        f"Total Income: {total_income:.3f}\n"
                        f"Total Expense: {total_expense:.3f}\n"
                        f"Remaining Budget: {remaining_budget:.3f}")

def analyse_budget():
    categories={}
    for i in expense_data:
        if i["Category"] in categories:
            categories[i["Category"]]+=i["Amount"]
        else:
            categories[i["Category"]]=i["Amount"]
    analysis="Expense Analysis by Category:\n"
    for category,total in categories.items():
        analysis+=f"{category}: {total:.3f}\n"
    messagebox.showinfo("Budget Analysis",analysis)

clear_files()

root=tk.Tk()
root.title("Budget Tracker")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

frame=tk.Frame(root,bg="#f0f0f0")
frame.pack(pady=20)

title_label=tk.Label(frame,text="Budget Tracker",font=("Arial", 16, "bold"),bg="#f0f0f0")
title_label.grid(row=0,column=0,columnspan=2,pady=10)

category_label=tk.Label(frame,text="Category:",bg="#f0f0f0")
category_label.grid(row=1,column=0,padx=10,pady=5)
category_entry=tk.Entry(frame,width=20)
category_entry.grid(row=1,column=1,padx=10,pady=5)

amount_label=tk.Label(frame,text="Amount:",bg="#f0f0f0")
amount_label.grid(row=2,column=0,padx=10,pady=5)
amount_entry=tk.Entry(frame, width=20)
amount_entry.grid(row=2,column=1,padx=10,pady=5)

def handle_add_income():
    category=category_entry.get()
    try:
        amount=float(amount_entry.get())
    except ValueError:
        messagebox.showwarning("Input Error","Please enter a valid amount.")
        return
    add_income(category,amount)

def handle_add_expense():
    category=category_entry.get()
    try:
        amount=float(amount_entry.get())
    except ValueError:
        messagebox.showwarning("Input Error","Please enter a valid amount.")
        return
    add_expense(category,amount)

add_income_button=tk.Button(frame, text="Add Income",command=handle_add_income,bg="#4CAF50",fg="white",width=15)
add_income_button.grid(row=3,column=0,padx=10,pady=10)

add_expense_button=tk.Button(frame, text="Add Expense",command=handle_add_expense,bg="#f44336",fg="white",width=15)
add_expense_button.grid(row=3,column=1,padx=10,pady=10)

calculate_budget_button=tk.Button(frame,text="Calculate Budget",command=calculate_budget,bg="#2196F3",fg="white",width=15)
calculate_budget_button.grid(row=4,column=0,padx=10,pady=10)

analyse_budget_button=tk.Button(frame,text="Analyse Budget",command=analyse_budget,bg="#FFC107",fg="white",width=15)
analyse_budget_button.grid(row=4,column=1,padx=10,pady=10)

exit_button=tk.Button(frame,text="Exit",command=root.quit,bg="#9E9E9E",fg="white",width=32)
exit_button.grid(row=5,column=0,columnspan=2,pady=10)

root.mainloop()
