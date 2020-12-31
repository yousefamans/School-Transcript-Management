import sqlite3

import pandas as pd

from sqlite3 import Error

from tkinter import *

from pandastable import Table

from pandastable import images
from pandastable.dialogs import addButton

import matplotlib.pyplot as ppt

import sys

import numpy as np 






# note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
gui = Tk()
gui.geometry("1000x600")

gui.attributes("-alpha", 0.89)



gui.rowconfigure(0,weight=1)
gui.columnconfigure(0,weight=1)

def show(frame):
    frame.tkraise()





frame14 = Frame(gui,bg='#070801')
frame13 = Frame(gui,bg='#070801')
frame12 = Frame(gui,bg='#070801')
frame11 = Frame(gui,bg='#070801')
frame10 = Frame(gui,bg='#070801')
frame9 = Frame(gui,bg='#070801')
frame8 = Frame(gui,bg='#070801')
frame7 = Frame(gui,bg='#070801')
frame6 = Frame(gui,bg='#070801')
frame5 = Frame(gui,bg='#070801')
frame4 = Frame(gui,bg='#070801')
frame3 = Frame(gui,bg='#070801')
frame2 = Frame(gui,bg='#070801')
frame1 = Frame(gui,bg='#070801')




for frame in (frame14,frame13,frame12,frame11,frame10,frame9,frame8, frame7, frame6, frame5,frame4,frame3, frame2,frame1):
    frame.grid(row=0,column=0,sticky='nsew')







########################################################################
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()
    

def sql_connection():

    try:

        con = sqlite3.connect(r"C:\Users\user\Videos\IT\attendance.db")

        return con

    except Error:

        print(Error)

lan = "a"        

def sql_table(con, query):

    cursorObj = con.cursor()

    cursorObj.execute(query)
        
   
     

    # Print the updated listed of tables after renaming the stud table
    def database_info():
        tableList = cursorObj.fetchall()


        for table in tableList:

            print("Database Object Type: %s"%(table[0]))

            print("Name of the database object: %s"%(table[1]))

            print("Name of the table: %s"%(table[2]))

            print("Root page: %s"%(table[3]))

            print("SQL Statement: %s"%(table[4]))

    #database_info()       

###############################################################
    con.commit()

con = sql_connection()

#sql_table(con,'select * from sqlite_master')

#sql_table(con,"delete from marks where admsn_no = 1003; ")

data = pd.read_sql("select name,exam,marks from marks ;",con)
#print(data)





def exec_data():
    sql_table(con,"select *  from marks; ")
    print(data)
    print(var1.get())
    print(var2.get())
    print(var3.get())
    print(pd.read_sql("select * from attendance ;",con))


back = Button(frame2, text=' ← ',height=1,width=4,font=1.5, bg="#46e385",command = lambda: show(frame4)) 
back.place(x=0,y=0)




adms_no = Label(frame2, text = "Admission no:",font=25)
adms_no.place(x=50,y=40)


s_name = Label(frame2, text = "Name:",font=25)
s_name.place(x=50,y=80)


stream = Label(frame2, text = "Stream:",font=25)
stream.place(x=50,y=120)

exam = Label(frame2, text = "Exam:",font=25)
exam.place(x=50,y=160)

marks = Label(frame2, text = "Marks:",font=25)
marks.place(x=50,y=200)

english = Label(frame2, text = "English:",font=25)
english.place(x=50,y=240)







my_list = ["Science / Commerce","Science + IT","Science + Math","Commerce + IT","Commerce + Math"]
options = StringVar(gui)
options.set(my_list[0]) # default value

e3 =OptionMenu(frame2, options, *my_list)
e3.place(x=350,y=120)



str_out= StringVar(gui)
str_out.set("Output")

l2 = Label(frame2,  textvariable=str_out, width=10 )  
l2.place(x=350,y=160) 




e1 = Entry(frame2,bd=1,width=30)
e1.place(x=350,y=40)

e2 = Entry(frame2,bd=1,width=30)
e2.place(x=350,y=80)






e4 = Entry(frame2,bd=1,width=30)
e4.place(x=350,y=160)


e5 = Entry(frame2,bd=1,width=30)
e5.place(x=350,y=200)

e6 = Entry(frame2,bd=1,width=30)
e6.place(x=350,y=240)



def it():
    global e7

    it = Label(frame2, text = "Informatics:",font=25)
    it.place(x=50,y=280)

    e7 = Entry(frame2,bd=1,width=30)
    e7.place(x=350,y=280)

def math():
    global e8

    
    maths = Label(frame2, text = "Maths:",font=25)
    maths.place(x=50,y=320)


    e8 = Entry(frame2,bd=1,width=30)
    e8.place(x=350,y=320)


def sci():

        
    chemistry = Label(frame2, text = "Chemistry:",font=25)
    chemistry.place(x=50,y=360)


    biology = Label(frame2, text = "Biology:",font=25)
    biology.place(x=50,y=400)


    physics = Label(frame2, text = "Physics:",font=25)
    physics.place(x=50,y=440)


    global e9
    e9 = Entry(frame2,bd=1,width=30)
    e9.place(x=350,y=360)

    global e10
    e10 = Entry(frame2,bd=1,width=30)
    e10.place(x=350,y=400)

    global e11
    e11 = Entry(frame2,bd=1,width=30)
    e11.place(x=350,y=440)

def com():

        
    economics = Label(frame2, text = "Economics:",font=25)
    economics.place(x=50,y=480)

    accountancy = Label(frame2, text = "Accountancy:",font=25)
    accountancy.place(x=50,y=520)


    business = Label(frame2, text = "Business:",font=25)
    business.place(x=50,y=560)



    global e12
    e12 = Entry(frame2,bd=1,width=30)
    e12.place(x=350,y=480)

    global e13    
    e13 = Entry(frame2,bd=1,width=30)
    e13.place(x=350,y=520)

    global e14
    e14 = Entry(frame2,bd=1,width=30)
    e14.place(x=350,y=560)




#print(str_out.set(options.get()))


        
def my_show(*args):
     str_out.set(options.get())
     if options.get() == "Science + IT":
        it()
        sci()
        

     elif options.get() == "Science + Math":
        math()

        sci()
     elif options.get() == "Commerce + IT":
            it()
            com()
     elif options.get() == "Commerce + Math":
        math()
        com()

     def insert_data():

         cursorObj = con.cursor()


                 
         

        

         


         

        
         if options.get() == "Science + IT" :
             
             
             SciIT = (int(e6.get()) + int(e7.get()) + int(e9.get()) + int(e10.get()) + int(e11.get()))/5
              

             cursorObj.execute("insert into marks (admsn_no ,name,stream , exam , marks , english , informatics , chemistry , biology , physics  ) VALUES (?,?,'s',?,?,?,?,?,?,?); ",(e1.get(),e2.get(),e4.get(),SciIT,e6.get(),e7.get(),e9.get(),e10.get(),e11.get()))
             con.commit()
             print(pd.read_sql("select admsn_no ,name,stream , exam , marks , english , informatics , chemistry , biology , physics  from marks;",con))

         if options.get() == "Science + Math" :
             
             
             SciMath = (int(e6.get()) + int(e8.get()) + int(e9.get()) + int(e10.get()) + int(e11.get()))/5

          

             cursorObj.execute("insert into marks (admsn_no ,name,stream , exam , marks , english , maths , chemistry , biology , physics  ) VALUES (?,?,'s',?,?,?,?,?,?,?); ",(e1.get(),e2.get(),e4.get(),SciMath,e6.get(),e8.get(),e9.get(),e10.get(),e11.get()))
             con.commit()
             print(pd.read_sql("select admsn_no ,name,stream , exam , marks , english , maths , chemistry , biology , physics from marks;",con))

         if options.get() == "Commerce + IT" :
             
             ComIT = (int(e6.get()) + int(e7.get()) + int(e12.get()) + int(e13.get()) + int(e14.get()))/5

       
       

             cursorObj.execute("insert into marks (admsn_no ,name,stream , exam , marks , english , informatics , economics , accountancy , business_studies  ) VALUES (?,?,'c',?,?,?,?,?,?,?); ",(e1.get(),e2.get(),e4.get(),ComIT,e6.get(),e7.get(),e12.get(),e13.get(),e14.get()))
             con.commit()
             print(pd.read_sql("select admsn_no ,name,stream , exam , marks , english , informatics , economics , accountancy , business_studies from marks;",con))


         if options.get() == "Commerce + Math" :
             
             
             ComMath = (int(e6.get()) + int(e8.get()) + int(e12.get()) + int(e13.get()) + int(e14.get()))/5

         
      

             cursorObj.execute("insert into marks (admsn_no ,name,stream , exam , marks , english , maths , economics , accountancy , business_studies  ) VALUES (?,?,'c',?,?,?,?,?,?,?); ",(e1.get(),e2.get(),e4.get(),ComMath,e6.get(),e8.get(),e12.get(),e13.get(),e14.get()))
             con.commit()
             print(pd.read_sql("select admsn_no ,name,stream , exam , marks , english , maths , economics , accountancy , business_studies from marks;",con))


            

             

     insert = Button(frame2,text="insert",bg='lightblue',height=2,width=12,font=5,command=insert_data)
     insert.place(x=690,y=500)
     
        

options.trace('w',my_show)




# Code to add widgets will go here...
#################################################
###############################################
###############################################3



#sql_table(con,'CREATE TABLE attendance(id int(5), date date , Samir varchar(4), Lana varchar(4), Harum varchar(4),  Fadu varchar(4) , Albert varchar(4) , Joseph varchar(4)) ;')

#print(pd.read_sql(con,'select * from attendance'))

def attendanceDATA():
    print(var1.get())
    sql_table(con,("insert into attendance (Samir, Lana , Harum ,  Fadu  , Albert, Joseph) values((?),(?),(?),(?),(?),(?)); ",(var1.get(),var2.get,var3.get(),var4.get(),var5.get(),var6.get())))

    

back = Button(frame3, text=' ← ',height=1,width=4,font=1.5, bg="lightyellow",command = lambda: show(frame1)) 
back.place(x=0,y=0)


name = Label(frame3, text = "Name:",font=25)
name.place(x=50,y=40)

state = Label(frame3, text = "Absent / Present",font=25)
state.place(x=550,y=40)


stud1 = Label(frame3, text = "Samir:",font=20)
stud1.place(x=60,y=80)


stud2 = Label(frame3, text = "Lana:",font=20)
stud2.place(x=60,y=140)


stud3 = Label(frame3, text = "Hakum:",font=20)
stud3.place(x=60,y=200)


stud4 = Label(frame3, text = "Fadu:",font=20)
stud4.place(x=60,y=260)

stud5 = Label(frame3, text = "Albert:",font=20)
stud5.place(x=60,y=320)

stud6 = Label(frame3, text = "Joseph:",font=20)
stud6.place(x=60,y=380)


c1 = Checkbutton(frame3,  variable = var1, bg='#070801' ,  \
                 onvalue = "p", offvalue = "a", height=1, \
                 width = 20 )
c1.place(x=550,y=80)
c1.deselect()

c2 = Checkbutton(frame3,  variable = var2, bg='#070801',\
                 onvalue = "p", offvalue = "a", height=1, \
                 width = 20)
c2.place(x=550,y=140)
c2.deselect()

c3 = Checkbutton(frame3,  variable = var3, bg='#070801', \
                 onvalue = "P", offvalue = "a", height=1, \
                 width = 20)
c3.place(x=550,y=200)
c3.deselect()


c4 = Checkbutton(frame3,  variable = var4, bg='#070801', \
                 onvalue = "P", offvalue = "a", height=1, \
                 width = 20)
c4.place(x=550,y=260)
c4.deselect()


c5 = Checkbutton(frame3,  variable = var5, bg='#070801', \
                 onvalue = "P", offvalue = "a", height=1, \
                 width = 20)
c5.place(x=550,y=320)
c5.deselect()

c6 = Checkbutton(frame3,  variable = var6, bg='#070801', \
                 onvalue = "P", offvalue = "a", height=1, \
                 width = 20)
c6.place(x=550,y=380)
c6.deselect()




submit = Button(frame3,text="Submit",bg='lightblue',height=2,width=20,font=5 , command = attendanceDATA) 
submit.place(x=550,y=500)









# function to change properties of button on hover 
def changeOnHover(button, colorOnHover, colorOnLeave): 

    # adjusting backgroung of the widget 
    # background on entering widget 
    button.bind("<Enter>", func=lambda e: button.config( 
            background=colorOnHover)) 

    # background color on leving widget 
    button.bind("<Leave>", func=lambda e: button.config( 
            background=colorOnLeave)) 










table = pd.read_sql("select admsn_no ,name,stream , exam , marks , english , informatics , chemistry , biology , physics  from marks where stream='s';",con)
table1 = pd.read_sql("select admsn_no ,name,stream , exam , marks , english , maths , chemistry , biology , physics  from marks where stream='s';",con)


table2= pd.read_sql("select admsn_no ,name,stream , exam , marks , english , informatics , economics , accountancy , business_studies from marks;",con)


table3= pd.read_sql("select admsn_no ,name,stream , exam , marks , english , maths , economics , accountancy , business_studies from marks;",con)


pd.option_context('display.max_rows', 400, 'display.max_columns', 9, 'display.expand_frame_repr', False)

#pd.set_option('display.max_columns', None)





sci_it = Button(frame4,text="Science + IT",height=2,width=20,font=5,command = lambda: show(frame5)) 
sci_it.place(x=310,y=100)


sci_math = Button(frame4,text="Science + Math",height=2,width=20,font=5,command = lambda: show(frame6)) 
sci_math.place(x=310,y=200)


com_it = Button(frame4,text="Commerce + IT",height=2,width=20,font=5,command = lambda: show(frame7)) 
com_it.place(x=310,y=300)




com_math = Button(frame4,text="Commerce + Math",height=2,width=20,font=5,command = lambda: show(frame8)) 
com_math.place(x=310,y=400)


insertMarks = Button(frame4,text="Insert Marks",bg='lightblue',height=2,width=12,font=5,command = lambda: show(frame2)) 
insertMarks.place(x=650,y=350)


stats = Button(frame4,text="Show Analytics",bg='lightblue',height=2,width=12,font=5,command = lambda: show(frame9)) 
stats.place(x=650,y=420)






#####################################


pt = Table(frame5, dataframe=table,showtoolbar=True, showstatusbar=True)
pt.place(x=100,y=200)
pt.show()

back1 = Button(frame5, text=' ← ',height=1,width=4,font=1.5, bg="yellow",command = lambda: show(frame4))
#back1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
back1.place(x=0,y=0)

changeOnHover(back1, "red", "aqua") 




pt = Table(frame6, dataframe=table1,showtoolbar=True, showstatusbar=True)
pt.place(x=100,y=200)
pt.show()

back2 = Button(frame6, text=' ← ',height=1,width=4,font=1.5, bg="yellow",command = lambda: show(frame4))
back2.place(x=0,y=0)


pt = Table(frame7, dataframe=table2,showtoolbar=True, showstatusbar=True)
pt.place(x=100,y=200)
pt.show()

back3 = Button(frame7, text=' ← ',height=1,width=4,font=1.5, bg="yellow",command = lambda: show(frame4))
back3.place(x=0,y=0)

pt = Table(frame8, dataframe=table3,showtoolbar=True, showstatusbar=True)
pt.place(x=100,y=200)
pt.show()

back4 = Button(frame8, text=' ← ',height=1,width=4,font=1.5, bg="yellow",command = lambda: show(frame4))
back4.place(x=0,y=0)





back = Button(frame4, text=' ← ',height=1,width=4,font=1.5, bg="yellow" ,command = lambda: show(frame1))
back.place(x=0,y=0)

pt.setColumnColors(cols=0, clr='red')
pt.setColumnColors(cols=[1, 2], clr='green')
pt.setColumnColors(cols=[-1], clr='#a0a0ff')

##########################################3 home ############

marksButton = Button(frame1,text="Marks",height=2,width=20,font=5,command = lambda: show(frame4)) 
marksButton.place(x=200,y=260)







attendanceButton = Button(frame1,text="Attendance",height=2,width=20,font=5,command = lambda: show(frame3)) 
attendanceButton.place(x=450,y=260)



 
#########################  Analytics ##############################
        
def statsData():
    print(pd.read_sql("select name, marks  from marks where exam = 'u1'  ;",con))
    
    print(pd.read_sql("select name, marks  from marks where  exam = 'u2'  ;",con))

     
    print(pd.read_sql("select name, marks  from marks where  exam = 't1' ;",con))

     
    print(pd.read_sql("select name, marks  from marks where  exam = 't2' ;",con))

     

     

    topScore = pd.DataFrame((pd.read_sql("select name, (sum(marks)/300)*100 as avg  from marks where (exam = 'u1' or exam = 'u2' or exam = 't1' or exam = 't2') group by name order by avg  ;",con)))
    print(topScore)

    
    bar = ppt.bar(topScore['name'],topScore['avg'])
    ppt.show()

    print(bar)

    

   

    




toppers = Label(frame9, text = "Top scoring students.",font=20)
toppers.place(x=60,y=160)




show1 = Button(frame9,text="Show",bg='lightblue',height=2,width=12,font=5,command = statsData) 
show1.place(x=270,y=160)





studentWISE = Button(frame9,text="Show student wise analytics ",bg='lightblue',height=2,width=26,font=5,command = lambda: show(frame10)) 
studentWISE.place(x=70,y=260)


back = Button(frame9, text=' ← ',height=1,width=4,font=1.5, bg="yellow" ,command = lambda: show(frame4))
back.place(x=0,y=0)




############################################   FRAME 10 #########################


     
def unitWiseMark(name,admsn):   
    u1_num = pd.read_sql("select  marks as u1  from marks where exam = 'u1' and ( name = (?) or admsn_no = (?));",con,params= (name,admsn))
    u1 = (pd.DataFrame(u1_num))
    print(u1['u1'] )

    u2_num = pd.read_sql("select  marks as u2  from marks where exam = 'u2' and ( name = (?) or admsn_no = (?));",con,params= (name,admsn))
    u2 = pd.DataFrame(u2_num)
    print(u2['u2'])
    

    t1_num = pd.read_sql("select  marks as t1  from marks where exam = 't1' and ( name = (?) or admsn_no = (?));",con,params= (name,admsn))
    t1 = pd.DataFrame(t1_num)
    print(t1['t1'])


    t2_num = pd.read_sql("select  marks as t2  from marks where exam = 't2' and  ( name = (?) or admsn_no = (?));",con,params= (name,admsn))
    t2 = pd.DataFrame(t2_num)
    print(t2['t2'])



    

    marks = [(int(u1['u1'])/50)*100 , (int(u2['u2'])/50)*100 , (int(t1['t1'])/100)*100 , (int(t2['t2'])/100)*100]
    unit = ['unit 1', 'unit2','term 1', 'term2']
    
    print('############################')
    

    print(marks)
    
 
    
    bar1 = ppt.bar(unit,marks)

    stud = pd.read_sql("select distinct name  from marks where  admsn_no = (?);",con,params= (admsn,))

    d1 = pd.DataFrame(stud)

 
    
    ppt.title(str(d1['name'].str.cat(sep='\n'))+ ' Marks')
    

    ppt.show()



    
    #print(pd.read_sql("select name exam , marks , english , informatics , chemistry , biology , physics from marks;",con))





back = Button(frame10, text=' ← ',height=1,width=4,font=1.5, bg="yellow" ,command = lambda: show(frame9))
back.place(x=0,y=0)

studentUnitWISE_label = Label(frame10, text = "student's unit wise marks analytics.",font=20)
studentUnitWISE_label.place(x=60,y=220)


    

    

adm = Label(frame10, text = "Admission no:",font=20)
adm.place(x=60,y=120)


global adm_no
adm_no = Entry(frame10,bd=1,width=25,font=20)
adm_no.place(x=180,y=120,height=30)



stud_name = Label(frame10, text = "Student's Name:",font=20)
stud_name.place(x=460,y=120)



global student_name
student_name = Entry(frame10,bd=1,width=25,font=20)
student_name.place(x=600,y=120,height=30)



studentUnitWISE = Button(frame10,text="Show",bg='lightblue',height=2,width=26,font=5,command = lambda: unitWiseMark(student_name.get(),adm_no.get())) 
studentUnitWISE.place(x=470,y=220)




###################################################


def unitSubjectWise(name,admsn,exam):

    if exam == 'u1':
        u1_sql = pd.read_sql("select admsn_no ,name,stream , exam , marks , english , informatics ,maths , chemistry , biology , physics , economics , accountancy , business_studies   from marks  where exam = 'u1' and ( name = (?) or admsn_no = (?));",con,params= (name,admsn))
    
    elif exam == 'u2':
        u1_sql = pd.read_sql("select admsn_no ,name,stream , exam , marks , english , informatics ,maths , chemistry , biology , physics , economics , accountancy , business_studies   from marks  where exam = 'u2' and ( name = (?) or admsn_no = (?));",con,params= (name,admsn))

    elif exam == 't1':
        u1_sql = pd.read_sql("select admsn_no ,name,stream , exam , marks , english , informatics ,maths , chemistry , biology , physics , economics , accountancy , business_studies   from marks  where exam = 't1' and ( name = (?) or admsn_no = (?));",con,params= (name,admsn))

    elif exam == 't2':
        u1_sql = pd.read_sql("select admsn_no ,name,stream , exam , marks , english , informatics ,maths , chemistry , biology , physics , economics , accountancy , business_studies   from marks  where exam = 't2' and ( name = (?) or admsn_no = (?));",con,params= (name,admsn))
        
       
    
    
    u1 = pd.DataFrame(u1_sql)

    if (u1['economics'].isnull().values.any() == True ) and (u1['maths'].isnull().values.any() == True)  :
         marks = [int(u1['english']), u1['informatics']  ,u1['chemistry'],u1['biology'] , u1['physics']  ]
         sub =  ['english' , 'informatics'  , 'chemistry' , 'biology' , 'physics' ]
    
         print('ti')

         

    elif (u1['economics'].isnull().values.any() == True ) and (u1['maths'].isnull().values.any() == False)  :
         marks = [int(u1['english']), u1['maths']  ,u1['chemistry'],u1['biology'] , u1['physics']  ]
         sub =  ['english' , 'maths'  , 'chemistry' , 'biology' , 'physics' , 'economics' ]
    
         print('ti')

         

    elif (u1['economics'].isnull().values.any() == False ) and (u1['maths'].isnull().values.any() == True)  :
         marks = [int(u1['english']), u1['informatics']   , u1['economics'] , u1['accountancy'], u1['business_studies'] ]
         sub =  ['english' , 'informatics'  , 'economics' , 'accountancy' , 'business_studies' ]
    
         print('ti')

         


    elif (u1['economics'].isnull().values.any() == False ) and (u1['maths'].isnull().values.any() == False)  :
         marks = [int(u1['english']), u1['maths']   , u1['economics'] , u1['accountancy'], u1['business_studies'] ]
         sub =  ['english' , 'maths'  , 'economics' , 'accountancy' , 'business_studies' ]
    
         print('ti')    
        
        

    #marks = [int(u1['english']), u1['informatics'] , u1['maths'] ,u1['chemistry'],u1['biology'] , u1['physics'] , u1['economics'] , u1['accountancy'], u1['business_studies'] ]
    print(marks)

    bar = ppt.bar(sub,marks)


    ppt.title(str(u1['name'].str.cat(sep='\n'))+ "'s " + exam + "  Marks")
    ppt.show()





subUnitWISE_label = Label(frame10, text = "student's subject wise marks analytics.",font=20)
subUnitWISE_label.place(x=60,y=320)


sub1UnitWISE = Button(frame10,text="Show",bg='lightblue',height=2,width=26,font=5,command = lambda: show(frame11)) 
sub1UnitWISE.place(x=470,y=320)

################################# Exam List #################3


back = Button(frame11, text=' ← ',height=1,width=4,font=1.5, bg="yellow" ,command = lambda: show(frame10))
back.place(x=0,y=0)

examU1 = Button(frame11,text="Unit 1",bg='lightblue',height=2,width=20,font=5,command = lambda: unitSubjectWise(student_name.get(),adm_no.get() , 'u1' )) 
examU1.place(x=350,y=200)


examU2 = Button(frame11,text="Unit 2",bg='lightblue',height=2,width=20,font=5,command = lambda: unitSubjectWise(student_name.get(),adm_no.get() , 'u2' )) 
examU2.place(x=350,y=300)


examT1 = Button(frame11,text="Term 1",bg='lightblue',height=2,width=20,font=5,command = lambda: unitSubjectWise(student_name.get(),adm_no.get() , 't1' )) 
examT1.place(x=350,y=400)


examT2 = Button(frame11,text="Term 2",bg='lightblue',height=2,width=20,font=5,command = lambda: unitSubjectWise(student_name.get(),adm_no.get() , 't2' ))  
examT2.place(x=350,y=500)




##################################################


def AllUnitsSubjectWise(name,admsn):

    
    u1_sql = pd.read_sql("select  english , informatics ,maths , chemistry , biology , physics , economics , accountancy , business_studies   from marks  where exam = 'u1' and ( name = (?) or admsn_no = (?));",con,params= (name,admsn))
    
    
    u2_sql = pd.read_sql("select  english , informatics ,maths , chemistry , biology , physics , economics , accountancy , business_studies   from marks  where exam = 'u2' and ( name = (?) or admsn_no = (?));",con,params= (name,admsn))

    
    t1_sql = pd.read_sql("select  english , informatics ,maths , chemistry , biology , physics , economics , accountancy , business_studies   from marks  where exam = 't1' and ( name = (?) or admsn_no = (?));",con,params= (name,admsn))

    
    t2_sql = pd.read_sql("select  english , informatics ,maths , chemistry , biology , physics , economics , accountancy , business_studies   from marks  where exam = 't2' and ( name = (?) or admsn_no = (?));",con,params= (name,admsn))
        
       
    
    
    u1D = pd.DataFrame(u1_sql)

    u1 = (u1D/50)*100

    u2D = pd.DataFrame(u2_sql)

    u2 = (u2D/50)*100

    t1D = pd.DataFrame(t1_sql)

    t1 = (t1D/100)*100

    t2D = pd.DataFrame(t2_sql)

    t2 = (t2D/100)*100

    

    if (u1['economics'].isnull().values.any() == True ) and (u1['maths'].isnull().values.any() == True)  :
         

         marks = [ [ int(u1['english']), int(u2['english']) , int(t1['english']) , int(t2['english'])            ],
                   [ int(u1['informatics'])            ,int(u2['informatics'])             ,int(t1['informatics'])             , int(t2['informatics'])      ],
                   [ int(u1['chemistry'])        ,int(u2['chemistry'])         ,int(t1['chemistry'])         ,int(t2['chemistry'])   ],
                   [ int(u1['biology'])      ,int(u2['biology'])       ,int(t1['biology'])       ,int(t2['biology']) ],
                   [ int(u1['physics']) , int(u2['physics']) ,int(t1['physics'])  , int(t2['physics']) ]]         
         
         sub =  ['english' , 'informatics'  , 'chemistry' , 'biology' , 'physics' ]

         it_mat = 'informatics'

         chem_eco = 'chemistry'

         bio_acct = 'biology'

         phy_busi = 'physics'
    
         print('ti')

         

    elif (u1['economics'].isnull().values.any() == True ) and (u1['maths'].isnull().values.any() == False)  :
        
         marks = [ [ int(u1['english']), int(u2['english']) , int(t1['english']) , int(t2['english'])            ],
                   [ int(u1['maths'])            ,int(u2['maths'])             ,int(t1['maths'])             , int(t2['maths'])      ],
                   [ int(u1['chemistry'])        ,int(u2['chemistry'])         ,int(t1['chemistry'])         ,int(t2['chemistry'])   ],
                   [ int(u1['biology'])      ,int(u2['biology'])       ,int(t1['biology'])       ,int(t2['biology']) ],
                   [ int(u1['physics']) , int(u2['physics']) ,int(t1['physics'])  , int(t2['physics']) ]]
         
         sub =  ['english' , 'maths'  , 'chemistry' , 'biology' , 'physics' , 'economics' ]


         it_mat = 'maths'

         chem_eco = 'chemistry'

         bio_acct = 'biology'

         phy_busi = 'physics'
    
    
         print('ti')

         

    elif (u1['economics'].isnull().values.any() == False ) and (u1['maths'].isnull().values.any() == True)  :
        
         marks = [ [ int(u1['english']), int(u2['english']) , int(t1['english']) , int(t2['english'])            ],
                   [ int(u1['informatics'])            , int(u2['informatics'])             , int(t1['informatics'])             , int(t2['informatics'])      ],
                   [ int(u1['economics'])        ,int(u2['economics'])         ,int(t1['economics'])         ,int(t2['economics'])   ],
                   [ int(u1['accountancy'])      ,int(u2['accountancy'])       ,int(t1['accountancy'])      ,int(t2['accountancy']) ],
                   [ int(u1['business_studies']) , int(u2['business_studies']) ,int(t1['business_studies'])  , int(t2['business_studies']) ]]


         sub =  ['english' , 'informatics'  , 'economics' , 'accountancy' , 'business_studies' ]

         it_mat = 'informatics'

         chem_eco = 'economics'

         bio_acct = 'accountancy'

         phy_busi = 'business studies'
    
    
         print('ti')

         


    elif (u1['economics'].isnull().values.any() == False ) and (u1['maths'].isnull().values.any() == False)  :
        

         marks = [ [ int(u1['english']), int(u2['english']) , int(t1['english']) , int(t2['english'])            ],
                   [ int(u1['maths'])            , int(u2['maths'])             , int(t1['maths'])             , int(t2['maths'])      ],
                   [ int(u1['economics'])        ,int(u2['economics'])         ,int(t1['economics'])         ,int(t2['economics'])   ],
                   [ int(u1['accountancy'])      ,int(u2['accountancy'])       ,int(t1['accountancy'])      ,int(t2['accountancy']) ],
                   [ int(u1['business_studies']) , int(u2['business_studies']) ,int(t1['business_studies'])  , int(t2['business_studies']) ]]

         sub =  ['english' , 'maths'  , 'economics' , 'accountancy' , 'business_studies' ]

         it_mat = 'maths'

         chem_eco = 'economics'

         bio_acct = 'accountancy'

         phy_busi = 'business studies'
    
         print('ti')


         
        
    u1 = pd.DataFrame(pd.read_sql("select distinct name  from marks where   name = (?) or admsn_no = (?);",con,params= (name,admsn)))
     

    #marks = [u1_marks, u2_marks , t1_marks , t2_marks]
    print(marks[0])
    print('#3')
    print(marks[1])
    print(marks[2])
    print(marks[3])
    print(marks[4])

    x = np.arange(4)

    ppt.figure(figsize=(10, 5))  # width:20, height:3

    #ppt.bar(sub,marks)

    barWidth = 0.16

    r1 = np.arange(len(marks[0]))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    r4 = [x + barWidth for x in r3]
    r5 = [x + barWidth for x in r4]
     

    
    


    ppt.bar(r1 , marks[0], color = 'b' , width = barWidth , label = 'English')

    ppt.bar(r2 , marks[1], color = 'r' , width = barWidth , label = it_mat)

    ppt.bar(r3 , marks[2], color = 'y' , width = barWidth , label = chem_eco)
    ppt.bar(r4 , marks[3], color = 'g' , width = barWidth , label = bio_acct)

    ppt.bar(r5 , marks[4], color = 'aqua' , width = barWidth , label  = phy_busi)

    ppt.ylim(0,100)

    ppt.xticks([r + barWidth for r in range(len(marks[0]))],['unit 1', 'unit 2' , 'term 1' , 'term 2' ])



    ppt.legend(loc = 'best')

    ppt.title(str(u1['name'].str.cat(sep='\n')) + "'s  Marks")
    ppt.show()

    






AllUnitWISE_label = Label(frame10, text = "student's subject wise marks analytics for all units.",font=20)
AllUnitWISE_label.place(x=60,y=420)


AllUnitWISE = Button(frame10,text="Show",bg='lightblue',height=2,width=26,font=5,command = lambda: AllUnitsSubjectWise(student_name.get(),adm_no.get())) 
AllUnitWISE.place(x=470,y=420)



gui.mainloop()
