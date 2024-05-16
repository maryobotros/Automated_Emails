import csv
import smtplib

# Sender email
email = "circdesk@oxy.edu"

# Open the CSV file and read it with DictReader
with open('Phil_R5/data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Traverse the CSV file and extract necessary column info from each row
    for row in reader:
        
        # Receiver email found using info from the roq
        receiver_email = row['Preferred Email']
        
        # Formulate the email subject using the info from the row
        subject = ("URGENT - Books Due Tomorrow")

        # Formulate the email message using the info from the row
        message = ("Hi " + row['First Name'] +
              ", \n\nIt looks like you still have the following book: " + row['Title'] + "\n\n" +

               "This is the final notice for you to return the book. If it is not returned by noon, tomorrow May 17, 2024, your student account will be charged $70.\n\n" +

               "Thank you,\n" + 
               "Oxy Library Information Desk"
              )
        
        text = f"Subject: {subject}\n\n{message}"

        # Starting server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Logging in using app password
        server.login(email,  "gxun yayj hdxn qjbp")

        # Send the email and convert the text to utf-8
        server.sendmail(email, receiver_email, text.encode('utf-8'))