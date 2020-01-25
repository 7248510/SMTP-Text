import smtplib
#from config import server,email,password
#server.ehlo()
#server.starttls()
#server.ehlo()
#server.login(email, password)

def message():  
    presend = ('presend')
    send = ('send') 
    print('If you would like to send a message please type "send".\nIf you would like to send a predefined message please type "presend".')
    selection = input()
    
    #Prompts the user
    if (selection != send and presend != selection):
        print("Not a valid option.")
        f1 = "'"
        print('You entered',f1+selection+f1,'\nWould you like to restart the program?', "\nPlease type 'yes' to restart.","\nIf you'd like to exit press any key.")

        trigger = input()
        if (trigger == 'yes'):
            message()
        else:
            print("Closing program.")
                           
    if (selection == presend):
        premessage = ("This is the messsage that will be sent unless it's changed.")
        print(premessage)
    '''
    #check = 160 the length of the string
        before the message is sent.
    '''
    if (selection == send):
        print("Please enter the string you would like to send!")
   
    #msginput = input()
    #server.sendmail(email, "number@designatedcarrier.com", msg)
def main():
   message()   
main()


