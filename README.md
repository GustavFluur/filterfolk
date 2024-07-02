# Filter For Folks 

![Am I responsive](assets/images/Am%20I%20responsive/Am%20I%20responsive%20.png)

### Project Goals

Filter for Folks is a Business to Consumer (B2C) e-commerce site.

[ Link to deployed site](https://filter-for-folks-58441ed4952a.herokuapp.com/) 

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

The opening page was added from [Pexels](https://www.pexels.com/) and it was also used in other areas of the website to appear professional depending on the navigation. A few product images as mentioned in the beginning the readme file was taken from a simple [Google Search](https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwjyuJSQxYaHAxWeAxAIHS0CDz0QPAgJ) e.g. [Rubber Strips](https://www.google.com/search?sca_esv=119356d5c00122f0&rlz=1C5CHFA_enSE941SE942&q=rubber+strips&udm=2&fbs=AEQNm0Aa4sjWe7Rqy32pFwRj0UkWd8nbOJfsBGGB5IQQO6L3J_TJ4YMS4eRay1mUcjRHkZwkNnuzbvXdHSnZt8SI-ypec-U-KajbXe9hbStxnPJuWxTCm8NISzlcRgh-mkg5a1XRWoiIVMkT5RYbraDRnHsJFse2AdcMQ0qNzsDHDLrzlWTINDALsSJJNGpMRvO4XnQg0w6_&sa=X&ved=2ahUKEwii2tiNxYaHAxWDLBAIHcy3CvAQtKgLegQIFBAB&biw=1440&bih=779&dpr=2) and from the Swedish hardware store [Biltema](https://www.biltema.se/en-se/). 

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
* [Code Institute Database (DB)](https://dbs.ci-dbs.net/) For the deployed site database

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

* [Mail Chimp](https://mailchimp.com/?currency=SEK) - To create newsletters. 

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

## Deployment & Local Development

### Deployment

The project is deployed using Heroku. To deploy the project:



## Features

#### New Visitor view:

1. Once you come to the Filter for Folks website the opening page looks like this: 

![ opening-page ](assets/images/FEATURES/opening-page.png)

2. As visitor you have multiple options. For starters if you can click on the "OUR INVENTORY" button to come the total inventory page. 

![Inventory Mobile](assets/images/FEATURES/our-inventory-mobile.png)

![Inventory Desktop](assets/images/FEATURES/our-inventory-desktop.png)
![Inventory Desktop 2](assets/images/FEATURES/our-inventory-desktop%202.png)

![Product-Detail-no-account](assets/images/FEATURES/product-detail-no-acoount.png)

3. In there you are able to see the product description and images of each product, however to prevent other competitors to see what our prices are we have set up a function that a new visitor needs to register an account at Filter for Folks. 

![register-account](assets/images/FEATURES/register-account.png)

4. This is to generate substantial amount of traffic to the website and arouse curiosity. Once you click on the gray button that says "Wanna see our prices?" it takes you to the register page.

![after-register-account](assets/images/FEATURES/after-register-account.png)

#### Registered Personal Account view:

5. Once you have created an account it it greats you with a new message on the home page. This is an indication that you're in and a sense of change within the navigation for the visitor. Who is now our full customer with more accessibility on the page. Besides has the navbar been updated:

![updated-navbar](assets/images/FEATURES/updated-navbar.png)

6. The navbar has also been updated for the user. With 3 new buttons to account member. Once you click on uppercase button "search products". You'll enter product filter page.  

![search-product](assets/images/FEATURES/search-product.png)
![product-filter](assets/images/FEATURES/product-filter-page.png)
![product-filter-tab](assets/images/FEATURES/product-filter-tab.png)

7. In the tab to the left of the product filter you are able to type your product of interest in the search bar. e.g, you search toolbox: 

![toolbox-search-example](assets/images/FEATURES/toolbox-search-example.png)

8. However, in order to see all the products again and make another product search you need to press on default button to clear the filter. 

9. If chooses one of the categories you'll see either one or several items in the filter. * As mention the user needs to use the default filter button to see all the inventory again. * 

#### Purchase experience view:

10. If you decides to you purchase something, then you click on one of the products. In this case we purchases a vacuum cleaner: 

![product-vacuum-cleaner](assets/images/FEATURES/product-vacuum-cleaner.png)

11. You immediately navigated to the product detail page where you decides if you want to add this item into the shopping cart and its quantity. Plus you see an update in terms of its color (from gray to turquoise) and quantity in the cart. 

![cart-change](assets/images/FEATURES/shopping-change-add.png)

12. In the shopping it looks like this where you can do its changes and or if you want to delete the product entirely. This is before you do your checkout:

![cart-content](assets/images/FEATURES/cart-content.png)

13. Right after you click on secure checkout you'll be navigated to the checkout page where you can add the required personal details for you purchase:

![Checkout page](assets/images/FEATURES/checkout-page-submitted-details.png)

14. Once you clicked on the secure checkout you will be receiving a purchase confirmation: 

![Checkout page](assets/images/FEATURES/purchase-confirmation%20.png)

#### Tracking purchase view:

15. As a user you are able to do some updates in your personal account, if your personal details has changed and also you can look on previous orders (related to your personal account) - you'll able to find this necessary information there. Plus by clicking on the "order number" you'll be navigated back to the confirmation page. Thus it's an easy user experience to the customer and also important if they want to call or send an email to the Filter for Folks customer service in case of tracking the order. 

![Profile page & Tracking orders](assets/images/FEATURES/profile-account-info.png)

#### Reach out to the business view:

16. If you want to reach out to the business you need to click on the "contact" button in the footer below or the second nav element. The user can either contact by either email and calling the store. On the contact page the user is able to sign up for the newsletter connected to the Mail Chimp and find Filter for Folks Facebook page. (How the facebook looks like you'll find it above).

![Contact page](assets/images/FEATURES/connection-b2c.png)


17. How do you get yourself back to the home page? Either clicking on the business name "Filter for Folks" in the top left - in the nav element below. In there you also find the page of Filter for Folk's [Privacy Policy](https://www.termsfeed.com/live/1a7cc1bc-3fec-45b9-87a8-a43810a76fdf) to their users and how they are following the [GDPR](https://gdpr-info.eu/).  

![Nav below](assets/images/FEATURES/below-nav.png)

#### Sign In & Log Out views:

18. Once you want to leave the website you are clicking on the "logout" button in above nav element and the same comes to if you already have an account though you click on "Sign In" instead: 

![Log Out](assets/images/FEATURES/log-out.png)

19. Once you click on the sign out then you log out from the page. 

![Sign In](assets/images/FEATURES/Sign-In.png)

20. The user who clicks on the Sign In button will be directed to this page: 

![Sign In Page](assets/images/FEATURES/sign-in-page.png)

#### Admin view:

21. If you are an admin you are been allocated with a green button that's being called add product. This is to add some new products for the admin into the page and for customer to see how much they have spent in the cart area.

![Sign In Page](assets/images/FEATURES/filteradmin-view.png)

22. The add product page looks like this as the admin can choose name, which category that particular product belongs to, description, price and image. 

![Add Product Page](assets/images/FEATURES/add-product-page.png)


### Future Implementations

Favicon - wasn't implemented into the project. The reason behind this was that I started my project from scratch and didn't use Boutique Ado as foundation in beginning. Neither allauth packages thus some templates are in the allauth folder and other in core app. 

A feature that unfortunately was not implemented into the project is that the admin is able to create an category to further enhance the website for its liking.

### Accessibility

I have paid careful attention while coding to make sure the website is as user-friendly as possible for all users. This has been accomplished by:

* Using semantic HTML.
* Using descriptive alt attributes on images on the site.
* Providing information for screen readers where there are icons used and no text.
* Ensuring that there is a sufficient color contrast throughout the site.
* Accessibility was tested using Lighthouse and WAVE and further information can be found in the [TESTING.md](TESTING.md).

## Deployment & Local Development

### Deployment

The project is deployed using Heroku. To deploy the project:

#### **Create the Live Database**

We have been using the sqlite3 database in development, however this is only available for use in development so we will need to create a new external database which can be accessed by Heroku.

1. Go to the [ElephantSQL](https://www.elephantsql.com/) dashboard and click the create new instance button on the top right.
2. Name the plan (your project name is a good choice), select tiny turtle plan (this is the free plan) and choose the region that is closest to you then click the review button.
3. Check the details are all correct and then click create instance in the bottom right.
4. Go to the dashboard and select the database just created.
5. Copy the URL (you can click the clipboard icon to copy)

#### **Heroku app setup**

  1. From the [Heroku dashboard](https://dashboard.heroku.com/), click the new button in the top right corner and select create new app.
  2. Give your app a name (this must be unique), select the region that is closest to you and then click the create app button bottom left.
  3. Open the settings tab and create a new config var of `DATABASE_URL` and paste the database URL you copied from elephantSQL into the value (the value should not have quotation marks around it).

#### **Preparation for deployment in GitPod**

1. Install dj_database_url and psycopg2 (they are both needed for connecting to the external database you've just set up):

   ```bash
   pip3 install dj_database_url==0.5.0 psycopg2
   ```

2. Update your requirements.txt file with the packages just installed:

    ```bash
    pip3 freeze > requirements.txt
    ```

3. In settings.py underneath import os, add `import dj_database_url`

4. Find the section for DATABASES and comment out the code. Add the following code below the commented out database block, and use the URL copied from elephantSQL for the value:

    (NOTE! don't delete the original section, as this is a temporary step whilst we connect the external database. Make sure you don't push this value to GitHub - this value should not be saved to GitHub, it will be added to the Heroku config vars in a later step, this is temporary to allow us to migrate our models to the external database)

    ```python
    DATABASES = {
        'default': dj_database_url.parse('paste-elephantsql-db-url-here')
    }
    ```

5. In the terminal, run the show migrations command to confirm connection to the external database:

    ```bash
    python3 manage.py runserver
    ```

6. If you have connected the database correctly you will see a list of migrations that are unchecked. You can now run migrations to migrate the models to the new database:

    ```bash
    python3 manage.py migrate
    ```

7. Create a superuser for the new database. Input a username, email and password when directed.

    ```bash
    python3 manage.py createsuperuser
    ```

8. You should now be able to go to the browser tab on the left of the page in elephantsql, click the table queries button and see the user you've just created by selecting the auth_user table.

## Credits

The foundation of this project is based upon the walkthrough project [Boutique Ado](https://github.com/ckz8780/boutique_ado_v1). Since the requirements needed to have a checkout, cart, payment functionalities I used the majority of the code in that element. Because I saw the complexity of doing it dependently and Code Institute's TUT support referred me to the walkthrough project once I got stuck so I was forced to let it go to conduct my coding and followed the requirements for finalize the project accordingly. 

Before I started to work on Filter For Folks, I actually worked on another project and I came across a lot of issues regarding its migrations, stripe and deployment on Heroku. Some of the code from [Gold Scroll](https://github.com/GustavFluur/gold_scroll) has been a great help and a sense of direction if I got stuck during the process. 

I was also on a study break due to personal reasons and during that period I was keeping up my coding skills by working on [Merch Discount](https://github.com/GustavFluur/merch_discount) and this one is based upon the a course from [Learn Django by Building an Online Marketplace – Python Tutorial for Beginners](https://www.youtube.com/watch?v=ZxMB6Njs3ck) & [E-commerce Website using Django | Live Demo | Desphixs](https://www.youtube.com/watch?v=5n8FKv19os0&list=PL_KegS2ON4s53FNSqgXFdictTzUbGjoO-) - recommended by my mentor Jubril Akolade. 

---- 

#### Projects that has supported me thanks to Jubril Akolade(Mentor) 

- [Boutique-Ado by Kera Cudmore](https://github.com/kera-cudmore/Boutique-Ado) & I used the project's readme file as foundation. It might appear the same and I was stressed before I hand it in the project. Thus I some of the content within the readme file is structured the same. Plus I have dyslexia to save some time I was copy and pasted some of the words into my readme file. Likewise it's the same walkthrough project as it for the course at Code Institute. I want to have it addressed into my readme file and thanks for your understanding! 
- [The Quiz Arms by Kera Cudmore](https://github.com/kera-cudmore/TheQuizArms)

### Other projects that have give me an inspiration to this project: 


- [Python Django Web Framework - Full Course for Beginners](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=1795s)
- [How to Build an E-commerce Website with Django and Python](https://www.youtube.com/watch?app=desktop&v=YZvRrldjf1Y) 
- [Python Django Ecommerce CRUD and UUID - Managing multiple addresses](https://www.youtube.com/watch?app=desktop&v=8SP76dopYVo)
- [Building an Ecommerce Store with Django and Stripe Payments (Live Coding)](https://www.youtube.com/watch?app=desktop&v=g96MJj2pPg8&fbclid=IwAR3V1bLoN8-Np_HTYjNOfAGSmYmmWBfp0Lxv0IC_QJkxTbYx_EaHGLTfMU8)


## Credits to my mentor

I want to show my gratitude to my mentor at Code Institute, who guided me in this project. 

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