# *********************** College Management System ********************************


# importing library's

from tkinter import *
from tkinter.messagebox import * 
from tkinter.scrolledtext import * 
# from mysql.connector import *
from mysql.connector import MySQLConnection
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



# function for buttons

# -----------main to student
def f1():
	root.withdraw()
	sw.deiconify()

#-----------student to main page

def f2():
	sw.withdraw()
	root.deiconify()

#----------- main to department

def f3():
	root.withdraw()
	dew.deiconify()

#-----------department to main

def f4():
	dew.withdraw()
	root.deiconify()

#-------student to add page

def f5():
	sw.withdraw()
	aw.deiconify()

#---------- add page to student 

def f6():
	aw.withdraw()
	sw.deiconify()

#-----------student to view page
def f7():
	sw.withdraw()
	vw.deiconify()

	# this code for view the data in view page
	vw_st_data.delete(1.0,END)
	con = None
	try:
		con = connect(host="localhost",user="root",password="Mangesh@123",database="collegedb")
		cursor =con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data:
			info = info + "Student Roll No. = " + str(d[0])+"\nName = " +str(d[1])+"\nEmail ID = " +str(d[2]) +"\nStudent Dept = " + str(d[3])+"\n"+("_" * 37) + "\n"
		vw_st_data.insert(INSERT, info)
	except Exception as e:
		showerror("Issue ",e)
	finally:
		if con is not None:
			con.close()

#----------view page to student
def f8():
	vw.withdraw()
	sw.deiconify() 


#---------student to update page
def f9():
	sw.withdraw()
	uw.deiconify()

#----------update page to student
def f10():
	uw.withdraw()
	sw.deiconify()


#----------student to delete page
def f11():
	sw.withdraw()
	dw.deiconify()

#----------delete page to student 
def f12():
	dw.withdraw()
	sw.deiconify()


#***************
#-------department to add page

def f13():
	dew.withdraw()
	daw.deiconify()

#---------- add page to department 

def f14():
	daw.withdraw()
	dew.deiconify()

#-----------department to view page
def f15():
	dew.withdraw()
	dvw.deiconify()

	# this code for view the data in view page
	dvw_st_data.delete(1.0,END)
	con = None
	try:
		con = connect(host="localhost",user="root",password="Mangesh@123",database="collegedb")
		cursor =con.cursor()
		sql = "select * from department"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data:
			info = info + "Dept ID = " + str(d[0])+"\nDept Name = " +str(d[1])+"\nDept HOD = " +str(d[2]) +"\n"+("_" * 37) + "\n"
		dvw_st_data.insert(INSERT, info)
	except Exception as e:
		print("Issue ",e)
	finally:
		if con is not None:
			con.close()

#----------view page to department
def f16():
	dvw.withdraw()
	dew.deiconify() 


#---------department to update page
def f17():
	dew.withdraw()
	duw.deiconify()

#----------update page to department
def f18():
	duw.withdraw()
	dew.deiconify()


#----------department to delete page
def f19():
	dew.withdraw()
	ddw.deiconify()

#----------delete page to department 
def f20():
	ddw.withdraw()
	dew.deiconify()

# ______________________for add student page_____________________________________

def addstu():
	con = None
	try:
		con = connect(host="localhost",user="root",password="Mangesh@123",database="collegedb")

		rno = int(aw_ent_rno.get())
		name = aw_ent_name.get()
		email = aw_ent_email.get()
		dept = dept_name.get()
		
		cursor = con.cursor()
		sql = "insert into student values('%d','%s','%s','%s')"
		cursor.execute(sql%(rno,name,email,dept))
		con.commit()		
		showinfo("Success", "Record Created")
		
	except Exception as e:
		if con is not None:
			con.rollback()
		showerror("Issue","Please Enter Valid Detail's")
	finally:
		if con is not None:
			con.close()
		aw_ent_rno.delete(0,END)
		aw_ent_name.delete(0,END)
		aw_ent_email.delete(0,END)
		aw_ent_rno.focus()


# ___________________________here update student_________________________________

def updatestu():
	con = None
	try:
		con = connect(host = "localhost", user = "root", password = "Mangesh@123",			database = "collegedb")
		cursor = con.cursor()
		sql = "update student set name ='%s',email ='%s',Dept ='%s' where rno = '%d'"
		rno = int(uw_ent_rno.get())
		name = uw_ent_name.get()
		email = uw_ent_email.get()
		dept = dept_name.get()
		cursor.execute(sql % (name,email,dept,rno))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Updated", "Record Updated")
		else:
			showinfo("Failed", "Record does not exists")

	except Exception as e:
		if con is not None:
			con.rollback()
		showerror("Issue", "Please Enter Valid Details")
	finally:
		if con is not None:
			con.close()
		uw_ent_rno.delete(0,END)
		uw_ent_name.delete(0,END)
		uw_ent_email.delete(0,END)
		uw_ent_rno.focus()


# _______________________for delete student____________________________________

def deletestu():
	con = None

	try:
		con = connect(host = "localhost", user = "root", password = "Mangesh@123",			database = "collegedb")
		cursor = con.cursor()
		sql = "delete from student where rno = '%d'"
		rno = int(dw_ent_rno.get())
		cursor.execute(sql % (rno))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Deleted", "Record Deleted")
		else:
			showinfo("Failed", "Record does not exists")

	except Exception as e:
		if con is not None:
			con.rollback()
		showerror("Issue",  "Please Enter valid rno")
	finally:
		if con is not None:
			con.close()
		dw_ent_rno.delete(0,END)
		dw_ent_rno.focus()


#*************************************************************************
# ______________________for add department page_____________________________

def adddept():
	con = None
	try:
		con = connect(host="localhost",user="root",password="Mangesh@123",database="collegedb")
		id = int(daw_ent_id.get())
		dname = daw_ent_dname.get()
		hod = daw_ent_hod.get()
		cursor = con.cursor()
		sql = "insert into department values('%d','%s','%s')"
		cursor.execute(sql%(id,dname,hod))
		con.commit()		
		showinfo("Success", "Record Created")
		
	except Exception as e:
		if con is not None:
			con.rollback()
		showerror("Issue","Please Enter Valid Details")
	finally:
		if con is not None:
			con.close()
		daw_ent_id.delete(0,END)
		daw_ent_dname.delete(0,END)
		daw_ent_hod.delete(0,END)
		daw_ent_id.focus()



# _______________________here update department details_________________________

def updatedept():
	con = None
	try:
		con = connect(host = "localhost", user = "root", password = "Mangesh@123",			database = "collegedb")
		cursor = con.cursor()
		sql = "update department set dname ='%s',hod ='%s' where id = '%d'"
		id = int(duw_ent_id.get())
		dname = duw_ent_dname.get()
		hod = duw_ent_hod.get()
		cursor.execute(sql % (dname,hod,id))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Updated", "Record Updated")
		else:
			showinfo("Failed", "Record does not exists")

	except Exception as e:
		if con is not None:
			con.rollback()
		showerror("Issue",  "Please Enter Valid Details")
	finally:
		if con is not None:
			con.close()
		duw_ent_id.delete(0,END)
		duw_ent_dname.delete(0,END)
		duw_ent_hod.delete(0,END)
		duw_ent_id.focus()

# _______________________for delete department_________________________________

def deletedept():
	con = None

	try:
		con = connect(host = "localhost", user = "root", password = "Mangesh@123",			database = "collegedb")
		cursor = con.cursor()
		sql = "delete from department where id = '%d'"
		id = int(ddw_ent_id.get())
		cursor.execute(sql % (id))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Deleted", "Record Deleted")
		else:
			showinfo("Failed", "Record does not exists")

	except Exception as e:
		if con is not None:
			con.rollback()
		showerror("Issue",  "Please Enter Dept ID")
	finally:
		if con is not None:
			con.close()
		ddw_ent_id.delete(0,END)
		ddw_ent_id.focus()

#___________________chart________________________________________

def chart():
	
	con = None
	try:
		con = connect(host="localhost",user="root",password="Mangesh@123",database="collegedb")
		cursor = con.cursor()
	# Fecthing Data From mysql to my python progame
		cursor.execute("select dept,count(rno) from student group by dept;")
		result = cursor.fetchall

		dname = []
		rno = []
	
		for i in cursor:
			dname.append(i[0])
			rno.append(i[1])

		plt.bar(dname,rno,width = 0.40)
		plt.xlabel("Name of Department")
		plt.ylabel("No. of Student")
		plt.title("Count of Students")
		plt.show()

	except Exception as e:
		if con is not None:
			showerror("Issue", "Please Check Detail's !!!")
	finally:
		if con is not None:
			con.close()




# --------------------------Main Page----------------------------------

root = Tk()
root.title("College Management System")
root.geometry("600x700+50+50")
#root.iconbitmap("employee.ico")
f =("Arial",26,"bold")
root.configure(bg ="lightblue")

lab_head = Label(root,text="College Management System",fg = "red",font=('Times', 35 ,"bold"))
lab_head.config(bg="lightblue")
lab_head.pack(pady = 30)
btn_add = Button(root,text ="Student",font = f, width= 15,command = f1)
btn_add.pack(pady=25)
btn_view = Button(root,text ="Department",font = f, width= 15,command = f3)
btn_view.pack(pady=25)



# ----------------------second frame for student---------------------------- 

sw = Toplevel(root)
sw.title("Student Page")
sw.geometry("600x750+50+50")
sw.configure(bg = "lightgreen")

sw.lab_head = Label(sw,text="Student Information",fg = "red",font=('Times', 30,"bold"))
sw.lab_head.config(bg="lightgreen")
sw.lab_head.pack(pady = 20)

sw.btn_add = Button(sw,text ="Add Student",font = f, width= 15, command = f5)
sw.btn_add.pack(pady=18)
sw.btn_view = Button(sw,text ="View Students",font = f, width= 15, command = f7)
sw.btn_view.pack(pady=18)
sw.btn_update = Button(sw,text ="Update Student",font = f, width= 15, command = f9)
sw.btn_update.pack(pady=18)
sw.btn_delete = Button(sw,text ="Delete Student",font = f, width= 15, command = f11)
sw.btn_delete.pack(pady=18)
sw.btn_back = Button(sw,text ="Back",font = f, width= 8,bg = "skyblue",command = f2)
sw.btn_back.pack(pady=20)

sw.withdraw()



#------------------third main page for Department------------------------

dew = Toplevel(root)
dew.title("Department Page")
dew.geometry("600x750+50+50")
dew.configure(bg = "lightgreen")

dew.lab_head = Label(dew,text="Departments Information",fg = "red",font=('Times', 30,"bold"))
dew.lab_head.config(bg="lightgreen")
dew.lab_head.pack(pady = 20)

dew.btn_add = Button(dew,text ="Add Dept",font = f, width= 15,command = f13)
dew.btn_add.pack(pady=10)
dew.btn_view = Button(dew,text ="View Dept's",font = f, width= 15,command = f15)
dew.btn_view.pack(pady=10)
dew.btn_update = Button(dew,text ="Update Dept",font = f, width= 15,command = f17)
dew.btn_update.pack(pady=10)
dew.btn_delete = Button(dew,text ="Delete Dept",font = f, width= 15,command = f19)
dew.btn_delete.pack(pady=10)
dew.btn_chart = Button(dew,text ="Chart",font = f, width= 15,command = chart)
dew.btn_chart.pack(pady=10)


dew.btn_back = Button(dew,text ="Back",font = f, width= 8,bg = "skyblue",command = f4)
dew.btn_back.pack(pady=20)

dew.withdraw()



#______________________________________Add student page________________________________

aw = Toplevel(root)
aw.title("Add Student")
aw.geometry("600x750+50+50")
aw.configure(bg = "lightblue")

aw_lab_rno = Label(aw,text ="Enter rno", font = f)
aw_ent_rno = Entry(aw,font = f, bd = 2)
aw_lab_name = Label(aw, text = "Enter Name", font = f)
aw_ent_name = Entry(aw, font = f, bd = 2)
aw_lab_email = Label(aw, text = "Enter Email", font = f)
aw_ent_email = Entry(aw, font = f, bd = 2)


dept_name = StringVar()
dept_name.set("Computer")
list1 = ["Computer","IT"]
aw_droplist = OptionMenu(aw,dept_name,*list1)
aw_droplist.config(width = 15)
dept_name.set("Select Dept")
aw_droplist.config(font=  ("Arial",25,"bold"))

aw_btn_save = Button(aw, text = "Add", font =f, command = addstu)
aw_btn_back = Button(aw, text = "Back", font = f,command = f6)

aw_lab_rno.pack(pady = 10)
aw_ent_rno.pack(pady = 10)
aw_lab_name.pack(pady = 10)
aw_ent_name.pack(pady = 10)
aw_lab_email.pack(pady = 10)
aw_ent_email.pack(pady = 10)
aw_droplist.pack(pady=10)
aw_btn_save.pack(pady = 10)
aw_btn_back.pack(pady = 10)


aw.withdraw()




# _____________________________View students page___________________________________

vw = Toplevel(root)
vw.title("View Student")
vw.geometry("600x750+50+50")
vw.configure(bg = "lightyellow")
f1 = ("Arial",20)

vw_st_data = ScrolledText(vw, height = 17, font = f1, bd = 6)
vw_btn_back = Button(vw, text = "Back", font = f, command = f8)
vw_st_data.pack(pady = 10)
vw_btn_back.pack(pady = 10)

vw.withdraw()





#______________________________update student________________________________________

uw = Toplevel(root)
uw.title("Update Student")
uw.geometry("600x750+50+50")
uw.configure(bg="lightpink")

uw_lab_rno = Label(uw, text = "Enter rno", font = f)
uw_ent_rno = Entry(uw, font = f, bd = 2)
uw_lab_name = Label(uw, text = "Enter Name", font = f)
uw_ent_name = Entry(uw, font = f, bd = 2)
uw_lab_email = Label(uw, text = "Enter Email", font = f)
uw_ent_email = Entry(uw, font = f, bd = 2)
uw_lab_dept = Label(uw, text = "Select Dept Name", font = ("Arial",26,"bold"))


dept_name = StringVar()
list1 = ["Computer","IT"]
uw_droplist = OptionMenu(uw,dept_name,*list1)
uw_droplist.config(width = 15)
dept_name.set("Select Dept")
uw_droplist.config(font=  ("Arial",25,"bold"))

uw_btn_save = Button(uw, text = "Update", font = f,command = updatestu)
uw_btn_back = Button(uw, text = "Back", font = f, command = f10)

uw_lab_rno.pack(pady = 10)
uw_ent_rno.pack(pady = 10)
uw_lab_name.pack(pady = 10)
uw_ent_name.pack(pady = 10)
uw_lab_email.pack(pady = 10)
uw_ent_email.pack(pady = 10)
uw_droplist.pack(pady = 10)
uw_btn_save.pack(pady = 10)
uw_btn_back.pack(pady = 10)


uw.withdraw()




#____________________________Delete Student________________________________________

dw = Toplevel(root)
dw.title("Delete Student")
dw.geometry("600x750+50+50")
dw.configure(bg="orange")

dw_lab_rno = Label(dw, text = "Enter rno", font = f)
dw_ent_rno = Entry(dw, font = f, bd = 2)

dw_btn_save = Button(dw, text = "Delete", font = f,command = deletestu)
dw_btn_back = Button(dw, text = "Back", font = f, command = f12)

dw_lab_rno.pack(pady = 10)
dw_ent_rno.pack(pady = 10)
dw_btn_save.pack(pady = 10)
dw_btn_back.pack(pady = 10)
dw.withdraw()





# for department ****#*#*#*#*#*#*#*#*#*#*#*#*#*


#______________________________________Add department page________________________________

daw = Toplevel(root)
daw.title("Add Department")
daw.geometry("600x750+50+50")
daw.configure(bg = "lightblue")

daw_lab_id = Label(daw,text ="Enter ID", font = f)
daw_ent_id = Entry(daw,font = f, bd = 2)
daw_lab_dname = Label(daw, text = "Enter Dept Name", font = f)
daw_ent_dname = Entry(daw, font = f, bd = 2)
daw_lab_hod = Label(daw, text = "Enter HOD Name", font = f)
daw_ent_hod = Entry(daw, font = f, bd = 2)

daw_btn_save = Button(daw, text = "Add", font = f,command = adddept)
daw_btn_back = Button(daw, text = "Back", font = f,command = f14)

daw_lab_id.pack(pady = 10)
daw_ent_id.pack(pady = 10)
daw_lab_dname.pack(pady = 10)
daw_ent_dname.pack(pady = 10)
daw_lab_hod.pack(pady = 10)
daw_ent_hod.pack(pady = 10)
daw_btn_save.pack(pady = 10)
daw_btn_back.pack(pady = 10)

daw.withdraw()




# _____________________________View department page___________________________________

dvw = Toplevel(root)
dvw.title("View Department")
dvw.geometry("600x750+50+50")
dvw.configure(bg = "lightyellow")
f1 = ("Arial",20)

dvw_st_data = ScrolledText(dvw, height = 17, font = f1, bd = 6)
dvw_btn_back = Button(dvw, text = "Back", font = f, command = f16)
dvw_st_data.pack(pady = 10)
dvw_btn_back.pack(pady = 10)

dvw.withdraw()





#______________________________update department________________________________________

duw = Toplevel(root)
duw.title("Update Department")
duw.geometry("600x750+50+50")
duw.configure(bg="lightpink")

duw_lab_id = Label(duw, text = "Enter ID", font = f)
duw_ent_id = Entry(duw, font = f, bd = 2)
duw_lab_dname = Label(duw, text = "Enter Dept Name", font = f)
duw_ent_dname = Entry(duw, font = f, bd = 2)
duw_lab_hod = Label(duw, text = "Enter HOD Name", font = f)
duw_ent_hod = Entry(duw, font = f, bd = 2)

duw_btn_save = Button(duw, text = "Update", font = f,command = updatedept)
duw_btn_back = Button(duw, text = "Back", font = f, command = f18)

duw_lab_id.pack(pady = 10)
duw_ent_id.pack(pady = 10)
duw_lab_dname.pack(pady = 10)
duw_ent_dname.pack(pady = 10)
duw_lab_hod.pack(pady = 10)
duw_ent_hod.pack(pady = 10)
duw_btn_save.pack(pady = 10)
duw_btn_back.pack(pady = 10)

duw.withdraw()




#____________________________Delete department__________________________________________

ddw = Toplevel(root)
ddw.title("Delete Department")
ddw.geometry("600x750+50+50")
ddw.configure(bg="orange")

ddw_lab_id = Label(ddw, text = "Enter ID", font = f)
ddw_ent_id = Entry(ddw, font = f, bd = 2)

ddw_btn_save = Button(ddw, text = "Delete", font = f, command = deletedept)
ddw_btn_back = Button(ddw, text = "Back", font = f, command = f20)

ddw_lab_id.pack(pady = 10)
ddw_ent_id.pack(pady = 10)
ddw_btn_save.pack(pady = 10)
ddw_btn_back.pack(pady = 10)
ddw.withdraw()





#________________if user exit then showing message to user_______________________________

def fun():
	answer = askyesno(title='confirmation', message = 'Really you want to exit !!')
	if answer:
		root.destroy()
root.protocol("WM_DELETE_WINDOW",fun)


root.mainloop()
