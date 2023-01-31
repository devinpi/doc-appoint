# Final Project for CS50W with Python and Javascript

## Project Name: *Doc-Appoint*

This project was created as the Final Project for Harvard's CS50 Web Development course. There were 5 other projects associated with the course as well.

## Introduction:
In simple words, Doc-Appoint is an effective way for personal users or patients to book appointments with the doctors that are available on the platform.

### Why I built this?
Before starting the final project I took some days and thought about the problems and wanted to come up with a solution that could actually be used by people. That's how Doc-Appoint was created.

**The Story:**

While I was doing this course, I had some health issues and I was frequently meeting with doctors, visiting clinics and hospitals. In my hometown, while big hospitals have a system to manage appointments and patients, private clinics on the other hand don't have any good management. I visited a lot of clinics that still use pen and paper for appointments and keeping a record of their patients. I wanted it to be more organized which could help doctors as well as patients. Although there are softwares in the market that can solve this, but I wanted to give it a try. 

### What did I do to solve this? 
I  decided to design a system where a user could either be a doctor or a patient. User can register on the platform and after registering, user can login and will get access to the dashboard.

**Registration:** 

- For Doctors, after you enter your username, password, email etc. you will be asked to fill another form that will contain details related to your study, the services you provide, location, phone number, your education and experience. Once you complete it you will be authorized to access the dashboard.

- For Personal, after registering you will be asked to fill in your personal details like, Full Name, Date of Birth, Gender, Phone etc. After that you get the access to the dashboard.

**Dashboard:**

- Dashboard for doctor account will allow you to search for your patients using the search bar by their name. There are options to toggle betweent the upcoming appointment and the history of appointments. This makes it easier to manage the record of patients. 

- Dashboard for personal or patient account will allow to search all the doctors based on their name or the services they provide. There are options to toggle between upcoming appointments, history appointments and, browse doctors. In browse doctors, all the doctors available on the platform will be available. This makes it easier for the patients to maintain the record of their appointments. So, if I want to review reports from 6 months before, I can review it through my dashboard.

**Booking Appointment**

- When a user as a patient visits a booking appointment page, it has all the details of the doctor. There is a book appointment section. It has date and time field. As you select the date, the application will tell you what all appointment times are booked for that date. After selecting the right date and time, book the appointment. 

*Note: You can only book appointment with a particular doctor once your previous appointment with that doctor  has passed.*

**Patient-Report**

- After an appointment has been booked with a particular doctor, that doctor can see it in the doctor's dashboard. The doctor can search for their patients and can add something to the patient's report through patient report page.

*Note: You only get to edit a patients report till the day of the appointment. After that that appointment will be shifted in the history section and report cannt be edited.*

---

## Distinctiveness and Complexity:

As per the requirement, this project is not similar to any of the projects done during this course. It is not similar to a social network, e-commerce website or the Pizza project. It is a booking system with 2 user types, each having their personal dashboard that updates when the information in the backend is updated. 

### What makes this project distinct and complex than the others?

The first thing is the idea itself. I wanted to think of something that would solve a problem. Coming up with a good idea is important. Because the idea was different, I had to think how the whole system will work from scratch. 

**Solving 2 user types problem**

- In the start, I was not sure how I was going to manage 2 different user types how database models will work together to store information. 
  - I came up with a solution of using CHOICES in django models in the User abstract class. Before registering the user is given a choice to select whether they are looking for doctors or want to register as a doctor.
  - Then assign that type based on the registration mode chosen by the user. This worked!

**Database models and how they'll work**

- The application has 5 models. User, Patient, Doctor, Report, Appointment. More about this is explained in the working section.
- The first issue that I encountered was where the doctor and patient database object should get created.
  - Solution was to create them after the additional forms were completed. 
- The next one is how to report and appointment models would operate:
  - Solution was to create a new report for every appointment that was created. So appointment is a table of all the upcoming appointments and the history of appointments. 
  - Every time a patient books an appointment a new report object is created with it which can be edited by the doctor during the day of the appointment. Once it goes to the history it cannot be edited.

**Setting up appointment timings dynamically:**

- Setting up the booking system and how it will work out.
  - In the beginning I tried to integrate some booking api in the application but, could not find a proper guide. So, I decided to build my own. It is not very complex but creating it took some time.
- Date and time data types and their conversion for different uses
  - I had to understand the datetime module in python and how to convert the datetime types to strings to output them to the front end. Then convert them back to datetime objects to store them in the database. 
  - Got to know more about timedelta, strptime, strftime functions and how to use them. Also, how to extract particular data from datetime objects.  
- Time slots for appointments
  - I wanted to use JavaScript to output the appointment timeslots dynamically as entered by the doctor during the registration phase.
  - The application also shows what time slots are booked for the selected date which uses Javascript.

Creating 2 user types of the same application and deciding how the models will work togther. Understanding the datetime module and coming up with an booking system and how it will work took some time as it was a new concept to implement. All these were not used in the previous projects built during the course.

Also, I did come up with a theme, logo, name etc for the project. I did not focus a lot on UI in my previous projects. For this project I wanted the UI to be better than the previous ones.

## Description of file in the project:

## How to run the app:

## Additional Information:

**Added OAuth2**
- I implemented Google OAuth2 for authorization and security along with django's auth. The additions and changes in the code are still there, It worked properly but, I had to remove the (button used to login using google) at the end because of some errors. It did not work properly with 2 user types and their models so, I had to leave it out of this project for now. I will add it some time in the future. 
