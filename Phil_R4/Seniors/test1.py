import csv
import smtplib

# Sender email
email = "circdesk@oxy.edu"

# Open the CSV file and read it with DictReader
with open('Phil_R4/Seniors/seniors_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Traverse the CSV file and extract necessary column info from each row
    for row in reader:
        
        # Receiver email found using info from the roq
        receiver_email = row['Preferred Email']
        
        # Formulate the email subject using the info from the row
        subject = ("URGENT - Final Overdue Notice")

        # Formulate the email message using the info from the row
        message = ("Hi " + row['First Name'] + " " + row["Last Name"] +
              ", \n\n According to Oxy Library records, you currently have " + row['Title'] + " checked out under your account, and it is " + row['Days Overdue'] +
              " days overdue. This is the final notice for you to return " + row['Title'] + "\n\n" +

              "Failure to return this item by May 10, 2024 will result in a replacement fee of $70. \n\n" +

               "Please return this book to the Library Information Desk in the Academic Commons. \n" + 
               "We are currently open Sunday through Thursday from 8AM to Midnight, Friday from 8AM to 10PM, and Saturday 10AM to 10PM.\n\n" +

               "Thank you,\n" + 
               "Oxy Library Information Desk"
              )
        
        text = f"Subject: {subject}\n\n{message}"

        # Starting server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Logging in using app password
        server.login(email,  "rxsp ndoy mgkd ttwu")

        # Send the email and convert the text to utf-8
        server.sendmail(email, receiver_email, text.encode('utf-8'))