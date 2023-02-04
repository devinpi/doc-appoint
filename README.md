# Final Project for CS50W with Python and Javascript

## Project Name: *Doc-Appoint*

## Demo Video URL: (https://youtu.be/qKvAbQnQL1M)

## Introduction:
Doc-Appoint is an effective way for patients to book appointments with the doctors that are available on the platform.

![Home Page](https://github.com/devinpi/doc-appoint/blob/387231e8812f13e7ec1e918cff3cc8a1723c29b5/Doc_Appoint%20home%20Page.png)

### Why did I build this?
**The Story:** While I was doing this course, I had some health issues and I was frequently meeting with doctors, visiting clinics and hospitals. In my hometown, while big hospitals have a system to manage appointments and patients, private clinics on the other hand don't have any good management. I wanted it to be more organized which could help doctors as well as patients.

### What did I do to solve this? 
I  decided to design a system where a user could either be a doctor or a patient. User can register on the platform and after registering, user can login and will get access to the dashboard.

**Registration:** 

- Doctors will fill a form that will contain details related to your study, the services you provide, location, phone number, your education and experience.

- Patients, will fill personal details like, Full Name, Date of Birth, Gender, Phone etc. After that you get the access to the dashboard.

**Dashboard:**

- Doctor's dashboard will allow to search for patients using the search bar by their name. There are options to toggle betweent upcoming appointment and the history of appointments.

- Patient account will allow to search all the doctors based on their name or the services they provide. There are options to toggle between upcoming appointments, history appointments and, browse doctors.

**Booking Appointment**

- When a user as a patient visits a booking appointment page, it has all the details of the doctor. There is a book appointment section. It has date and time field. As you select the date, the application will tell you what all appointment times are booked for that date. After selecting the right date and time, book the appointment. 

**Patient-Report**

- After an appointment has been booked with a particular doctor, that doctor can see it in the doctor's dashboard. The doctor can search for their patients and can add something to the patient's report through patient report page.

## Distinctiveness and Complexity:
I wanted to think of something that would solve a problem. I had to think how the whole system will work from scratch. Also, I did come up with a theme, logo, name etc for the project. For this project I wanted the UI to be better than the previous projects. Used Figma, canva for design.

**Solving 2 user types problem**
- Before registering the user is given a choice to select whether they are looking for doctors or want to register as a doctor. Then assign that type based on the registration mode chosen by the user.

**Database models and how they'll work**

- The application has 5 models. User, Patient, Doctor, Report, Appointment.
- how the report and appointment models would operate:
  - To create a new report for every appointment that was created. So appointment is a table of all the upcoming and history of appointments. 
  - Every time a patient books an appointment a new report object is created with it which can be edited by the doctor during the day of the appointment. Once it goes to the history it cannot be edited.

**Setting up appointment timings dynamically:**

- Date and time data types and their conversion for different uses
  - Learned how to convert the datetime types to strings. Then convert them back to datetime objects to store them in the database. 
  - Used timedelta, strptime, strftime functions and extracted particular data from datetime objects.  
- Used JavaScript to output the appointment timeslots dynamically as entered by the doctor during the registration phase.
- The application also shows what time slots are booked for the selected date.

Creating 2 user types of the same application and deciding how the models will work togther. Understanding the datetime module and coming up with an booking system and how it will work took some time as it was a new concept to implement. All these were not used in the previous projects built during the course.


## What's there in each file?
- **views.py:** Contains all the view functions that render the html pages. It also has the api and other(search, time-slots) functions created for asynchronous programming that uses javascript.
- **models.py:** It has all the database model classes that are used for storing data. The classes or sqlite tables are: User, Patient, Doctor, Report, Appointment.
- **index.js, index-doc.js:** Contain JS functions for async programming for toggling between upcoming, history, browse buttons without reloding the page.
- **styles.css, booking_styles.css:** Contains all the styles for the html files.
- **index.html:** file for the home page of the web app.
- **login.html, register.html:** Contains pages for the user to login and register.
- **selection.html:** A page that gives a choice to the user, if wants to register as a doctor or a patient.
- **layout.html:** It has the main layout of the web app, all other pages use this layout.
- **next_steps_doc.html, next_steps_personal.html:** These pages have the forms for extra information from the doctor and the patient.
- **dashboard_doc.html, dashboard_personal.html:** These pages contain the dashboard code for both the user types. 
- **book_appointment.html:** A page that allows the patient to access info about the doctor and book an appointment.
- **patient-report:** A page to save the report of the patient.
- **urls.py:** Has all the paths for navigating the web app. All the api paths are also defined here.
- **admin.py:** To allow superuse to see the models in the Django admin UI.
- **requirement.txt:** All the package required for the web app.
- **README.md:** Read me markdown file for the project.
- Doc Appoint_footer.png, Doc Appoint_logo_v2.png, Doc Appoint_title_icon.png, doctor.svg, hero-image.svg, patient.svg, working.png: All the static images for the app.

## How to run the app:
- To run the app, first clone it on your pc using git
```
git clone <insert repository link>
```

- For database migrations use:
```
python manage.py makemigrations
python manage.py migrate
```

- For running the server use:
```
python manage.py runserver
```

- For using shell to insert data and testing use:
```
python manage.py shell
```

## Additional Information:
**Added OAuth2**
- I implemented Google OAuth2 for authorization and security along with django's auth. The additions and changes in the code are still there, It worked properly but, I had to remove the (button used to login using google) at the end because of some errors.

- For this project all available appointment time slots will have a difference of 30 minutes. 
