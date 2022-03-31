# Langs Bar & Cocktail Lounge
## By Clayton File

![Am I Responsive](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/testing_results/langs-responsive.png)
![BookingAppHomepage](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/homepage.png)

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

## Structure
- User Story:
```
As a user i can easily identify what the website is about so that i know what it has to offer.
```

Acceptance Criteria:

Image displayed on the main page with clear inforation on the sites purpose.

Implementation:

The Home Page will contain the main website title of "Langs Bar & Cocktail Bar" in the image.
The visitor will be met with the information on the general purpose of the site immediately.

- User Story:
'''
As a Customer i can log in so that I can view my booking.
'''

Acceptance Criteria:

The sites page will be met with the need to login before any bookings can be seen.

Implementation:

The "My Profile" tab will be innaccessable without first logging in. Users will be able to click the login page from the nav menu.

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
![Database Diagram](### VIP Booths
![VIP Booths](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/database.png)

### Security
Using config variables in heroku, all SECRET access keys are stored safely to prevent unwanted connections to the database.

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

- 

## Testing

![Flow Chart](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/flow-chart-2.png)
- [Flow Chart](https://lucid.app/)

![Lighthouse](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/testing_results/lighthouse.png)
- [Google Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse)
Lighthouse was used to ensure performance, best practices and colours didnt prevent readability. There was a few factors which doesnt allow the score to add up to 100% including no HTTPS connection with heroku.

Another important piece of testing was to ensure only admin users can add, edit or delete events using if statements to restrict any user without super user access cannot manually search web address.

- [Event Details False Error](https://github.com/TechCentreUK/langs-bar/blob/main/readme_images/testing_results/false-error-event-detail.png)
The html validator shows a false error saying max value cannot be a empty string but in fact this is not the case.
```
<input readonly class="form-control qty_input text-dark" type="number"
name="quantity" value="1" min="1" max="{{ item.event.quantity }}"
data-item_id="{{ event.id }}"
id="id_qty_{{ event.id }}">
```

## models.py
```
class Month(models.Model):
    """ A Model for months category """

    class Meta:
        """ Verbose name for admin """
        verbose_name_plural = 'Month'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    def get_friendly_name(self):
        """ Get friendly / front end name """
        return f"{self.friendly_name}"


ACTIVE_EXPIRED = [
    ('active', 'Active'),
    ('expired', 'Expired'),
]


class Event(models.Model):
    """ A Model for events """
    month = models.ForeignKey(
        'Month', null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    date = models.CharField(max_length=254)
    booth_size = models.CharField(max_length=254, null=True, blank=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    active_expired = models.CharField(
        choices=ACTIVE_EXPIRED, default='active', max_length=200
    )

    def __str__(self):
        return f"{self.name} - {self.date} - {self.active_expired}"
```
## views.py
```
@login_required
def add_event(request):
    """ Add a event to the store """

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

## Credits

- [Whitenoise](https://devcenter.heroku.com/articles/django-assets)
For teaching me how to install whitenoise for my static assets.

- The Code Institute Course Material
For teaching me the majority of what is needed to complete this module.

### Acknowledgment
I'd like to thank my mentor [Daisy McGirr](https://github.com/Daisy-McG) for her continued guidance and support throughout my project.
