import sqlite3

import pandas as pd

from sqlite3 import Error

from tkinter import *

import tkinter.font as tkFont


from pandastable import Table

from pandastable import images
from pandastable.dialogs import addButton

import matplotlib.pyplot as ppt

import sys

import numpy as np

import time






# note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
gui = Tk()
gui.geometry("1000x650")

gui.attributes("-alpha", 0.85)



gui.rowconfigure(0,weight=1)
gui.columnconfigure(0,weight=1)

def show(frame):
    frame.tkraise()




frame15 = Frame(gui,bg='#070801')
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
frame0 = Frame(gui,bg='#070801')




for frame in (frame15,frame14,frame13,frame12,frame11,frame10,frame9,frame8, frame7, frame6, frame5,frame4,frame3, frame2,frame1,frame0):
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

data = pd.read_sql("select id,name,exam,marks from marks ;",con)
#print(data)





def exec_data():
    sql_table(con,"select *  from marks; ")
    print(data)
    print(var1.get())
    print(var2.get())
    print(var3.get())
    print(pd.read_sql("select * from attendance ;",con))
##########################################3 home ############



    
fontStyle = tkFont.Font(family="Helvetica", size=18)

  
tms = Label(frame0, text = 'Students Transcript Management ',font= fontStyle ,bg='#070801' , fg = 'white')
tms.place(x=300,y=60)
    
class12 = Label(frame1,  text="Class: 12",font=('Sans',14) ,bg='#070801' , fg = 'white')
class12.place(x=825,y=60)



enter = Button(frame0,text="Enter    ❯",height=2,width=20,font=('Sans',16) , bg='lightblue' ,command = lambda: show(frame1)) 
enter.place(x=380,y=350, height = 65)




home = Button(frame1,text="⌂",width=5,font=15 ,command = lambda: show(frame0)) 
home.place(x=0,y=0)


marksButton = Button(frame1,text="Marks",height=2,width=20,bg='lightblue' ,font=5,command = lambda: show(frame4)) 
marksButton.place(x=250,y=260)







attendanceButton = Button(frame1,text="Attendance",height=2,width=20,bg='lightblue' ,font=5,command = lambda: show(frame3)) 
attendanceButton.place(x=500,y=260)






time1 = ''
time2 = time.strftime('%H:%M:%S')




watch = Label(frame1, text=time2, fg= 'white' ,font=('Sans',20,'bold'),height=2,width=10,  bg='#070801')
watch.place(x=800,y=120)



def changeLabel():
    if int(time.strftime('%H')) > int('12') :
        hour =  int(time.strftime('%H')) - 12
        
    time2 = time.strftime(str(hour) + ' : %M: %S')
    watch.configure(text=time2)
    frame1.after(200, changeLabel) #it'll call itself continuously



changeLabel() #first call it manually





############

# create label for current time
lbl = Label(frame0, text='Hello There' , font = ('Sans' , 26),bg='#070801' , fg = '#46e385')
lbl.place(x= 300 , y= 200)

# run `update_time` first time after 1000ms (1s)

#frame0.after(3000, update_txt) # function name without ()
#update_time() # or run first time immediately




test_string = "Hello there, Welcome back !!"
#Time delay between chars, in milliseconds
delta = 200 
delay = 0
for i in range(len(test_string) + 1):
    s = test_string[:i]
   
    update_text = lambda s=s: lbl.configure(text=s)
    frame0.after(delay, update_text)
    delay += delta

##############################################









back = Button(frame2, text=' ← ',height=1,width=4,font=1.5, bg="#46e385",command = lambda: show(frame4)) 
back.place(x=0,y=0)




adms_no = Label(frame2, text = "Admission no:",font=25,bg='#070801' , fg = 'white')
adms_no.place(x=50,y=40)


s_name = Label(frame2, text = "Name:",font=25 ,bg='#070801' , fg = 'white')
s_name.place(x=50,y=80)


stream = Label(frame2, text = "Stream:",font=25 ,bg='#070801' , fg = 'white')
stream.place(x=50,y=120)

exam = Label(frame2, text = "Exam:",font=25 ,bg='#070801' , fg = 'white')
exam.place(x=50,y=160)

marks = Label(frame2, text = "Marks:",font=25 ,bg='#070801' , fg = 'white')
marks.place(x=50,y=200)

english = Label(frame2, text = "English:",font=25 ,bg='#070801' , fg = 'white')
english.place(x=50,y=240)







my_list = ["Science / Commerce","Science + IT","Science + Math","Commerce + IT","Commerce + Math"]
options = StringVar(gui)
options.set(my_list[0]) # default value

e3 =OptionMenu(frame2, options, *my_list )
e3.place(x=350,y=120)



str_out= StringVar(gui)
str_out.set("Output")

l2 = Label(frame2,  textvariable=str_out, width=10 ,bg='#070801' , fg = 'white')  
l2.place(x=350,y=160) 




e1 = Entry(frame2,bd=1,width=30)
e1.place(x=350,y=40,height=30)

e2 = Entry(frame2,bd=1,width=30)
e2.place(x=350,y=80,height=30)






e4 = Entry(frame2,bd=1,width=30)
e4.place(x=350,y=160,height=30)


e5 = Entry(frame2,bd=1,width=30)
e5.place(x=350,y=200,height=30)

e6 = Entry(frame2,bd=1,width=30)
e6.place(x=350,y=240,height=30)



def it():
    global e7

    it = Label(frame2, text = "Informatics:",font=25 ,bg='#070801' , fg = 'white')
    it.place(x=50,y=280,height=30)

    e7 = Entry(frame2,bd=1,width=30)
    e7.place(x=350,y=280,height=30)

def math():
    global e8

    
    maths = Label(frame2, text = "Maths:",font=25  ,bg='#070801' , fg = 'white')
    maths.place(x=50,y=320,height=30)


    e8 = Entry(frame2,bd=1,width=30)
    e8.place(x=350,y=320,height=30)


def sci():

        
    chemistry = Label(frame2, text = "Chemistry:",font=25 ,bg='#070801' , fg = 'white')
    chemistry.place(x=50,y=360)


    biology = Label(frame2, text = "Biology:",font=25 ,bg='#070801' , fg = 'white')
    biology.place(x=50,y=400)


    physics = Label(frame2, text = "Physics:",font=25 ,bg='#070801' , fg = 'white')
    physics.place(x=50,y=440)


    global e9
    e9 = Entry(frame2,bd=1,width=30)
    e9.place(x=350,y=360,height=30)

    global e10
    e10 = Entry(frame2,bd=1,width=30)
    e10.place(x=350,y=400,height=30)

    global e11
    e11 = Entry(frame2,bd=1,width=30)
    e11.place(x=350,y=440,height=30)

def com():

        
    economics = Label(frame2, text = "Economics:",font=25 ,bg='#070801' , fg = 'white')
    economics.place(x=50,y=480)

    accountancy = Label(frame2, text = "Accountancy:",font=25 ,bg='#070801' , fg = 'white')
    accountancy.place(x=50,y=520)


    business = Label(frame2, text = "Business:",font=25,bg='#070801' , fg = 'white')
    business.place(x=50,y=560)



    global e12
    e12 = Entry(frame2,bd=1,width=30)
    e12.place(x=350,y=480,height=30)

    global e13    
    e13 = Entry(frame2,bd=1,width=30)
    e13.place(x=350,y=520,height=30)

    global e14
    e14 = Entry(frame2,bd=1,width=30)
    e14.place(x=350,y=560,height=30)




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



#sql_table(con,'CREATE TABLE attendance(id INTEGER PRIMARY KEY, date date , Samir varchar(4), Lana varchar(4), Harum varchar(4),  Fadu varchar(4) , Albert varchar(4) , Joseph varchar(4)) ;')

def attencance_plot():

    attend = pd.DataFrame(pd.read_sql('select * from attendance ;',con))


    attend_data = {'Samir' : attend.query('Samir == "a"').Samir.count() ,
                              'Lana' : attend.query('Lana == "a"').Lana.count()  ,
                              'Harum' : attend.query('Harum == "a"').Harum.count()  ,
                              'Fadu' : attend.query('Fadu == "a"').Fadu.count()  ,
                              'Albert' : attend.query('Albert == "a"').Albert.count() ,
                              'Joseph'  : attend.query('Joseph == "a"').Joseph.count() }

    attend_df = pd.DataFrame(attend_data, index = [0])

    attend_df = attend.id.count() - attend_df 

    print(attend_df)
    print(attend.id.count())

    names = ['Samir', 'Lana', 'Harum', 'Fadu' , 'Albert' , 'Joseph' ]

    values =  [int(attend_df.Samir) , int(attend_df.Lana) , int(attend_df.Harum) , int(attend_df.Fadu) , int(attend_df.Albert) , int(attend_df.Joseph)]


    print(values)
    ppt.bar(names, values)
    ppt.xlabel('Names')
    ppt.ylabel('Number of days')
    ppt.title('Students Attendance ')
    ppt.show()

#sql_table(con,"drop table attendance ; ")




def attendanceDATA():
    print(var1.get())
    
    cursorObj = con.cursor()

    cursorObj.execute("insert into attendance (date,Samir, Lana , Harum ,  Fadu  , Albert, Joseph) values( CURRENT_DATE,?,?, ?, ? , ? , ?); ",(var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get() )  )
        
   
     
    con.commit()

   

back = Button(frame3, text=' ← ',height=1,width=4,font=1.5 , bg="#46e385" ,command = lambda: show(frame1)) 
back.place(x=0,y=0)


name = Label(frame3, text = "Name:",font=25 ,bg='#070801' , fg = 'white')
name.place(x=50,y=40)

state = Label(frame3, text = "Absent / Present",font=25 ,bg='#070801' , fg = 'white')
state.place(x=550,y=40)


stud1 = Label(frame3, text = "Samir:",font=20 ,bg='#070801' , fg = 'white')
stud1.place(x=60,y=80)


stud2 = Label(frame3, text = "Lana:",font=20 ,bg='#070801' , fg = 'white')
stud2.place(x=60,y=140)


stud3 = Label(frame3, text = "Harum:",font=20 ,bg='#070801' , fg = 'white')
stud3.place(x=60,y=200)


stud4 = Label(frame3, text = "Fadu:",font=20 ,bg='#070801' , fg = 'white')
stud4.place(x=60,y=260)

stud5 = Label(frame3, text = "Albert:",font=20 ,bg='#070801' , fg = 'white')
stud5.place(x=60,y=320)

stud6 = Label(frame3, text = "Joseph:",font=20 ,bg='#070801' , fg = 'white')
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




sub1UnitWISE = Button(frame3,text="Analytics",bg='lightblue',height=2,width=12,font=3,command = attencance_plot) 
sub1UnitWISE.place(x=750,y=220)


updateData = Button(frame3,text="Update Data",bg='lightblue',height=2,width=12,font=5,command = lambda: show(frame13)) 
updateData.place(x=750,y=300)



deleteData = Button(frame3,text="Delete Data",bg='red',height=2,width=12,font=5,command = lambda: show(frame15)) 
deleteData.place(x=750,y=380)






#####################################################################################################33

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
insertMarks.place(x=650,y=220)


stats = Button(frame4,text="Show Analytics",bg='lightblue',height=2,width=12,font=5,command = lambda: show(frame9)) 
stats.place(x=650,y=280)

updateData = Button(frame4,text="Update Data",bg='lightblue',height=2,width=12,font=5,command = lambda: show(frame12)) 
updateData.place(x=650,y=340)


deleteData = Button(frame4,text="Delete Data",bg='red',height=2,width=12,font=5,command = lambda: show(frame14)) 
deleteData.place(x=650,y=400)





#####################################


pt = Table(frame5, dataframe=table,showtoolbar=True, showstatusbar=True)
pt.place(x=100,y=200)
pt.show()

back1 = Button(frame5, text=' ← ',height=1,width=4,font=1.5, bg="#46e385",command = lambda: show(frame4))
#back1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
back1.place(x=0,y=0)

changeOnHover(back1, "red", "aqua") 




pt = Table(frame6, dataframe=table1,showtoolbar=True, showstatusbar=True)
pt.place(x=100,y=200)
pt.show()

back2 = Button(frame6, text=' ← ',height=1,width=4,font=1.5    , bg="#46e385",command = lambda: show(frame4))
back2.place(x=0,y=0)


pt = Table(frame7, dataframe=table2,showtoolbar=True, showstatusbar=True)
pt.place(x=100,y=200)
pt.show()

back3 = Button(frame7, text=' ← ',height=1,width=4,font=1.5, bg="#46e385",command = lambda: show(frame4))
back3.place(x=0,y=0)

pt = Table(frame8, dataframe=table3,showtoolbar=True, showstatusbar=True)
pt.place(x=100,y=200)
pt.show()

back4 = Button(frame8, text=' ← ',height=1,width=4,font=1.5, bg="#46e385",command = lambda: show(frame4))
back4.place(x=0,y=0)





back = Button(frame4, text=' ← ',height=1,width=4,font=1.5, bg="#46e385" ,command = lambda: show(frame1))
back.place(x=0,y=0)

pt.setColumnColors(cols=0, clr='red')
pt.setColumnColors(cols=[1, 2], clr='green')
pt.setColumnColors(cols=[-1], clr='#a0a0ff')







 
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

    

   

    




toppers = Label(frame9, text = "Top scoring students.",font=20 ,bg='#070801' , fg = 'white')
toppers.place(x=60,y=160)




show1 = Button(frame9,text="Show",bg='lightblue',height=2,width=12,font=5,command = statsData) 
show1.place(x=270,y=160)





studentWISE = Button(frame9,text="Show student wise analytics ",bg='lightblue',height=2,width=26,font=5,command = lambda: show(frame10)) 
studentWISE.place(x=70,y=260)


back = Button(frame9, text=' ← ',height=1,width=4,font=1.5, bg="#46e385" ,command = lambda: show(frame4))
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





back = Button(frame10, text=' ← ',height=1,width=4,font=1.5, bg="#46e385" ,command = lambda: show(frame9))
back.place(x=0,y=0)

studentUnitWISE_label = Label(frame10, text = "student's unit wise marks analytics.",font=20 ,bg='#070801' , fg = 'white')
studentUnitWISE_label.place(x=60,y=220)


    

    

adm = Label(frame10, text = "Admission no:",font=20 ,bg='#070801' , fg = 'white')
adm.place(x=60,y=120)


global adm_no
adm_no = Entry(frame10,bd=1,width=25,font=20)
adm_no.place(x=180,y=120,height=30)



stud_name = Label(frame10, text = "Student's Name:",font=20 ,bg='#070801' , fg = 'white')
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





subUnitWISE_label = Label(frame10, text = "student's subject wise marks analytics.",font=20 , bg='#070801' , fg = 'white')
subUnitWISE_label.place(x=60,y=320)


sub1UnitWISE = Button(frame10,text="Show",bg='lightblue',height=2,width=26,font=5,command = lambda: show(frame11)) 
sub1UnitWISE.place(x=470,y=320)

################################# Exam List #################3


back = Button(frame11, text=' ← ',height=1,width=4,font=1.5, bg="#46e385" ,command = lambda: show(frame10))
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

    






AllUnitWISE_label = Label(frame10, text = "student's subject wise marks analytics for all units.",font=20 ,bg='#070801' , fg = 'white')
AllUnitWISE_label.place(x=60,y=420)


AllUnitWISE = Button(frame10,text="Show",bg='lightblue',height=2,width=26,font=5,command = lambda: AllUnitsSubjectWise(student_name.get(),adm_no.get())) 
AllUnitWISE.place(x=470,y=420)

#################################
####################
#################3



back = Button(frame12, text=' ← ',height=1,width=4,font=1.5, bg="#46e385" ,command = lambda: show(frame4))
back.place(x=0,y=0)
  
row = Label(frame12,  text="ID number:",font=25 ,bg='#070801' , fg = 'white')
row.place(x=350,y=20)


row_id = Entry(frame12,bd=1,width=30)
row_id.place(x=350,y=60,height=30)


column_list = ["select column","admsn_no","name","stream", "exam","marks","english","informatics","math", "chemistry", "biology"  , "physics", "economics" , "accountancy" , "business_studies"]
column_options = StringVar(gui)
column_options.set(column_list[0]) # default value

column = OptionMenu(frame12, column_options, *column_list)
column.place(x=350,y=120)



 

   
update1 = Label(frame12,  text="New value:",font=25 ,bg='#070801' , fg = 'white')
update1.place(x=350,y=200)

update_value = Entry(frame12,bd=1,width=30)
update_value.place(x=350,y=250,height=30)

   




def column_show(*args):
     str_out.set(column_options.get())

     cursorObj = con.cursor()
     
     


     qry = "update marks set " + column_options.get() +"= ? where id = ? ;"
 
     cursorObj.execute(qry,(update_value.get()  , row_id.get()     ))
     con.commit()


    


        

column_options.trace('w',column_show)


def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func

update = Button(frame12,text="Update",height=2,width=20,bg='lightblue' ,font=5,command = sequence(lambda: sql_table(con,"select * from marks;"), column_show )) 
update.place(x=350,y=400)









#########################3

 
back = Button(frame13, text=' ← ',height=1,width=4,font=1.5, bg="#46e385" ,command = lambda: show(frame3))
back.place(x=0,y=0)

row1 = Label(frame13,  text="ID number:",font=25 ,bg='#070801' , fg = 'white')
row1.place(x=350,y=20)


row_id1 = Entry(frame13,bd=1,width=30)
row_id1.place(x=350,y=60,height=30)


column_list1 = ["select column","id","date","Samir","Lana", "Harum","Fadu","Albert","Joseph"]
column_options1 = StringVar(gui)
column_options1.set(column_list1[0]) # default value

column1 = OptionMenu(frame13, column_options1, *column_list1)
column1.place(x=350,y=120)



 

   
newValue = Label(frame13,  text="New value:",font=25 ,bg='#070801' , fg = 'white')
newValue.place(x=350,y=200)

new_value = Entry(frame13,bd=1,width=30)
new_value.place(x=350,y=250,height=30)

   



print(data)

def column_show1(*args):
     str_out.set(column_options.get())

     cursorObj = con.cursor()
     
     


     qry = "update attendance set " + column_options1.get() +"= ? where id = ? ;"
 
     cursorObj.execute(qry,(new_value.get()  , row_id1.get()     ))
     con.commit()


     
     print(pd.read_sql("select * from attendance;",con))

    


        

column_options1.trace('w',column_show1)




updateA = Button(frame13,text="Update",height=2,width=20,bg='lightblue' ,font=5,command = sequence(lambda: print(pd.read_sql("select * from attendance;",con)), column_show1 )) 
updateA.place(x=350,y=400)



#########################################




back = Button(frame14, text=' ← ',height=1,width=4,font=1.5, bg="#46e385",command = lambda: show(frame4))
back.place(x=0,y=0)


  
row2 = Label(frame14,  text="ID number:",font=25 ,bg='#070801' , fg = 'white')
row2.place(x=350,y=100)


row_id2 = Entry(frame14,bd=1,width=30)
row_id2.place(x=350,y=150,height=30)



def deleteData():
    sql_table(con,"delete from marks where id = " +row_id2.get() + ";" )

updateA = Button(frame14,text="=Delete",height=2,width=20,bg='red' ,font=5,command = sequence( deleteData ,  lambda: print(pd.read_sql("select * from marks;",con)))) 
updateA.place(x=350,y=300)


############################################

back = Button(frame15, text=' ← ',height=1,width=4,font=1.5, bg="#46e385",command = lambda: show(frame3))
back.place(x=0,y=0)


  
row3 = Label(frame15,  text="ID number:",font=25 ,bg='#070801' , fg = 'white')
row3.place(x=350,y=100)


row_id3 = Entry(frame15,bd=1,width=30)
row_id3.place(x=350,y=150,height=30)



def deleteData():
    sql_table(con,"delete from attendance where id = " +row_id3.get() + ";" )

updateA1 = Button(frame15,text="Delete",height=2,width=20,bg='red' ,font=5,command = sequence( deleteData ,  lambda: print(pd.read_sql("select * from attendance;",con)))) 
updateA1.place(x=350,y=300)





gui.mainloop()
