# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:29:11 2019

@author: lisa_
"""

from tkinter import *
from tkinter import messagebox
class Window(Frame):
        def __init__(self, master=None):
                Frame.__init__(self, master)
                self.master = master
# Creating result text field
                self.resultField = Text(master, bg="#000000", fg="#4EFEB3", height=1, width=16)
                self.resultField.insert(INSERT, "0")
                self.resultField.grid(row=0, columnspan=4)
# Creating number and operation buttons
                b1 = Button(master, bg="#000000", fg="#4EFEB3", text="  1  ", command=lambda: self.notice(1))
                b2 = Button(master, bg="#000000", fg="#4EFEB3", text="   2   ", command=lambda: self.notice(2))
                b3 = Button(master, bg="#000000", fg="#4EFEB3", text="    3   ", command=lambda: self.notice(3))
                bPlus = Button(master, bg="#000000", fg="#4EFEB3", text="   +  ", command=lambda: self.notice("+"))
                b4 = Button(master, bg="#000000", fg="#4EFEB3", text="  4  ", command=lambda: self.notice(4))
                b5 = Button(master, bg="#000000", fg="#4EFEB3", text="   5   ", command=lambda: self.notice(5))
                b6 = Button(master, bg="#000000", fg="#4EFEB3", text="    6   ", command=lambda: self.notice(6))
                bMinus = Button(master, bg="#000000", fg="#4EFEB3", text="    -  ", command=lambda: self.notice("-"))
                b7 = Button(master, bg="#000000", fg="#4EFEB3", text="  7  ", command=lambda: self.notice(7))
                b8 = Button(master, bg="#000000", fg="#4EFEB3", text="   8   ", command=lambda: self.notice(8))
                b9 = Button(master, bg="#000000", fg="#4EFEB3", text="    9   ", command=lambda: self.notice(9))
                bMultip = Button(master, bg="#000000", fg="#4EFEB3", text="   X  ", command=lambda: self.notice("x"))
                b0 = Button(master, bg="#000000", fg="#4EFEB3", text="  0  ", command=lambda: self.notice(0))
                bLeft = Button(master, bg="#000000", fg="#4EFEB3", text="  （  ", command=lambda: self.notice("("))
                bRight = Button(master, bg="#000000", fg="#4EFEB3", text="    ） ", command=lambda: self.notice(")"))
                bDivide = Button(master, bg="#000000", fg="#4EFEB3", text="    /  ", command=lambda: self.notice("/"))
# Aligning number and operation buttons
                b1.grid(row=1, column=0)
                b2.grid(row=1, column=1)
                b3.grid(row=1, column=2)
                bPlus.grid(row=1, column=3)
                b4.grid(row=2, column=0)
                b5.grid(row=2, column=1)
                b6.grid(row=2, column=2)
                bMinus.grid(row=2, column=3)
                b7.grid(row=3, column=0)
                b8.grid(row=3, column=1)
                b9.grid(row=3, column=2)
                bMultip.grid(row=3, column=3)
                b0.grid(row=4, column=0)
                bLeft.grid(row=4, column=1)
                bRight.grid(row=4, column=2)
                bDivide.grid(row=4, column=3)
# Creating and aligning calculation buttons
                bCalculate = Button(master, bg="#000000", fg="#4EFEB3", text="  ═  ", command=self.displayRes)
                bClear = Button(master, bg="#000000", fg="#4EFEB3", text=" AC ", command=self.clear)
                bDot = Button(master, bg="#000000", fg="#4EFEB3", text="  .   ", command=self.dot)
                bDelete = Button(master, bg="#000000", fg="#4EFEB3", text="  DEL", command=self.delete)
                bCalculate.grid(row=5, column=1)
                bClear.grid(row=5, column=3)
                bDot.grid(row=5, column=0)
                bDelete.grid(row=5, column=2)
        def dot(self):
                self.resultField.insert(INSERT, ".")
        def delete(self):
                res = self.resultField.get("0.0", END)
                self.resultField.delete("0.0")
                if len(res) == 2:
                    self.resultField.insert(INSERT, "0")
                else:
                    self.resultField.insert(INSERT, "")
        def notice(self, num):
                if self.resultField.get("0.0", END) == "0\n":
                        self.resultField.delete("0.0", END)
                self.resultField.insert(INSERT, str(num))
        def clear(self):
                self.resultField.delete("0.0", END)
                self.resultField.insert(INSERT, "0")
        def displayRes(self):
                res = self.calculate(self.resultField.get("0.0",END)[:-1])
                self.resultField.delete("0.0", END)
                self.resultField.insert(INSERT, str(res))
        def calculate(self, task):
                if task == "ERROR":
                        return "ERROR" # don't proceed if error happened in underlying call
                try:
                        return(float(task))
                except ValueError:
                        if ")" in task:
                                level = 0
                                maxLevelStartIndex = 0
                                maxLevelEndIndex = 0
                                for i in range(0, len(task)):
                                        if task[i] == "(":
                                                level += 1
                                                maxLevelStartIndex = i
                                        if task[i] == ")":
                                                level -= 1
                                if level != 0:
                                        messagebox.showerror("Error", "ERROR: brackets don't match: %i layers too much in expression %s" %(level, task))
                                        return "ERROR"
                                for i in range(maxLevelStartIndex, len(task)):
                                        if task[i] == ")":
                                                maxLevelEndIndex = i
                                                break
                                newTask = task[:maxLevelStartIndex] + str(self.calculate(task[maxLevelStartIndex+1:maxLevelEndIndex])) + task[maxLevelEndIndex+1:]
                                return self.calculate(newTask)
                        elif "+" in task:
                                tesk = task.split("+")
                                res = self.calculate(tesk[0])
                                for t in tesk[1:]:
                                        res += self.calculate(t)
                                return res
                        elif "-" in task:
                                tesk = task.split("-")
                                res = self.calculate(tesk[0])
                                for t in tesk[1:]:
                                        res -= self.calculate(t)
                                return res
                        elif "*" in task:
                                tesk = task.split("*")
                                res = self.calculate(tesk[0])
                                for t in tesk[1:]:
                                        res *= self.calculate(t)
                                return res
                        elif "/" in task:
                                tesk = task.split("/")
                                res = self.calculate(tesk[0])
                                for t in tesk[1:]:
                                        try:
                                                res /= self.calculate(t)
                                        except ZeroDivisionError:
                                                messagebox.showerror("Error", "ERROR: division by 0")
                                                return "ERROR"
                                return res
                        else:
                                messagebox.showerror("Error", "ERROR: invalid expression")
                                return "ERROR"
root = Tk()
app = Window(root)
root.wm_title("Calculator")
root.mainloop()