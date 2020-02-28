        #USE PYTHON 2.7
#Steve Dubon
#December 13, 2017
#sdubon@terepmai.umd.edu

import Tkinter as tk
import ttk
import mysql.connector

LARGE_FONT=("Verdana", 12)
NORMAL_FONT=("Verdana", 10)
SMALL_FONT=("Verdana", 8)
#=======================================================================================================================
                                   #PYTHON AND MySQL CONNECTION
#=======================================================================================================================
conn=mysql.connector.connect(user='me',
                             password='me',
                             host='localhost',
                             database='test')

mycursor=conn.cursor()
#=======================================================================================================================
                                     #CLOSES MySQL CONNECTION
#=======================================================================================================================
def CloseConnection():
    conn.close()
#=======================================================================================================================
                        #FUNCTIONS FOR THE "About..." MENU CASCADE OPTIONS
#=======================================================================================================================
def AboutUs():
    popup = tk.Tk()
    popup.wm_title("Contact Us")

    label = tk.Label(popup, text="Programmer's Information:", font=NORMAL_FONT)
    label.grid(row=0, column=0, sticky="NW")

    label1 = ttk.Label(popup, text="\nName: Steve Dubon", font=SMALL_FONT)
    label1.grid(row=1, column=0, sticky="NW")
    label2 = ttk.Label(popup, text="Email: sdubon@terpmail.umd.edu", font=SMALL_FONT)
    label2.grid(row=2, column=0, sticky="NW")
    label3 = ttk.Label(popup, text="Class: Inst326", font=SMALL_FONT)
    label3.grid(row=3, column=0, sticky="NW")
    label4 = ttk.Label(popup, text="Professor: Timothy Richards", font=SMALL_FONT)
    label4.grid(row=4, column=0, sticky="NW")
    label5 = ttk.Label(popup, text="Assignment: Individual Final Project", font=SMALL_FONT)
    label5.grid(row=5, column=0, sticky="NW")

    popup.geometry("500x400")
    popup.mainloop()
#-----------------------------------------------------------------------------------------------------------------------
def Instructions():
    popup = tk.Tk()
    popup.wm_title("Instructions")

    label = tk.Label(popup, text="How To Use The Program:", font=NORMAL_FONT)
    label.grid(row=0, column=0, sticky="NW")

    label1 = ttk.Label(popup, text="Step 1: Create an account. Make sure you remember your User ID.", font=SMALL_FONT)
    label1.grid(row=1, column=0, sticky="NW")
    label2 = ttk.Label(popup, text="\nStep 2: Check the flight list. Make sure you remember the Flight ID.", font=SMALL_FONT)
    label2.grid(row=2, column=0, sticky="NW")
    label3 = ttk.Label(popup, text="\nStep 3: Purchase a tickets. Make sure you use your user ID and the flight's ID. "
                                   "\nKeep the transaction ID and plane's ID", font=SMALL_FONT)
    label3.grid(row=3, column=0, sticky="NW")
    label4 = ttk.Label(popup, text="\nStep 4: You can start using the other features.", font=SMALL_FONT)
    label4.grid(row=4, column=0, sticky="NW")
    label5 = ttk.Label(popup, text="\nStep 5: Log-in to your account to see your transactions history.", font=SMALL_FONT)
    label5.grid(row=5, column=0, sticky="NW")
    label6 = ttk.Label(popup, text="\nStep 6: Close the program.", font=SMALL_FONT)
    label6.grid(row=6, column=0, sticky="NW")

    popup.geometry("500x400")
    popup.mainloop()
#-----------------------------------------------------------------------------------------------------------------------
def QuestionsAnswers():
    popup = tk.Tk()
    popup.wm_title("Frequent Q/As")

    label = tk.Label(popup, text="Frequent Q/As:", font=NORMAL_FONT)
    label.grid(row=0, column=0, sticky="NW")

    label1 = ttk.Label(popup, text="Question 1: How do I use the Program?", font=SMALL_FONT)
    label1.grid(row=1, column=0, sticky="NW")
    label2 = ttk.Label(popup, text="Answer 1: Refer to the instructions menu option.", font=SMALL_FONT)
    label2.grid(row=2, column=0, sticky="NW")
    label3 = ttk.Label(popup, text="\nQuestion 2: What's the Information I need?", font=SMALL_FONT)
    label3.grid(row=3, column=0, sticky="NW")
    label4 = ttk.Label(popup, text="Answer 2: Always Keep your User_ID and Transaction ID.", font=SMALL_FONT)
    label4.grid(row=4, column=0, sticky="NW")
    label5 = ttk.Label(popup, text="\nQuestion 3: I forgot my password, what do I do?", font=SMALL_FONT)
    label5.grid(row=5, column=0, sticky="NW")
    label6 = ttk.Label(popup, text="Answer 3: Go to Customers and click on 'Forgot Password?'", font=SMALL_FONT)
    label6.grid(row=6, column=0, sticky="NW")
    label7 = ttk.Label(popup, text="\nQuestion 4: Why am I not getting an output?", font=SMALL_FONT)
    label7.grid(row=7, column=0, sticky="NW")
    label8 = ttk.Label(popup, text="Answer 4: Your ID information is wrong. Please refer back to correct information and"
                                   "\ntry again.", font=SMALL_FONT)
    label8.grid(row=8, column=0, sticky="NW")
    label9 = ttk.Label(popup, text="\nQuestion 5: I cannot log in from the cascade menu option.", font=SMALL_FONT)
    label9.grid(row=9, column=0, sticky="NW")
    label10 = ttk.Label(popup, text="Answer 5: We are aware of the situation. Our developing team is working hard to fix"
                                    "\nthis issue."
                                    "But, you can always log-in from the home page. That option works fine", font=SMALL_FONT)
    label10.grid(row=10, column=0, sticky="NW")

    popup.geometry("500x400")
    popup.mainloop()
#=======================================================================================================================
                              #FUNCTIONS FOR THE "Customers" MENU CASCADE OPTIONS
#=======================================================================================================================
def menuCreateAccount():
    popup = tk.Tk()
    popup.wm_title("Create an Account")

    def SQLConnection():
        Fname = entry2.get()
        Lname = entry3.get()
        PW = entry4.get()
        EM = entry5.get()
        #print(Fname, Lname, PW, EM)

        mycursor.execute("INSERT INTO accounts VALUES(default,'%s','%s','%s','%s')" % (Fname, Lname, PW, EM))
        conn.commit()
        # controller.show_frame(PageThree)

        mycursor.execute("SELECT * FROM accounts WHERE Password='%s' AND First_Name='%s' AND Last_Name='%s'" % (PW, Fname, Lname))
        information = (mycursor.fetchall())
        #print information

        for item in information:
            User_Email = "\nUser Email: " + str(item[4])
            text1.insert(0.5, User_Email)
            # print str(item[1])
            User_Password = "\nUser Password: " + str(item[3])
            text1.insert(0.4, User_Password)
            Last_Name = "\nUser Last Name: " + str(item[2])
            text1.insert(0.3, Last_Name)
            First_Name = "\nUser First Name: " + str(item[1])
            text1.insert(0.2, First_Name)
            User_ID = "\nUser ID: " + str(item[0])
            text1.insert(0.1, User_ID)
            message1 = "Congratulation! You've Created an Account"
            text1.insert(0.0, message1)

    label = tk.Label(popup, text="Create an Account:", font=NORMAL_FONT)
    # label.pack(pady=10, padx=10)
    label.grid(row=0, column=1, sticky="nsew")

    label2 = ttk.Label(popup, text="First Name:", font=SMALL_FONT)
    label2.grid(row=2, column=0, sticky="NW")
    entry2 = ttk.Entry(popup)
    entry2.grid(row=2, column=1, sticky="NW")
    label3 = ttk.Label(popup, text="Last Name:", font=SMALL_FONT)
    label3.grid(row=3, column=0, sticky="NW")
    entry3 = ttk.Entry(popup)
    entry3.grid(row=3, column=1, sticky="NW")
    label4 = ttk.Label(popup, text="Password:", font=SMALL_FONT)
    label4.grid(row=4, column=0, sticky="NW")
    entry4 = ttk.Entry(popup)
    entry4.grid(row=4, column=1, sticky="NW")
    label5 = ttk.Label(popup, text="Email:", font=SMALL_FONT)
    label5.grid(row=5, column=0, sticky="NW")
    entry5 = ttk.Entry(popup)
    entry5.grid(row=5, column=1, sticky="NW")

    button1 = ttk.Button(popup, text="Create", command=lambda: SQLConnection())
    #button1.pack()
    button1.grid(row=6, column=1, sticky="NW")

    text1 = tk.Text(popup, width=50, height=15, font=SMALL_FONT)
    text1.grid(row=7, column=1, sticky="NE")

    button2 = ttk.Button(popup, text="Exit", command=lambda: popup.destroy())
    #button2.pack()
    button2.grid(row=8, column=1, sticky="NE")

    popup.geometry("500x400")
    popup.mainloop()
#-----------------------------------------------------------------------------------------------------------------------
def LogInInformation():
    popup = tk.Tk()
    popup.wm_title("Log In")

    label6 = ttk.Label(popup, text="Log In:", font=NORMAL_FONT)
    label6.grid(row=0, column=2, sticky="nsew")

    UserEmail = tk.StringVar()
    UserID = tk.StringVar()

    def LogInformation():
        UE = UserEmail.get()
        UID = UserID.get()

        mycursor.execute("SELECT * FROM transaction WHERE User_ID='%s' " % (UID))
        information = (mycursor.fetchall())
        print information

        for item in information:
            User_Email = "\nPlane's ID: " + str(item[5])
            text1.insert(0.5, User_Email)
            # print str(item[1])
            User_Password = "\nTicket's Arrival Destination: " + str(item[4])
            text1.insert(0.4, User_Password)
            Last_Name = "\nTicket's Departure Destination: " + str(item[3])
            text1.insert(0.3, Last_Name)
            First_Name = "\nPassenger Name: " + str(item[2])
            text1.insert(0.2, First_Name)
            User_ID = "\nTransaction ID: " + str(item[0])
            text1.insert(0.1, User_ID)
            message1 = "TRANSACTION HISTORY:"
            text1.insert(0.0, message1)

    label7 = ttk.Label(popup, text="User Email:", font=SMALL_FONT)
    label7.grid(row=2, column=0, sticky="NW")
    entry7 = ttk.Entry(popup, textvariable=UserEmail)
    entry7.grid(row=2, column=1, sticky="NW")
    label8 = ttk.Label(popup, text="User ID Number:", font=SMALL_FONT)
    label8.grid(row=3, column=0, sticky="NW")
    entry8 = ttk.Entry(popup, textvariable=UserID)
    entry8.grid(row=3, column=1, sticky="NW")

    UE = entry7.get()
    UID = entry8.get()

    button1 = ttk.Button(popup, text="Log In", command=lambda: LogInformation())
    # button2.pack()
    button1.grid(row=4, column=1, sticky="NW")

    text1 = tk.Text(popup, width=50, height=15, font=SMALL_FONT)
    text1.grid(row=5, column=1, columnspan=3, sticky="NW")

    button2 = ttk.Button(popup, text="Exit", command=lambda: popup.destroy())
    #button2.pack()
    button2.grid(row=8, column=1, sticky="NE")

    mycursor.execute("SELECT * FROM transaction WHERE User_ID='%s' " % (UID))
    information = (mycursor.fetchall())
    # print information

    for item in information:
        User_Email = "\nPlane's ID: " + str(item[5])
        text1.insert(0.5, User_Email)
        # print str(item[1])
        User_Password = "\nTicket's Arrival Destination: " + str(item[4])
        text1.insert(0.4, User_Password)
        Last_Name = "\nTicket's Departure Destination: " + str(item[3])
        text1.insert(0.3, Last_Name)
        First_Name = "\nPassenger Name: " + str(item[2])
        text1.insert(0.2, First_Name)
        User_ID = "\nTransaction ID: " + str(item[0])
        text1.insert(0.1, User_ID)
        message1 = "TRANSACTION HISTORY:"
        text1.insert(0.0, message1)

    popup.geometry("500x400")
    popup.mainloop()
#-----------------------------------------------------------------------------------------------------------------------
def InfoRetrival():
    popup = tk.Tk()
    popup.wm_title("Retrieve Information")

    def SQLConnection():
        UID = entry2.get()
        EM = entry3.get()
        #print(UID, EM)

        #mycursor.execute("INSERT INTO accounts VALUES(default,'%s','%s','%s','%s')" % (PW, EM))
        #conn.commit()
        # controller.show_frame(PageThree)

        mycursor.execute("SELECT * FROM accounts WHERE User_ID='%s' AND Email='%s'" % (UID, EM))
        #conn.commit()
        information = (mycursor.fetchall())
        #print(information)

        for item in information:
            User_Email = "\nUser Email: " + str(item[4])
            text1.insert(0.5, User_Email)
            # print str(item[1])
            User_Password = "\nUser Password: " + str(item[3])
            text1.insert(0.4, User_Password)
            Last_Name = "\nUser Last Name: " + str(item[2])
            text1.insert(0.3, Last_Name)
            First_Name = "\nUser First Name: " + str(item[1])
            text1.insert(0.2, First_Name)
            User_ID = "\nUser ID: " + str(item[0])
            text1.insert(0.1, User_ID)
            message1 = "YOUR USER INFORMATION IS:"
            text1.insert(0.0, message1)

    label = tk.Label(popup, text="Forgot Your User Information?", font=NORMAL_FONT)
    # label.pack(pady=10, padx=10)
    label.grid(row=0, column=1, sticky="nsew")

    label2 = ttk.Label(popup, text="User ID Number:", font=SMALL_FONT)
    label2.grid(row=2, column=0, sticky="NW")
    entry2 = ttk.Entry(popup)
    entry2.grid(row=2, column=1, sticky="NW")
    label3 = ttk.Label(popup, text="User Email:", font=SMALL_FONT)
    label3.grid(row=3, column=0, sticky="NW")
    entry3 = ttk.Entry(popup)
    entry3.grid(row=3, column=1, sticky="NW")


    button1 = ttk.Button(popup, text="Retrieve", command=lambda: SQLConnection())
    button1.pack()
    button1.grid(row=6, column=1, sticky="NW")

    text1 = tk.Text(popup, width=50, height=15, font=SMALL_FONT)
    text1.grid(row=7, column=1, sticky="NE")

    button2 = ttk.Button(popup, text="Exit", command=lambda: popup.destroy())
    #button2.pack()
    button2.grid(row=8, column=1, sticky="NE")

    popup.geometry("500x400")
    popup.mainloop()
#-----------------------------------------------------------------------------------------------------------------------
def ChangeAccountInfo():
    popup = tk.Tk()
    popup.wm_title("Change Account Information")

    label = tk.Label(popup, text="Change Your Information", font=NORMAL_FONT)
    label.grid(row=0, column=1, sticky="NW")

    label2 = ttk.Label(popup, text="User's ID:", font=SMALL_FONT)
    label2.grid(row=2, column=0, sticky="NW")
    entry2 = ttk.Entry(popup)
    entry2.grid(row=2, column=1, sticky="NW")

    label3 = ttk.Label(popup, text="New First Name:", font=SMALL_FONT)
    label3.grid(row=3, column=0, sticky="NW")
    entry3 = ttk.Entry(popup)
    entry3.grid(row=3, column=1, sticky="NW")

    label4 = ttk.Label(popup, text="New Last Name:", font=SMALL_FONT)
    label4.grid(row=4, column=0, sticky="NW")
    entry4 = ttk.Entry(popup)
    entry4.grid(row=4, column=1, sticky="NW")

    label5 = ttk.Label(popup, text="New Password:", font=SMALL_FONT)
    label5.grid(row=5, column=0, sticky="NW")
    entry5 = ttk.Entry(popup)
    entry5.grid(row=5, column=1, sticky="NW")

    label6 = ttk.Label(popup, text="New Email:", font=SMALL_FONT)
    label6.grid(row=6, column=0, sticky="NW")
    entry6 = ttk.Entry(popup)
    entry6.grid(row=6, column=1, sticky="NW")

    text1 = tk.Text(popup, width=50, height=15, font=SMALL_FONT)
    text1.grid(row=8, column=1, columnspan=3, sticky="nsew")

    button1 = ttk.Button(popup, text="Change", command=lambda: Update())
    button1.grid(row=7, column=1, sticky="nsew")

    button2 = ttk.Button(popup, text="Exit", command=lambda: popup.destroy())
    #button2.pack()
    button2.grid(row=9, column=1, sticky="NE")

    def Update():
        UID = entry2.get()
        Fname = entry3.get()
        Lname = entry4.get()
        PW = entry5.get()
        EM = entry6.get()

        mycursor.execute("UPDATE accounts SET First_Name='%s', Last_Name='%s', Password='%s', Email='%s' WHERE User_ID='%s'" % (Fname, Lname, PW, EM, UID))
        conn.commit()

        message = "Success! You've changed your account information."
        text1.insert(0.3, message)

    popup.geometry("500x400")
    popup.mainloop()
#=======================================================================================================================
                                  #FUNCTIONS FOR THE "Flights" MENU CASCADE OPTIONS
#=======================================================================================================================
def FlightsOptions():
    popup = tk.Tk()
    popup.wm_title("Flights")

    def LookUp():
        FID=var.get()
        mycursor.execute("SELECT * FROM flights WHERE To_Destination='%s'" % (FID))
        # conn.commit()
        information = (mycursor.fetchall())
        #print(information)
        #print var.get()
        #popup.quit()

        for item in information:
            Total_Seats = "\nTotal Seats: " + str(item[8])
            text1.insert(0.7, Total_Seats)
            Duration = "\nDuration: " + str(item[6])
            text1.insert(0.6, Duration)
            Time_Arrival = "\nArrival Time: " + str(item[5])
            text1.insert(0.5, Time_Arrival)
            # print str(item[1])
            Time_Departure = "\nDeparture Time: " + str(item[4])
            text1.insert(0.4, Time_Departure)
            To_Destination = "\nArrival Destination: " + str(item[2])
            text1.insert(0.3, To_Destination)
            From_Destination = "\nDeparture Destination: " + str(item[1])
            text1.insert(0.2, From_Destination)
            Flight_ID = "\nFlight's ID: " + str(item[0])
            text1.insert(0.1, Flight_ID)
            message1 = "Flight's Information"
            text1.insert(0.0, message1)

    label = tk.Label(popup, text="Choose a Flight", font=NORMAL_FONT)
    label.pack(pady=10, padx=10)
    #label.grid(row=0, column=1, sticky="nsew")

    var = tk.StringVar(popup)
    var.set("Flights")
    #print(var)

    option = ttk.OptionMenu(popup, var, "Flight's Destination:", "Florida", "Texas", "Washington DC", "Maryland")
    #option.grid(row=1, column=1, sticky="nsew")
    option.pack()

    button = ttk.Button(popup, text="Look Up", command=LookUp)
    #button.grid(row=2, column=1, sticky="nsew")
    button.pack()

    text1 = tk.Text(popup, width=50, height=15, font=SMALL_FONT)
    #text1.grid(row=3, column=1, sticky="nsew")
    text1.pack()

    button2 = ttk.Button(popup, text="Purchase Ticket", command=lambda: TicketPurchase())
    #button.grid(row=2, column=1, sticky="nsew")
    button2.pack()

    popup.geometry("500x400")
    popup.mainloop()
#-----------------------------------------------------------------------------------------------------------------------
def CheckIn():
    popup = tk.Tk()
    popup.wm_title("Check In")

    def LookUp():
        UID = entry1.get()
        FID = entry2.get()
        #print(UID, FID)

        mycursor.execute("SELECT * FROM transaction WHERE User_ID='%s' " % (UID))
        information = (mycursor.fetchall())
        #print information

        mycursor.execute("SELECT * FROM flights WHERE Flight_ID='%s'" % (FID))
        information1 = (mycursor.fetchall())
        #print information1

        for item in information1:
            To = "\nTo: " + str(item[2])
            text1.insert(0.3, To)
            From = "\nFrom: " + str(item[1])
            text1.insert(0.2, From)

        for item in information:
            PName = "\nPassenger:" + str(item[2])
            text1.insert(0.0, PName)

    label = tk.Label(popup, text="Check In", font=NORMAL_FONT)
    label.grid(row=0, column=2, sticky="NW")

    label1 = ttk.Label(popup, text="User ID:", font=SMALL_FONT)
    label1.grid(row=1, column=0, sticky="NW")
    entry1 = ttk.Entry(popup)
    entry1.grid(row=1, column=1, sticky="NW")
    label2 = ttk.Label(popup, text="Flight's ID:", font=SMALL_FONT)
    label2.grid(row=2, column=0, sticky="NW")
    entry2 = ttk.Entry(popup)
    entry2.grid(row=2, column=1, sticky="NW")

    button1 = ttk.Button(popup, text="Check In", command=lambda: LookUp())
    button1.grid(row=3, column=1, sticky="nsew")

    text1 = tk.Text(popup, width=50, height=15, font=SMALL_FONT)
    text1.grid(row=4, column=1, columnspan=75, sticky="nsew")

    button2 = ttk.Button(popup, text="Exit", command=lambda: popup.destroy())
    button2.grid(row=8, column=1, sticky="NE")

    popup.geometry("500x400")
    popup.mainloop()
#-----------------------------------------------------------------------------------------------------------------------
def FlightStatus():
    popup = tk.Tk()
    popup.wm_title("Flight's Status")

    def LookUp():
        FID = entry1.get()
        #print(FID)

        mycursor.execute("SELECT * FROM flights WHERE Flight_ID='%s' " % (FID))
        information = (mycursor.fetchall())
        #print information

        for item in information:
            SOpen = "\nSeats Open: " + str(item[9])
            text1.insert(0.3, SOpen)
            STotal = "\nTotal Seats: " + str(item[8])
            text1.insert(0.2, STotal)
            Duration = "\nFlight's Duration: " + str(item[6])
            text1.insert(0.1, Duration)
            FStatus = "Flight's Status: " + str(item[7])
            text1.insert(0.0, FStatus)


    label = tk.Label(popup, text="Check Flight's Status", font=NORMAL_FONT)
    label.grid(row=0, column=2, sticky="NW")

    label1 = ttk.Label(popup, text="Flights ID:", font=SMALL_FONT)
    label1.grid(row=1, column=0, sticky="NW")
    entry1 = ttk.Entry(popup)
    entry1.grid(row=1, column=1, sticky="NW")

    button1 = ttk.Button(popup, text="Check In", command=lambda: LookUp())
    button1.grid(row=2, column=1, sticky="nsew")

    text1 = tk.Text(popup, width=50, height=15, font=SMALL_FONT)
    text1.grid(row=3, column=1, columnspan=3, sticky="nsew")

    button2 = ttk.Button(popup, text="Exit", command=lambda: popup.destroy())
    button2.grid(row=8, column=1, sticky="NE")

    popup.geometry("500x400")
    popup.mainloop()
#-----------------------------------------------------------------------------------------------------------------------
def PlanesInformation():
    popup = tk.Tk()
    popup.wm_title("Plane's Information")

    label = tk.Label(popup, text="Plane's Information", font=NORMAL_FONT)
    label.grid(row=0, column=2, sticky="NW")

    label1 = ttk.Label(popup, text="Plane's ID Number:", font=SMALL_FONT)
    label1.grid(row=1, column=0, sticky="NW")
    entry1 = ttk.Entry(popup)
    entry1.grid(row=1, column=1, sticky="NW")

    def LookUp():
        PID = entry1.get()
        # print(TID)

        mycursor.execute("SELECT * FROM planes WHERE Plane_ID='%s'" % (PID))
        information = (mycursor.fetchall())
        # mycursor.fetchall()
        # print information

        for item in information:
            PType = "\nPlane's Type: " + str(item[2])
            text1.insert(0.1, PType)
            AName = "Airline Name: " + str(item[1])
            text1.insert(0.0, AName)

    button1 = ttk.Button(popup, text="Look Up", command=lambda: LookUp())
    button1.grid(row=2, column=1, sticky="nsew")

    text1 = tk.Text(popup, width=50, height=15, font=SMALL_FONT)
    text1.grid(row=3, column=1, columnspan=3, sticky="nsew")

    button2 = ttk.Button(popup, text="Exit", command=lambda: popup.destroy())
    button2.grid(row=8, column=1, sticky="NE")

    popup.geometry("500x400")
    popup.mainloop()
#=======================================================================================================================
                                #FUNCTIONS FOR THE "Ticket" MENU CASCADE OPTIONS
#=======================================================================================================================
def TicketPurchase():
    popup = tk.Tk()
    popup.wm_title("Purchase Ticket")

    v = tk.StringVar(popup)
    #var.set("Flights")
    #print(var)

    def LookUp():
        FID = entry2.get()
        Type = v.get()
        #print(FID, Type)

        mycursor.execute("SELECT * FROM tickets WHERE Flight_ID='%s' AND Ticket_Type='%s'" % (FID, Type))
        information = (mycursor.fetchall())
        #print information

        mycursor.execute("SELECT * FROM flights WHERE Flight_ID='%s'" % (FID))
        information1 = (mycursor.fetchall())
        #print information1

        for item in information1:
            Duration = "\nFlight's Duration: " + str(item[6])
            text1.insert(0.10, Duration)
            DTime = "\nDeparture Time: " + str(item[4])
            text1.insert(0.8, DTime)
            ATime = "\nArrival Time: " + str(item[5])
            text1.insert(0.9, ATime)
            From = "\nDeparture Destination: " + str(item[1])
            text1.insert(0.5, From)
            To = "\nArrival Destination: " + str(item[2])
            text1.insert(0.6, To)
            PlaneID = "\nPlane's ID: " + str(item[3])
            text1.insert(0.7, PlaneID)

        for item in information:
            Flight_ID = "\nFlight's ID: " + str(item[1])
            text1.insert(0.2, Flight_ID)
            Ticket_ID = "\nTicket's ID: " + str(item[0])
            text1.insert(0.1, Ticket_ID)
            Ticket_Type = "\nTicket's Class: " + str(item[2])
            text1.insert(0.3, Ticket_Type)
            Price = "\nPrice: " + str(item[3])
            text1.insert(0.4, Price)
            message1 = "TICKET'S INFORMATION"
            text1.insert(0.0, message1)

    def Purchase():
        UID = entry1.get()
        FID = entry2.get()
        PN = entry3.get()

        mycursor.execute("SELECT * FROM transaction WHERE User_ID='%s' AND Passenger_Name='%s'" % (UID, PN))
        information3 = (mycursor.fetchall())
        #print information3

        mycursor.execute("SELECT * FROM flights WHERE Flight_ID='%s'" % (FID))
        information4 = (mycursor.fetchall())

        for item in information4:
            FDestination=str(item[1])
            TDestination=str(item[2])
            PlaneID=str(item[3])

            mycursor.execute("INSERT INTO transaction VALUES(default,'%s','%s','%s','%s','%s')" % (UID, PN, FDestination,TDestination, PlaneID))
            conn.commit()

            mycursor.execute("SELECT * FROM transaction WHERE User_ID='%s' AND Passenger_Name='%s'" % (UID, PN))
            information5 = (mycursor.fetchall())

            for items in information5:
                Price = "\n Transaction Number: " + str(items[0])
                text1.insert(13.4, Price)
                message1 = "\nCONFIRMED!"
                text1.insert(12.0, message1)

    label = tk.Label(popup, text="Purchase A Ticket", font=NORMAL_FONT)
    label.grid(row=0, column=2, sticky="NW")

    label1 = ttk.Label(popup, text="User ID:", font=SMALL_FONT)
    label1.grid(row=2, column=0, sticky="NW")
    entry1 = ttk.Entry(popup)
    entry1.grid(row=2, column=1, sticky="NW")
    label2 = ttk.Label(popup, text="Flight's ID:", font=SMALL_FONT)
    label2.grid(row=3, column=0, sticky="NW")
    entry2 = ttk.Entry(popup)
    entry2.grid(row=3, column=1, sticky="NW")
    label3 = ttk.Label(popup, text="Passenger's Name:", font=SMALL_FONT)
    label3.grid(row=4, column=0, sticky="NW")
    entry3 = ttk.Entry(popup)
    entry3.grid(row=4, column=1, sticky="NW")

    label4 = tk.Label(popup, text="Ticket Type:", font=NORMAL_FONT)
    label4.grid(row=5, column=0, sticky="NW")
    RButton1=ttk.Radiobutton(popup, text="First Class", value="first", variable=v, command=LookUp())
    RButton1.grid(row=6, column=1, sticky="NW")
    RButton2=ttk.Radiobutton(popup, text="Business Class", value="business",  variable=v, command=LookUp())
    RButton2.grid(row=7, column=1, sticky="NW")
    RButton3=ttk.Radiobutton(popup, text="Economy Class", value="economy",  variable=v, command=LookUp())
    RButton3.grid(row=8, column=1, sticky="NW")

    button1 = ttk.Button(popup, text="Purchase Ticket", command=lambda: LookUp())
    button1.grid(row=9, column=1, sticky="nsew")

    text1 = tk.Text(popup, width=50, height=15, font=SMALL_FONT)
    text1.grid(row=10, column=1, columnspan=3, sticky="nsew")

    button2 = ttk.Button(popup, text="Confirm", command=lambda: Purchase())
    button2.grid(row=11, column=1, sticky="nsew")

    popup.geometry("550x450")
    popup.mainloop()
#-----------------------------------------------------------------------------------------------------------------------
def CancelTicket():
    popup = tk.Tk()
    popup.wm_title("Cancel Flight")

    def LookUp():
        TID = entry1.get()
        #print(TID)

        mycursor.execute("DELETE FROM transaction WHERE Transaction_ID='%s' " % (TID))
        conn.commit()
        #mycursor.fetchall()
        #print information

        message = "You've cancelled you're flight. "
        text1.insert(0.0, message)

    label = tk.Label(popup, text="Cancel Your Flight", font=NORMAL_FONT)
    label.grid(row=0, column=2, sticky="NW")

    label1 = ttk.Label(popup, text="Transaction Number:", font=SMALL_FONT)
    label1.grid(row=1, column=0, sticky="NW")
    entry1 = ttk.Entry(popup)
    entry1.grid(row=1, column=1, sticky="NW")

    button1 = ttk.Button(popup, text="Cancel Flight", command=lambda: LookUp())
    button1.grid(row=2, column=1, sticky="nsew")

    text1 = tk.Text(popup, width=50, height=15, font=SMALL_FONT)
    text1.grid(row=3, column=1, columnspan=3, sticky="nsew")

    button2 = ttk.Button(popup, text="Exit", command=lambda: popup.destroy())
    button2.grid(row=8, column=1, sticky="NE")

    popup.geometry("550x450")
    popup.mainloop()
#=======================================================================================================================
                           #FUNCTIONS FOR THE "Manager's Options" MENU CASCADE OPTIONS
#=======================================================================================================================
def ManageTickets():
    popup = tk.Tk()
    popup.wm_title("Ticket Management")

    label = tk.Label(popup, text="Manager's Option", font=NORMAL_FONT)
    label.grid(row=0, column=1, sticky="NW")
    label1 = tk.Label(popup, text="Use Manager's ID: 12345 ONLY for DEMONSTRATION purposes.", font=NORMAL_FONT)
    label1.grid(row=1, column=1, sticky="NW")

    label2 = ttk.Label(popup, text="Manager's ID:", font=SMALL_FONT)
    label2.grid(row=2, column=0, sticky="NW")
    entry2 = ttk.Entry(popup)
    entry2.grid(row=2, column=1, sticky="NW")

    label3 = ttk.Label(popup, text="Flight ID:", font=SMALL_FONT)
    label3.grid(row=3, column=0, sticky="NW")
    entry3 = ttk.Entry(popup)
    entry3.grid(row=3, column=1, sticky="NW")

    label4 = ttk.Label(popup, text="Class of Ticket:", font=SMALL_FONT)
    label4.grid(row=4, column=0, sticky="NW")
    entry4 = ttk.Entry(popup)
    entry4.grid(row=4, column=1, sticky="NW")

    label5 = ttk.Label(popup, text="Price:", font=SMALL_FONT)
    label5.grid(row=5, column=0, sticky="NW")
    entry5 = ttk.Entry(popup)
    entry5.grid(row=5, column=1, sticky="NW")

    text1 = tk.Text(popup, width=50, height=15, font=SMALL_FONT)
    text1.grid(row=12, column=1, columnspan=3, sticky="nsew")

    button1 = ttk.Button(popup, text="Add Ticket", command=lambda: LookUp())
    button1.grid(row=13, column=1, sticky="nsew")

    def LookUp():
        # FID = entry10.get()
        ManagerID = entry2.get()

        if ManagerID == str(12345):
            # ManagerID = entry2.get()
            FID = entry3.get()
            Ctype = entry4.get()
            Price = entry5.get()

            mycursor.execute("INSERT INTO tickets VALUES(default, '%s','%s','%s')"
                             % (FID, Ctype, Price))
            conn.commit()

            message = "Success! You've added a flight."
            text1.insert(0.3, message)

    popup.geometry("575x450")
    popup.mainloop()
#-----------------------------------------------------------------------------------------------------------------------
def ManagePlanes():
    popup = tk.Tk()
    popup.wm_title("Plane Management")

    label = tk.Label(popup, text="Manager's Option", font=NORMAL_FONT)
    label.grid(row=0, column=1, sticky="NW")
    label1 = tk.Label(popup, text="Use Manager's ID: 12345 ONLY for DEMONSTRATION purposes.", font=NORMAL_FONT)
    label1.grid(row=1, column=1, sticky="NW")

    label2 = ttk.Label(popup, text="Manager's ID:", font=SMALL_FONT)
    label2.grid(row=2, column=0, sticky="NW")
    entry2 = ttk.Entry(popup)
    entry2.grid(row=2, column=1, sticky="NW")

    label3 = ttk.Label(popup, text="Airline Name:", font=SMALL_FONT)
    label3.grid(row=3, column=0, sticky="NW")
    entry3 = ttk.Entry(popup)
    entry3.grid(row=3, column=1, sticky="NW")

    label4 = ttk.Label(popup, text="Type of Plane:", font=SMALL_FONT)
    label4.grid(row=4, column=0, sticky="NW")
    entry4 = ttk.Entry(popup)
    entry4.grid(row=4, column=1, sticky="NW")

    text1 = tk.Text(popup, width=50, height=15, font=SMALL_FONT)
    text1.grid(row=12, column=1, columnspan=3, sticky="nsew")

    button1 = ttk.Button(popup, text="Add Plane", command=lambda: LookUp())
    button1.grid(row=13, column=1, sticky="nsew")

    def LookUp():
        ManagerID = entry2.get()

        if ManagerID == str(12345):
            Aname = entry3.get()
            Ptype = entry4.get()

            mycursor.execute("INSERT INTO planes VALUES(default, '%s', '%s')"
                             % (Aname, Ptype))
            conn.commit()

            message = "Success! You've added a flight."
            text1.insert(0.3, message)

    popup.geometry("575x450")
    popup.mainloop()
#-----------------------------------------------------------------------------------------------------------------------
def ManageFlights():
    popup = tk.Tk()
    popup.wm_title("Flight Management")

    label = tk.Label(popup, text="Manager's Option", font=NORMAL_FONT)
    label.grid(row=0, column=1, sticky="NW")
    label1 = tk.Label(popup, text="Use Manager's ID: 12345 ONLY for DEMONSTRATION purposes.", font=NORMAL_FONT)
    label1.grid(row=1, column=1, sticky="NW")

    label2 = ttk.Label(popup, text="Manager's ID:", font=SMALL_FONT)
    label2.grid(row=2, column=0, sticky="NW")
    entry2 = ttk.Entry(popup)
    entry2.grid(row=2, column=1, sticky="NW")

    label3 = ttk.Label(popup, text="Departure Destination:", font=SMALL_FONT)
    label3.grid(row=3, column=0, sticky="NW")
    entry3 = ttk.Entry(popup)
    entry3.grid(row=3, column=1, sticky="NW")

    label4 = ttk.Label(popup, text="Arrival Destination:", font=SMALL_FONT)
    label4.grid(row=4, column=0, sticky="NW")
    entry4 = ttk.Entry(popup)
    entry4.grid(row=4, column=1, sticky="NW")

    label5 = ttk.Label(popup, text="Plane ID:", font=SMALL_FONT)
    label5.grid(row=5, column=0, sticky="NW")
    entry5 = ttk.Entry(popup)
    entry5.grid(row=5, column=1, sticky="NW")

    label6 = ttk.Label(popup, text="Departure Time:", font=SMALL_FONT)
    label6.grid(row=6, column=0, sticky="NW")
    entry6 = ttk.Entry(popup)
    entry6.grid(row=6, column=1, sticky="NW")

    label7 = ttk.Label(popup, text="Arrival Time:", font=SMALL_FONT)
    label7.grid(row=7, column=0, sticky="NW")
    entry7 = ttk.Entry(popup)
    entry7.grid(row=7, column=1, sticky="NW")

    label8 = ttk.Label(popup, text="Duration:", font=SMALL_FONT)
    label8.grid(row=8, column=0, sticky="NW")
    entry8 = ttk.Entry(popup)
    entry8.grid(row=8, column=1, sticky="NW")

    label9 = ttk.Label(popup, text="Flight's Status:", font=SMALL_FONT)
    label9.grid(row=9, column=0, sticky="NW")
    entry9 = ttk.Entry(popup)
    entry9.grid(row=9, column=1, sticky="NW")

    label10 = ttk.Label(popup, text="Total Seats:", font=SMALL_FONT)
    label10.grid(row=10, column=0, sticky="NW")
    entry10 = ttk.Entry(popup)
    entry10.grid(row=10, column=1, sticky="NW")

    label11 = ttk.Label(popup, text="Open Seats:", font=SMALL_FONT)
    label11.grid(row=11, column=0, sticky="NW")
    entry11 = ttk.Entry(popup)
    entry11.grid(row=11, column=1, sticky="NW")

    text1 = tk.Text(popup, width=50, height=15, font=SMALL_FONT)
    text1.grid(row=12, column=1, columnspan=3, sticky="nsew")

    button1 = ttk.Button(popup, text="Add Flight", command=lambda: LookUp())
    button1.grid(row=13, column=1, sticky="nsew")

    def LookUp():
        # FID = entry10.get()
        ManagerID = entry2.get()

        if ManagerID == str(12345):
            # ManagerID = entry2.get()
            Ddestination = entry3.get()
            Adestination = entry4.get()
            PID = entry5.get()
            Dtime = entry6.get()
            Atime = entry7.get()
            Duration = entry8.get()
            Fstatus = entry9.get()
            Tseats = entry10.get()
            Oseats = entry11.get()

            mycursor.execute("INSERT INTO flights VALUES(default, '%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                             % (Ddestination, Adestination, PID, Dtime, Atime, Duration, Fstatus, Tseats, Oseats))
            conn.commit()

            mycursor.execute("SELECT * FROM flights WHERE From_Destination='%s' AND To_Destination='%s' "
                             "AND Plane_ID='%s' AND Time_Departure='%s' AND Time_Arrival='%s' AND Duration='%s' "
                             "AND Seats_Total='%s' AND Seat_Open='%s' AND Flight_Status='%s'"
                             % (Ddestination, Adestination, PID, Dtime, Atime, Duration, Fstatus, Tseats, Oseats))
            #information = (mycursor.fetchall())
            #print(information)

            message = "Success! You've added a flight."
            text1.insert(0.3, message)

    popup.geometry("600x500")
    popup.mainloop()
#-----------------------------------------------------------------------------------------------------------------------
def ManageFlightInfo():
    popup = tk.Tk()
    popup.wm_title("Change Flight Information")

    label = tk.Label(popup, text="Manager's Option", font=NORMAL_FONT)
    label.grid(row=0, column=1, sticky="NW")
    label1 = tk.Label(popup, text="Use Manager's ID: 12345 ONLY for DEMONSTRATION purposes.", font=NORMAL_FONT)
    label1.grid(row=1, column=1, sticky="NW")

    label2 = ttk.Label(popup, text="Manager's ID:", font=SMALL_FONT)
    label2.grid(row=2, column=0, sticky="NW")
    entry2 = ttk.Entry(popup)
    entry2.grid(row=2, column=1, sticky="NW")

    label3 = ttk.Label(popup, text="Departure Destination:", font=SMALL_FONT)
    label3.grid(row=4, column=0, sticky="NW")
    entry3 = ttk.Entry(popup)
    entry3.grid(row=4, column=1, sticky="NW")

    label4 = ttk.Label(popup, text="Arrival Destination:", font=SMALL_FONT)
    label4.grid(row=5, column=0, sticky="NW")
    entry4 = ttk.Entry(popup)
    entry4.grid(row=5, column=1, sticky="NW")

    label5 = ttk.Label(popup, text="Plane ID:", font=SMALL_FONT)
    label5.grid(row=6, column=0, sticky="NW")
    entry5 = ttk.Entry(popup)
    entry5.grid(row=6, column=1, sticky="NW")

    label6 = ttk.Label(popup, text="Departure Time:", font=SMALL_FONT)
    label6.grid(row=7, column=0, sticky="NW")
    entry6 = ttk.Entry(popup)
    entry6.grid(row=7, column=1, sticky="NW")

    label7 = ttk.Label(popup, text="Arrival Time:", font=SMALL_FONT)
    label7.grid(row=8, column=0, sticky="NW")
    entry7 = ttk.Entry(popup)
    entry7.grid(row=8, column=1, sticky="NW")

    label8 = ttk.Label(popup, text="Duration:", font=SMALL_FONT)
    label8.grid(row=9, column=0, sticky="NW")
    entry8 = ttk.Entry(popup)
    entry8.grid(row=9, column=1, sticky="NW")

    label9 = ttk.Label(popup, text="Flight's Status:", font=SMALL_FONT)
    label9.grid(row=10, column=0, sticky="NW")
    entry9 = ttk.Entry(popup)
    entry9.grid(row=10, column=1, sticky="NW")

    label10 = ttk.Label(popup, text="Total Seats:", font=SMALL_FONT)
    label10.grid(row=11, column=0, sticky="NW")
    entry10 = ttk.Entry(popup)
    entry10.grid(row=11, column=1, sticky="NW")

    label11 = ttk.Label(popup, text="Flight's ID:", font=SMALL_FONT)
    label11.grid(row=3, column=0, sticky="NW")
    entry11 = ttk.Entry(popup)
    entry11.grid(row=3, column=1, sticky="NW")

    label12 = ttk.Label(popup, text="Open Seats:", font=SMALL_FONT)
    label12.grid(row=12, column=0, sticky="NW")
    entry12 = ttk.Entry(popup)
    entry12.grid(row=12, column=1, sticky="NW")

    text1 = tk.Text(popup, width=50, height=15, font=SMALL_FONT)
    text1.grid(row=13, column=1, columnspan=3, sticky="nsew")

    button1 = ttk.Button(popup, text="Change Flight", command=lambda: LookUp())
    button1.grid(row=14, column=1, sticky="nsew")

    def LookUp():
        ManagerID = entry2.get()

        if ManagerID == str(12345):
            FID = entry11.get()
            Ddestination = entry3.get()
            Adestination = entry4.get()
            PID = entry5.get()
            Dtime = entry6.get()
            Atime = entry7.get()
            Duration = entry8.get()
            Fstatus = entry9.get()
            Tseats = entry10.get()
            Oseats = entry11.get()

            mycursor.execute("UPDATE flights SET From_Destination='%s', To_Destination='%s', Plane_ID='%s', "
                             "Time_Departure='%s', Time_Arrival='%s', Duration='%s', Flight_Status='%s', "
                             "Seats_Total='%s', Seat_Open='%s' WHERE Flight_ID='%s'"
                             % (Ddestination, Adestination, PID, Dtime, Atime, Duration, Fstatus, Tseats, Oseats, FID))
            conn.commit()

            message = "Success! You've changed a flight."
            text1.insert(0.3, message)

    popup.geometry("600x500")
    popup.mainloop()
#=======================================================================================================================
                           #CREATES MAIN PAGES OF MY GUI
#=======================================================================================================================
class DubonsAirline (tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Dubon's Airline")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        AboutMenu = tk.Menu(menubar, tearoff=0)
        AboutMenu.add_command(label="Contact Us", command=lambda: AboutUs())
        AboutMenu.add_separator()
        AboutMenu.add_command(label="Instructions", command=lambda: Instructions())
        AboutMenu.add_command(label="Frequent Q/As", command=lambda: QuestionsAnswers())
        AboutMenu.add_separator()
        AboutMenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="About...", menu=AboutMenu)

        CustomersMenu = tk.Menu(menubar, tearoff=0)
        CustomersMenu.add_command(label="Create Account", command=lambda: menuCreateAccount())
        CustomersMenu.add_command(label="Account Log-In", command=lambda: LogInInformation())
        CustomersMenu.add_separator()
        CustomersMenu.add_command(label="Forgot Your Password?", command=lambda: InfoRetrival())
        CustomersMenu.add_separator()
        CustomersMenu.add_command(label="Change Information", command=lambda: ChangeAccountInfo())
        CustomersMenu.add_separator()
        CustomersMenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="Customers", menu=CustomersMenu)

        FlightsMenu = tk.Menu(menubar, tearoff=0)
        FlightsMenu.add_command(label="Flights", command=lambda: FlightsOptions())
        FlightsMenu.add_separator()
        FlightsMenu.add_command(label="Check In", command=lambda: CheckIn())
        FlightsMenu.add_command(label="Flight Status", command=lambda: FlightStatus())
        FlightsMenu.add_separator()
        FlightsMenu.add_command(label="Plane's Information", command=lambda: PlanesInformation())
        FlightsMenu.add_separator()
        FlightsMenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="Flight", menu=FlightsMenu)

        TicketsMenu = tk.Menu(menubar, tearoff=0)
        TicketsMenu.add_command(label="Purchase", command=lambda: TicketPurchase())
        TicketsMenu.add_command(label="Cancel", command=lambda: CancelTicket())
        TicketsMenu.add_separator()
        TicketsMenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="Tickets", menu=TicketsMenu)

        ManagersOptions = tk.Menu(menubar, tearoff=0)
        ManagersOptions.add_command(label="Add Tickets", command=lambda: ManageTickets())
        ManagersOptions.add_separator()
        ManagersOptions.add_command(label="Add Planes", command=lambda: ManagePlanes())
        ManagersOptions.add_separator()
        ManagersOptions.add_command(label="Add Flights", command=lambda: ManageFlights())
        ManagersOptions.add_command(label="Change Flight's Information", command=lambda: ManageFlightInfo())
        ManagersOptions.add_separator()
        ManagersOptions.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="Manager's Options", menu=ManagersOptions)

        tk.Tk.config(self, menu=menubar)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column = 0, sticky="nsew")

        self.show_frame(StartPage)




    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Welcome to Dubon's Airway", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        #label.grid(row=0, column = 3, sticky="nsew")

        button1 = ttk.Button(self, text="Create Account",command=lambda: controller.show_frame(PageOne))
        button1.pack(pady=10, padx=10)
        #button1.grid(row=4, column = 0, sticky="NW")

        button2 = ttk.Button(self, text="Log In",command=lambda: controller.show_frame(PageTwo))
        button2.pack(pady=10, padx=10)
        #button2.grid(row=4, column = 5, sticky="NW")

        button3 = ttk.Button(self, text="Close MySQL Connection", command=lambda: CloseConnection())
        button3.pack(pady=10, padx=10)
#-----------------------------------------------------------------------------------------------------------------------
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        FirstName = tk.StringVar()
        LastName = tk.StringVar()
        Password = tk.StringVar()
        Email = tk.StringVar()
        #print(FirstName)

        def CreateAccount():
            Fname=FirstName.get()
            Lname=LastName.get()
            PW=Password.get()
            EM=Email.get()
            #print(Fname, Lname, PW, EM)

            mycursor.execute("INSERT INTO accounts VALUES(default,'%s','%s','%s','%s')" % (Fname, Lname, PW, EM))
            conn.commit()
            # controller.show_frame(PageThree)

            mycursor.execute("SELECT * FROM accounts WHERE Password='%s' AND First_Name='%s' AND Last_Name='%s'" % (PW, Fname, Lname))
            information = (mycursor.fetchall())
            #print information
            for item in information:
                #text1.delete(0.0, END)
                User_Email = "\nUser Email: " + str(item[4])
                text1.insert(0.5, User_Email)
                #text1.delete(0.5, END)
                # print str(item[1])
                User_Password = "\nUser Password: " + str(item[3])
                text1.insert(0.4, User_Password)
                #text1.delete(0.4, END)
                Last_Name = "\nUser Last Name: " + str(item[2])
                text1.insert(0.3, Last_Name)
                #text1.delete(0.3, END)
                First_Name = "\nUser First Name: " + str(item[1])
                text1.insert(0.2, First_Name)
                User_ID = "\nUser ID: " + str(item[0])
                text1.insert(0.1, User_ID)
                message1 = "Congratulation! You've Created an Account"
                text1.insert(0.0, message1)
                #text1.config(state=DISABLED)
                #text1.delete(0.0, END)


        label = tk.Label(self, text="Create an Account:", font=NORMAL_FONT)
        #label.pack(pady=10, padx=10)
        label.grid(row=0, column=1, sticky="nsew")

        label2 = ttk.Label(self, text="First Name:", font=SMALL_FONT)
        label2.grid(row=2, column=0, sticky="NW")
        entry2 = ttk.Entry(self, textvariable=FirstName)
        entry2.grid(row=2, column=1, sticky="NW")
        label3 = ttk.Label(self, text="Last Name:", font=SMALL_FONT)
        label3.grid(row=3, column=0, sticky="NW")
        entry3 = ttk.Entry(self, textvariable=LastName)
        entry3.grid(row=3, column=1, sticky="NW")
        label4 = ttk.Label(self, text="Password:", font=SMALL_FONT)
        label4.grid(row=4, column=0, sticky="NW")
        entry4 = ttk.Entry(self, textvariable=Password)
        entry4.grid(row=4, column=1, sticky="NW")
        label5 = ttk.Label(self, text="Email:", font=SMALL_FONT)
        label5.grid(row=5, column=0, sticky="NW")
        entry5 = ttk.Entry(self, textvariable=Email)
        entry5.grid(row=5, column=1, sticky="NW")

        button1 = ttk.Button(self, text="Create", command=lambda: CreateAccount())
        #button1.pack()
        button1.grid(row=6, column=1, sticky="NW")

        text1=tk.Text(self, width=50, height=15, font=SMALL_FONT)
        text1.grid(row=7, column=1, sticky="NE")

        button2 = ttk.Button(self, text="Return", command=lambda: controller.show_frame(StartPage))
        #button2.pack()
        button2.grid(row=8, column=1, sticky="NE")
#-----------------------------------------------------------------------------------------------------------------------
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label6 = ttk.Label(self, text="Log In:", font=NORMAL_FONT)
        label6.grid(row=0, column=2, sticky="nsew")

        UserEmail = tk.StringVar()
        UserID = tk.StringVar()

        def LogInInformation():
            UE=UserEmail.get()
            UID=UserID.get()

            mycursor.execute("SELECT * FROM transaction WHERE User_ID='%s' " % (UID))
            information = (mycursor.fetchall())
            #print information

            for item in information:
                User_Email = "\nPlane's ID: " + str(item[5])
                text1.insert(0.5, User_Email)
                # print str(item[1])
                User_Password = "\nTicket's Arrival Destination: " + str(item[4])
                text1.insert(0.4, User_Password)
                Last_Name = "\nTicket's Departure Destination: " + str(item[3])
                text1.insert(0.3, Last_Name)
                First_Name = "\nPassenger Name: " + str(item[2])
                text1.insert(0.2, First_Name)
                User_ID = "\nTransaction ID: " + str(item[0])
                text1.insert(0.1, User_ID)
                message1 = "TRANSACTION HISTORY:"
                text1.insert(0.0, message1)

        label7 = ttk.Label(self, text="User Email:", font=SMALL_FONT)
        label7.grid(row=2, column=0, sticky="NW")
        entry7 = ttk.Entry(self, textvariable=UserEmail)
        entry7.grid(row=2, column=1, sticky="NW")
        label8 = ttk.Label(self, text="User ID Number:", font=SMALL_FONT)
        label8.grid(row=3, column=0, sticky="NW")
        entry8 = ttk.Entry(self, textvariable=UserID)
        entry8.grid(row=3, column=1, sticky="NW")

        button1 = ttk.Button(self, text="Log In", command=lambda: LogInInformation())
        #button2.pack()
        button1.grid(row=4, column=1, sticky="NW")

        text1=tk.Text(self, width=50, height=15, font=SMALL_FONT)
        text1.grid(row=5, column=1, columnspan=3, sticky="NW")

        button2 = ttk.Button(self, text="Return", command=lambda: controller.show_frame(StartPage))
        #button1.pack()
        button2.grid(row=6, column=3, sticky="NSEW")

app = DubonsAirline()
app.geometry("500x400+550+200")
app.mainloop()

