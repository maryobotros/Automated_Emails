import csv
import smtplib

# Sender email
email = "techlending@oxy.edu"

# Open the CSV file and read it with DictReader
with open('Round 5/data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Traverse the CSV file and extract necessary column info from each row
    for row in reader:
        
        # Receiver email found using info from the roq
        receiver_email = row['Preferred Email']
        
        # Formulate the email subject using the info from the row
        subject = ("URGENT - Tech Lending Item Due Today")

        # Formulate the email message using the info from the row
        message = ("Hi " + row['First Name'] + 
              ", \n\n According to Oxy Library records, you still have an overdue " + row['Title'] + " \n\n" +

              "Today, May 10, 2024, is the final day to return tech lending items. If the item is not returned today by 5PM, your student account will be charged the total cost of the item \n\n" +

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