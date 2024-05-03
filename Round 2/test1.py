import csv
import smtplib

# Sender email
email = "techlending@oxy.edu"

# Open the CSV file and read it with DictReader
with open('Round 2/data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Traverse the CSV file and extract necessary column info from each row
    for row in reader:
        
        # Receiver email found using info from the roq
        receiver_email = row['Preferred Email']
        
        # Formulate the email subject using the info from the row
        subject = ("URGENT - Second Overdue Notice")

        # Formulate the email message using the info from the row
        message = ("Hi " + row['First Name'] + 
              ", \n\n According to Oxy Library records, you currently have a " + row['Title'] + " checked out, and it is now " + row['Days Overdue'] +
              " days overdue. We kindly ask that you return the " + row['Title']+ " as soon as possible to avoid a possible replacement fee, and so that" +
               " others may have a chance to borrow it.\n\n" +

               "Please return the " + row['Title'] + " to the Library Information Desk in the Academic Commons. \n" + 
               "We are currently open Sunday through Thursday from 8AM to Midnight, Friday from 8AM to 10PM, and Saturday 10AM to 10PM\n\n" +

               "Thank you,\n" + 
               "Oxy Library Tech Lending"
              )
        
        text = f"Subject: {subject}\n\n{message}"

        # Starting server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Logging in using app password
        server.login(email,  "xxil pueg prrl bscg")

        # Send the email
        server.sendmail(email, receiver_email, text)