import csv
import smtplib

# Sender email
email = "techlending@oxy.edu"

# Open the CSV file and read it with DictReader
with open('Round 6/data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Traverse the CSV file and extract necessary column info from each row
    for row in reader:
        
        # Receiver email found using info from the roq
        receiver_email = row['Preferred Email']
        
        # Formulate the email subject using the info from the row
        subject = ("IMPORTANT - Final Day To Return " + row['Title'])

        # Formulate the email message using the info from the row
        message = ("Hi " + row['First Name'] + 
              ", \n\nIt looks like you still have a " + row['Title'] + " from tech lending\n\n" +

              "If it is not returned by noon, tomorrow May 17, 2024, you will be billed the total cost of the item.\n\n" +

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