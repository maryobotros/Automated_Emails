import csv
import smtplib

# Sender email
email = "docdel@oxy.edu"

# Open the CSV file and read it with DictReader
with open('Tia/tia_faculty_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Traverse the CSV file and extract necessary column info from each row
    for row in reader:
        
        # Receiver email found using info from the roq
        receiver_email = row['Preferred Email']
        
        # Formulate the email subject using the info from the row
        subject = ("OVERDUE RESOURCE SHARING")

        # Formulate the email message using the info from the row
        message = ("Dear " + row['First Name'] + row['Last Name'] +
              ", \n\n According to our records, you have " + row['Title'] + " checked out under your account. The book is now " + row['Days Overdue'] +
              " days overdue. Please bring " + row['Title']+ " back before May 3, 2024.  If you do not return the book, we will consider this a lost title"+

               "It is important to note that these books do not belong to Occidental. We have borrowed these books from other libraries, and in order to be in good\n" + 
               "standing and foster a healthy resource sharing relationship, it is critical that we return books to their owning libraries in a timely manner.\n\n" +

               "Please let me know if you have any questions or concerns\n\n"+ 
               
               "Thank you for your propmpt attention."
              )
        
        text = f"Subject: {subject}\n\n{message}"

        # Starting server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Logging in using app password
        server.login(email,  "yama fbtr hmoy ulig")

        # Send the email
        server.sendmail(email, receiver_email, text)