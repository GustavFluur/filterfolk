### Project Goals

Filter for Folks is a Business to Consumer (B2C) e-commerce site.

The sites primary audience will be people who are living in condominiums and require air filter replacement in their apartments.

- Create a user-friendly platform for consumers seeking ventilation filters for their condos.
- Provide a diverse selection of filters categorized by location and type for easy navigation.
- Implement secure registration, login, and checkout processes to enhance user trust and satisfaction.
- Offer clear product descriptions, pricing, and sizing options to aid in informed decision-making.
- Enable easy management of products and orders for efficient store operations.

### Disclaimer

This project was inspired by the Stockholm based company [Folkfilter](https://www.folkfilter.se/) that I used to work for as an account manager. It gave me the understanding related to the target audience and daily challenges I faced during my employment. I was also taken a break from this course at Code Institute before I worked on Filter for Folks.  

With this message I want to show them my gratitude that I was allowed to use their product images into my website. Other product images was taken through a google search and from another Swedish company calls [Biltema](https://www.biltema.se/). 


### User Stories

| User Story ID | As a/an | I want to be able to ... | So that I can... |
| :--- | :--- | :--- | :---|
| **VIEWING & NAVIGATION** |
| 1 | Shopper | view a list of ventilation filters available on Filter Folks | select the filter I need for my condo |
| 2 | Shopper | view specific categories of filters, such as those designed for placement behind radiators or above windows | to quickly find products relevant to my needs. |
| **REGISTRATION & USER ACCOUNTS** |
| 3 | Site User | Easily register for an account on Filter Folks| Enabling me to view my profile and order history |
| 4 | Site User | Easily log in or out | Access my personal account information |
| 6 | Site User | Have a personalized user profile | View my personal order history and order confirmations, and save my payment information |
| **SORTING & SEARCHING** |
| 7 | Shopper | Sort the list of available filters by price, rating, and category | To identify the best options for my needs. |
| 8 | Shopper | Sort a specific category of Air Filter | Find the best-priced or best-rated product in a specific category, or sort the products in that category by name |
| 9 | Shopper | Search for a product by name or description | Find a specific product I'd like to purchase |
| 10 | Shopper | Easily see what I've searched for and the number of results | Quickly decide whether the product I want is available |
| **PURCHASING & CHECKOUT** |
| 11 | Shopper | Easily select the size and quantity of filters I wish to purchase | Ensuring I order the correct products |
| 12 | Shopper | View  items in my shopping bag, adjust quantities if necessary | enter payment information securely for checkout. |
| 13 | Shopper | View an order confirmation after checkout | Verify that I haven't made any mistakes |
| 14 | Shopper | Receive an email confirmation after checking out | Keep the confirmation of what I've purchased for my records |
| **ADMIN & STORE MANAGEMENT** |
| 15 | Store Owner | Add a product| Add new items to my store |
| 16 | Store Owner | Edit/update a product | Change product prices, descriptions, images and other product criteria |
| 17 | Store Owner | Delete a product | Remove items that are no longer for sale |

---

## Design

### Colour Scheme

- This the total color scheme for the whole website. If I have must have missed something in there I must apologise in advanced before you continue to read this readme file further. 

![color-scheme](assets/images/COLOR_SCHEME/color-scheme.png)
![color-scheme2](assets/images/COLOR_SCHEME/color-scheme2.png)


### Imagery

The opening page was added from [Pexels](https://www.pexels.com/) and it was also used in other areas of the website to appear professional depending on the navigation. A few product images as mentioned in the beginning the readme file was taken from a simple [Google Search](https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwjyuJSQxYaHAxWeAxAIHS0CDz0QPAgJ) e.g. [Rubber Strips](https://www.google.com/search?sca_esv=119356d5c00122f0&rlz=1C5CHFA_enSE941SE942&q=rubber+strips&udm=2&fbs=AEQNm0Aa4sjWe7Rqy32pFwRj0UkWd8nbOJfsBGGB5IQQO6L3J_TJ4YMS4eRay1mUcjRHkZwkNnuzbvXdHSnZt8SI-ypec-U-KajbXe9hbStxnPJuWxTCm8NISzlcRgh-mkg5a1XRWoiIVMkT5RYbraDRnHsJFse2AdcMQ0qNzsDHDLrzlWTINDALsSJJNGpMRvO4XnQg0w6_&sa=X&ved=2ahUKEwii2tiNxYaHAxWDLBAIHcy3CvAQtKgLegQIFBAB&biw=1440&bih=779&dpr=2) and from the Swedish hardwarestore [Biltema](https://www.biltema.se/en-se/). 

The reason for it was made this way was to save time and find a product image that easily represented of its usage for the potential buyer. I wasn't allowed to private photos of [Folkfilter's](https://www.folkfilter.se/) tools and they use to their air filter replacement services. 

### Facebook page 

- Facebook does not tolerate "fake" business profiles on its platform, so there's a risk that my business page might be deactivated if it's not deemed authentic, particularly if it was created using a new, empty Facebook user profile.

- To prevent any restraints regarding the presentation of my project in the readme.md file - I have  included some screenshots of the Facebook page in my documentation and followed those instructions by Code Institute. 

- If the Filter for Folk's [Facebook Page](https://www.facebook.com/profile.php?id=61561386792798) still exist -  please feel free to visit it!

![Facebook 1](assets/images/FACEBOOK/Facebook%201.png)
![Facebook 2](assets/images/FACEBOOK/Facebook%202.png)
![Facebook 3](assets/images/FACEBOOK/Facebook%203.png)
![Facebook 4](assets/images/FACEBOOK/Facebook%204.png)


---

## Technologies Used

### Languages Used

HTML, CSS, JavaScript, Python 3

### Databases Used

* sqlite3 - for the development database.
* ~~ElephantSQL - For the deployed sites database.~~ - ElephantSQL announced EOL for its service in February 2024.
* [CI DB](https://dbs.ci-dbs.net/) For the deployed site database

### Frameworks Used

* [Django](https://www.djangoproject.com/) - A high-level Python web framework that encourages rapid development and clean, pragmatic design.

* [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - Version 4.6 - A framework for building responsive, mobile-first sites.

### Libraries & Packages Used

* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)  - Used for authentication, registration & account management.

* [dj_database_url](https://pypi.org/project/dj-database-url/0.5.0/) - Allows us to utilise the DATABASE_URL environment variable.

* [Stripe](https://pypi.org/project/stripe/) - Version 9.11.0 - To allow us to utilise the Stripe API for payments.

* [gunicorn](https://pypi.org/project/gunicorn/) - Version 22.0.0 - a Python WSGI HTTP Server

* [psycopg2](https://pypi.org/project/psycopg2/) - A postgres database adaptor.

* [pillow](https://pypi.org/project/Pillow/)  - A python imaging library.

* asgiref

* [django-countries](https://pypi.org/project/django-countries/7.6.1/) - This is the latest stable version that is compatible with GitPod

* [django-crispy-forms](https://pypi.org/project/django-crispy-forms/) - provides a tag and filter that lets you quickly render forms

* oauthlib

* pytz

* requests-oauthlib

* sqlparse

* psycopg2 - a postgres database adapter which allow us to connect with a postgres database

* django-storages - a storage backend library


### Programs Used


* [GitHub](https://github.com/) - To save and store the files for this project.

* [Pip](https://pypi.org/project/pip/) - A tool for installing Python packages.

* [Google Dev Tools](https://developer.chrome.com/docs/devtools/) - To troubleshoot, test features and solve issues with responsiveness and styling.

* [MailChimo](https://mailchimp.com/?currency=SEK) - To create newsletters. 

* [Color Scheme](https://coolors.co/000000-2f1000-621b00-945600-c75000) - To create colorschemes. 

### Stripe

* [Stripe](https://stripe.com/gb) has been used in the project to implement the payment system.

Stripe for the website is currently in developer mode, which allows us to be able to process test payments to check the function of the site.

| Type | Card No | Expiry | CVC | ZIP |
| :--- | :--- |:--- | :--- | :--- |
| Success| Visa | 4242 4242 4242 4242 | A date in the future | Any 3 digits | Any 5 digits |
| Require authorisation | 4000 0027 6000 3184 | A date in the future | Any 3 digits | Any 5 digits |
| Declined | 4000 0000 0000 0002 | A date in the future | Any 3 digits | Any 5 digits |

Stripe Documentation- setting up stripe elements to accept payment [docs](https://stripe.com/docs/js)

---

## Features

Once you come to the Filter for Folks website the opening page looks like this: 

![opening-page](assets/images/FEATURES/opening-page.png)

As visitor you have multiple options. For starters if you can click on the "OUR INVENTORY" button to come the total inventory page. In there you are able to see the product description and images of each product, however to prevent other competitors to see what our prices are we have set up a function that a new visitor needs to register an account at Filter for Folks. 

![Inventory Mobile](assets/images/FEATURES/our-inventory-mobile.png)
![Inventory Desktop](assets/images/FEATURES/our-inventory-desktop.png)
![Inventory Desktop 2](assets/images/FEATURES/our-inventory-desktop%202.png)

This is to generate more traffic to the website and arouse curiosity. Once you click on the gray button that says "Wanna see our prices?" it takes you to the register page.

Once you have created an account it it greats you with a new message on the home page. This is an indication that you're in and a sense of change within the navigation for the visitor. Who is now our full customer with more accessibility on the page. 

The navbar has also been updated for the user. If you are an admin you are been allocated with a green button that's being called add product. This is to add some new products for the admin into the page and for customer to see how much they have spent in the cart area. 
 




### Future Implementations

Favicon - wasn't implemented into the project. The reason behind this was that I started my project from scratch and didn't use 



## Credits to my mentor

I want to show my gratitude to my mentor at Code Insitute, who guided me in this project. 

- Jubril Akolade 

I also want to highlight my previous mentor who supported me the whole course: 

- Martina Terlevic


## Credits to TUT Support on Code Institute

- John
- Roo 
- Oisin
- Roman
- Sarah
- Thomas 
- Holly
- Rebecca 
- Lewis
- Martin 
- Jason 
- Alan 
- Gemma
- Sean 
- Scott 

## Instructions if the workspace fails:

##### Follow these steps: 

- pip3 install 'django<4'
- pip install django-crispy-forms
- python -m pip install Pillow