import smtplib
import imghdr
from email.message import EmailMessage

def mailimage(image):
    Sender_Email = "falconmd73@gmail.com"
    Reciever_Email = "mike732000davis@gmail.com"
    Password = "MikeDavis@732"
    
    newMessage = EmailMessage()                         
    newMessage['Subject'] = "TEST MAIL" 
    newMessage['From'] = Sender_Email                   
    newMessage['To'] = Reciever_Email                   
    newMessage.set_content('Steganography. Image attached!') 
    
    with open(image, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    
    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        
        smtp.login(Sender_Email, Password)              
        smtp.send_message(newMessage)
        print("Image Sent")