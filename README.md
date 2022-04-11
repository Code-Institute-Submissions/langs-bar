# Langs Bar & Cocktail Lounge
## By Clayton File

![Am I Responsive](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/testing_results/langs-responsive.png)
![Lamgs Homepage](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/homepage.png)

Live Link [Here!](https://langs-bar-and-cocktail-lounge.herokuapp.com/)

## Table Of Contents
1. [Intro](#intro)
2. [Structure](#structure)
3. [Skeleton](#skeleton)
4. [Surface](#surface)
5. [Technologies](#technologies)
6. [Bugs & Fixes](#bugs--fixes)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Credits](#credits)

## Intro
A Heroku based E-Commerce Website for a Bar and Cocktail Lounge in Sittingbourne to allow customers to buy entry to the venues events and vip booths.

### Goals

- To enable the user to book events and vip tables.
- To enable the admin / company employee to check booked events backend and add new events.
- To enable the admin to add and update food and drink menus.

### Audience

- The application is aimed at potential and existing customers to view and book both events and VIP booths.
- The application is aimed at potential and existing customers by allowing them to view menu's for the venue.

### User Stories
Using Github "Issues" and "Projects" User stories are created to get a basic understanding of different users needs.
![User Stories](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/user-stories.png)

- Customers / Site Users
* As a User, I am able to access the site on my mobile, tablet and desktop which is adapted to provide the best experience.
* As a Customer i can log in so that I can view my event and vip booth booking.
* As a Customer i can contact the venue via the contact form.
* As a Customer i can reset my password by email so that i can reset without the need to contact admin.
* As a User i can easily navigate through the website without too much thought so that i can find what I'm looking for quickly.
* As a User i can easily identify what the website is about so that i know what it has to offer.
* As a Potential Customer or Existing Customer i can easily view the venues menu's.
* As a Potential Customer or Existing Customer i can easily view the venues menu's at the venue from a mobile device.

- Admin
* As an Admin i can Sign in backend so that i can view, edit and delete customer bookings.
* As an Admin i can add new bookings backend so that telephone and walk in customers can get booked in.
* As an Admin i can add or remove menu's backend so that i can ensure menu's are up to date.
* As an Admin i can add, edit or delete events frontend quickly and efficiently.


### Features:

* Website information clearly relayed upon entering the home page.
* Responsive Design - Site should function on mobile, tablet and desktop/laptop devices.
* Mobile and desktop navigations.
* Purchase event entries and vip booths.
* Manage, Edit and Delete events and vip booths.
* A Facebook page to advertise the business and accept "Messenger" for form of contact.

## Facebook
![Langs Facebook](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/langs-facebook.png)
I Created a company facebook page (see screenshot above) to demonstrate the capability but have unpublished this page due to the company already having an existing page for production which can be found at: [Here](https://www.facebook.com/LangsBarSittingbourne)

 -------------------------------------------------------------------------------------------------------------------------------------

## Structure
## - User Story:
```
As a user i can easily identify what the website is about so that i know what it has to offer.
```

## Acceptance Criteria:
Image displayed on the main page with clear inforation on the sites purpose.

## Implementation:
The Home Page will contain the main website title of "Langs Bar & Cocktail Bar" in the image.
The visitor will be met with the information on the general purpose of the site immediately.


## - User Story:
```
As a Customer, I can log in so that I can view my event and VIP booth booking.
```

## Acceptance Criteria:
The sites page will be met with the need to login before any bookings can be seen.

## Implementation:
The "My Profile" tab will be innaccessable without first logging in. Users will be able to click the login page from the nav menu.


## - User Story:
```
As a Customer, I can reset my password by email so that I can reset it without the need to contact the admin.
```
## Acceptance Criteria:
The website will send an email to the customers email address to reset password rather than posting to console which the user will not see.

## Implementation:
The website will be using an automated gmail app connection to send emails to the customers.


## - User Story:
```
As a Customer, I can contact the venue via the contact form.
```
## Acceptance Criteria:
The nav menu will have a link to a contact page.

## Implementation:
The contact form on the contact page will allow users to submit requests to the admin, which the admin can view from the backend.


## - User Story:
```
As a User, I am able to access the site on my mobile, tablet and desktop which is adapted to provide the best experience.
```
## Acceptance Criteria:
Clear responsiveness across all devices and all sizes.

## Implementation:
Responsiveness will be tested and adapted across all pages ensuring that users can use all devices from mobile, tablet and desktop.
Bootstrap 4 will take care of alot of this and ensuring each section sits where it should be expected across all devices.


## - User Story:
```
As a User, I can easily navigate through the website without too much thought so that I can find what I'm looking for quickly.
```
## Acceptance Criteria:
Easy to understand navigation system.

## Implementation:
The main navigation will hold all pages the user will need with some clearly displayed within a dropdown. The homepage will be easily identifiable via a font awesome icon of a house (home). Events are clearly displayed in their own section to add to bag.


## - User Story:
```
As an Admin I can Sign in backend so that I can view, edit and delete customer bookings.
```
## Acceptance Criteria:
A custom model allowing admin to view, edit and delete customer submissions.

## Implementation:
A custom model allowing admin to view, edit and delete customer submissions. Clear and easy to understand form used so we can get the customers 
information neeed to answer any enquiries.


## - User Story:
```
As a Potential Customer or Existing Customer, I can easily view the venue's menu's at the venue from a mobile device or from home.
```
## Acceptance Criteria:
A page to display menus on all device sizes.

## Implementation:
Using a bootstrap carousel all menus are displayed to the user front end, Admin can add more menus backend by simply uploading the image.


## - User Story:
```
As an Admin I can add new bookings backend so that telephone and walk-in customers can get booked in.
```
## Acceptance Criteria:
Allow Admin to manually add bookings.

## Implementation:
Using a custom model all bookings are possible to be created backend and asigned to customer details for thiose creating offline bookings or over the phone.


## - User Story:
```
As an Admin I can add or remove the menu's backend so that I can ensure menus are up to date.
```
## Acceptance Criteria:
Admin can manually add more menus backend.

## Implementation:
Using a custom model, Admin can upload a menu image backend which will automatically add to the menu carousel.


## - User Story:
```
As an Admin I can add, edit or delete events frontend quickly and efficiently.
```
## Acceptance Criteria:
Admin can create and edit events front end.

## Implementation:
Using a custom form, the Admin will be able to add or edit events front end with a nav link which only the superuser / admin role can see and access.

 -------------------------------------------------------------------------------------------------------------------------------------

## Skeleton

### Wireframes
The Company's current website is a bare bones structure of what they was looking for which was a mobile friendly website easy to use and check bookings and menu's.

### Homepage
![Homepage](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/wireframes/home-wireframe.png)
### About
![About](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/wireframes/about-wireframe.png)
### Add An Event
![Add An Event](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/wireframes/add-an-event-wireframe.png)
### Brunch
![Brunch](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/wireframes/brunch-wireframe.png)
### Cart
![Cart](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/wireframes/cart-wireframe.png)
### Checkout
![Checkout](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/wireframes/checkout-wireframe.png)
### Checkout Success
![Checkout Success](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/wireframes/checkout-success-wireframe.png)
### Contact Us
![Contact Us](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/wireframes/contact-us-wireframe.png)
### Evening Tables
![Evening Tables](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/wireframes/evening-tables-wireframe.png)
### Profile
![Profile](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/wireframes/profile-wireframe.png)
### VIP Booths
![VIP Booths](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/wireframes/vip-wireframe.png)
### Menus
![Menus](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/wireframes/menus-wireframe.png)

### Database Design
![Database Diagram](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/database.png)

### Flow Chart
![Flow Chart](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/flow-chart-2.png)
- [Flow Chart](https://lucid.app/)

### Security
Using config variables in heroku, all SECRET access keys are stored safely to prevent unwanted connections to the database.

-------------------------------------------------------------------------------------------------------------------------------------

## Surface
Typography
The site is using font-family Roboto with a backup of sans serif.


### Design

The Design ideas are from the existing company Langs Bar & Cocktail Lounge ( With Permission ) and adapted the app to match their current layout and colour scheme.
Their website can be found here:
- [Langs Bar & Cocktail Lounge](https://langsbar.co.uk/)

### Colours
We maintained the same colour pallete throughout to maintain consistency and ensure the website was a matching colour scheme to the existing Langs Bar & Cocktail Lounge Website. The black throughout the website is:
```
#030509
```

-------------------------------------------------------------------------------------------------------------------------------------

## Technologies

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
* This project was created using Python framework Django following Model-View-Template design
* Python Modules used (These can be found in the requirements.txt project file):
```
asgiref==3.5.0
cloudinary==1.29.0
countries==0.2.0
dj-database-url==0.5.0
Django==3.2
django-allauth==0.41.0
django-cloudinary-storage==0.3.0
django-countries==7.2.1
django-crispy-forms==1.14.0
django-phonenumber-field==6.0.0
gunicorn==20.1.0
oauthlib==3.2.0
phonenumberslite==8.12.42
Pillow==9.0.1
psycopg2-binary==2.9.3
python3-openid==3.2.0
pytz==2021.3
requests-oauthlib==1.3.1
sqlparse==0.4.2
stripe==2.65.0
whitenoise==6.0.0
```
- [HTML](https://en.wikipedia.org/wiki/HTML)
* This project uses HTML as the main language used to complete the structure of the Website.
- [CSS](https://en.wikipedia.org/wiki/CSS)
* This project uses custom written CSS to style the Website and some Bootstrap
- [Jquery](https://en.wikipedia.org/wiki/JQuery)
* Jquery was used for limit the quantity selectors.
- [Boostrap](https://getbootstrap.com/)
* The Bootstrap framework was used through the website for layout and responsiveness.
- [Django Web Framework](https://en.wikipedia.org/wiki/Django_(web_framework))
* The python web framework.
- [Heroku](https://en.wikipedia.org/wiki/Heroku)
* Heroku was used to deploy the live website.
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/)
* Google chromes built in developer tools are used to inspect page elements and help debug issues with the site layout and test different CSS styles.
- [Balsamiq](https://balsamiq.com/wireframes/)
* This was used to create wireframes for the 'Skeleton' Section above.
- [DBVisualizer](https://www.dbvis.com/)
* This was used to create the Database Diagram.
- [Cloudinary](https://cloudinary.com/)
* Used to store and style the site logo.
- [psycopg2](https://pypi.org/project/psycopg2/)
* Psycopg2 is a DB API 2.0 compliant PostgreSQL driver.
- [PostgreSQL](https://www.postgresql.org/)
* PostgreSQL was used to create the relational databases used as data storage for this project.
- [GitHub](https://github.com/)
* GitHub is the hosting site used to store the source code for the Website.
- [Google Fonts](https://fonts.google.com/specimen/Roboto?query=roboto#standard-styles)
* Google fonts are used throughout the project to import the Orbitron and Roboto fonts.

## Bugs & Fixes

- Date format in production on the events cards are backwards but correct locally.
This was fixed by using { event.date | date: "jS M Y" }, we must do this because of the way postgres handles date formatting.

## Testing

![Lighthouse](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/testing_results/lighthouse.png)
- [Google Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse)
Lighthouse was used to ensure performance, best practices and colours didnt prevent readability. There was a few factors which doesnt allow the score to add up to 100% including no HTTPS connection with heroku.

Another important piece of testing was to ensure only admin users can add, edit or delete events using if statements to restrict any user without super user access cannot manually search web address.

### Event Details False Error
![Event Details False Error](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/testing_results/false-error-event-detail.png)

The html validator shows a false error saying max value cannot be a empty string but in fact this is not the case.
```
<input readonly class="form-control qty_input text-dark" type="number"
name="quantity" value="1" min="1" max="{{ item.event.quantity }}"
data-item_id="{{ event.id }}"
id="id_qty_{{ event.id }}">
```

#### views.py
To ensure users cant add, edit or delete events and it is restricted to admin only, both "@login_required" and "if not request.user.is_superuser:".
This is to make sure 1) User is logged in and 2) The User trying to access this page is Admin / Super User.
See Example Below:
```
@login_required
def add_event(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
```

### HTML validator
HTML Validator was used to ensure best practices. I viewed the page source and copy and pasted into the HTML validator to confirm this.
![HTML Validator](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/testing_results/html-validator.png)
[HTML Validator](https://validator.w3.org/#validate_by_input)

### CSS Validator
CSS Validator was used, by copying and pasting css into W3C CSS Validator / Jigsaw.
![CSS Validator](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/testing_results/css-validator.png)
[CSS Validator](https://jigsaw.w3.org/css-validator/validator)

### PEP8 validator
[PEP8 Online](http://pep8online.com/) was used to check if python was pep8 compliant.
![PEP8](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/testing_results/pep8.png)

[Am I Responsive](http://ami.responsivedesign.is/)
![Am I Responsive](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/testing_results/langs-responsive.png)
Responsiveness was tested manually using google chrome development tools, my iPhone 13 pro max AND using Am i Responsive as per the above screenshot.

### Assumptions and Dependencies
Testing is dependent on the website being deployed live on Heroku.

### Access Requirements
Tester must have access to the Django Admin panel in order to manually verify the insertion of records into the databases.

### Regression Testing
Features previously tested during development in a local environment must be regression tested in production on the live website.

### Stripe Testing Debit / Credit Card
You can submit a test payment (because stripe is set to test mode) using the following card details.

Card Number:
4242 4242 4242 4242

Date:
04 / 24

Security:
242

Zip:
42424

## Manual Testing
![Manual Testing](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/testing_results/manually-testing.png)
All user stories have been included in testing along with each model, each test was ticked off the above list when receiving the expected results.

When manually testing stripe payments it was also important to check if the order still completes after closing the page during processing payment ensuring webhooks are working correctly.

When adding, updating or removing events from the bag/cart the quantity and totals updates correctly. After placing an order the quantity of the sold event also updates reducing the quantity available.

404.html and 500.html both work as expected, this was tested by typing a web address not recognised by the site for 404. For 500 a migration for contact was removed which results in the custom 500 page.

- All Models work correctly.
- All Forms work correctly.
- All Links lead to the correct destinations.
- Quantitys change correctly.
- Items can be removed from the bag correctly.
- Bag quantity updates correctly.
- Default billing in profile can be updated correctly.
- Menus can be added to the carousel by uploading backend.
- Uploaded images save correctly in Cloudinary.
- External links use rel="noopener" and target="blank"
- Emails working correctly.
- User profiles can be created.
- Passwords can be reset by email.
- Admin can view admin only pages, and Users cannot access these pages without superuser status.
- Events can be added both front and backend correctly.
- Site responsiveness was tested from mobile, tablet and laptop.
- Site was tested in iOS, Chrome, Safari, and google chrome browser extension for multi browser testing.
- All HTML, CSS, Javascript & Python checked and passed validators.
- All User stories have been completed and tested.

All expected results have passed during manual testing.

-------------------------------------------------------------------------------------------------------------------------------------

## Deployment

### Heroku
This application will be deployed via [Heroku](https://heroku.com)
1. Ensure all code is ready for deployment. 
2. Log into or sign up to Heroku
3. From Dashboard click "New" and select "create new app" from the drop-down menu.
4. Choose a unique but available name for your app and select your region.
5. Click "Create App".
6. Navigate to "Settings" and scroll down to "build packs".
7. Click "build packs" and then click both "python" and "node.js". Please note node.js is needed for the mock terminal and must be BELOW python on the list.
   they can be clicked and dragged to move.
8. Click on the settings tab and then click reveal config vars. Add your Variables here.
9. Navigate to the "Deploy" section.
10. Scroll down to "Deployment Method" and select "GitHub".
11. Authorize the connection of Heroku to GitHub.
12. Search for your GitHub repository name, and select the correct repository.
13. For Deployment there are two options, Automatic Deployments or Manual.
    - Automatic Deployment: This will prompt Heroku to re-build your app each time you push your code to GitHub.
    - Manual Deployment: This will only prompt Heroku to build your app when you manually tell it to do so.
14. Ensure the correct branch is selected "master/Main", and select the deployment method which suites you.

### Forking
If you wish to edit and experiment with the code you can fork the repository.
Forking a repository allows you to experiment without the original project being affected.
1. Navigate to the repository.
2. In the top right of the page, below your profile you should see a "Fork" button. Simply click on this.
3. A copy of the forked repository will then be added to your own Repositories Page.

### Clone

1. Navigate to the Github Repository you want to clone.

2. Click the drop down menu labelled "Clone".

3. Either Download the ZIP file, unpackage locally and open with IDE (This route ends here) OR Copy Git URL from the HTTPS dialogue box.

4. Open your developement editor and open a terminal window in a directory of your choice.

5. Use the 'git clone' command in terminal followed by the copied git URL.

6. A clone of the project will be created locally on your local machine.

-------------------------------------------------------------------------------------------------------------------------------------

## Credits

- [Whitenoise](https://devcenter.heroku.com/articles/django-assets)
For teaching me how to install whitenoise for my static assets.

- The Code Institute Course Material
For teaching me the majority of what is needed to complete this module.

### Acknowledgment
I'd like to thank my mentor [Daisy McGirr](https://github.com/Daisy-McG) for her continued guidance and support throughout my project.