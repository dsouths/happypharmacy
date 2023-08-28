<h2>Portfolio Project 5 - Happy Pharmacy - Ecommerce Website</h2>

- [**UX (User Experience)**](#ux-user-experience)
  - [**User Stories**](#user-stories)
- [**Design and Site Structure**](#design-and-site-structure)
  - [**Functional Structure**](#functional-structure)
  - [**Wireframes**](#wireframes)
- [**Features**](#features)
  - [**Responsive Design**](#responsive-design)
- [**Technologies**](#technologies)
  - [**Languages**](#languages)
  - [**Frameworks and Libraries**](#frameworks-and-libraries)
  - [**Tools**](#tools)
- [**Testing**](#testing)
- [**Deployment**](#deployment)
- [**Credits**](#credits)
  - [**Code**](#code)
  - [**Content**](#content)
  - [**Media**](#media)
  - [**Acknowledgments**](#acknowledgments)

## Introduction

This website is for educational purposes only and the credit card payment functionality is not set up to accept real payments. If testing interactively, you can use card details below. Further information can be viewed via Stripe documentation test page.

- 4242 4242 4242 4242 (Visa)
- Expiration date = Any future date (Example: 12/24)
- CVN = any 3 digits (Example: 132)
- Zip/Postcode = any 5 digits (Example: 90210)

As an online pharmacy operating in Ireland there are regulations that need to be adhered to if site is going into production.  The pharmacy regulator in Ireland is the PSI & more information on requirements for online pharmacies can be found [here](https://www.thepsi.ie/gns/Internet-Supply/Internet_supply_list_overview.aspx). If taken into production all guidelines will be adhered to including registration with the PSI.

![PSI online pharmacy](https://github.com/dsouths/happypharmacy/assets/105642587/7141a6e6-48da-494a-ae8a-7e87968fbfbe)


## Showcase

![amirepsonsive](https://github.com/dsouths/happypharmacy/assets/105642587/23097de1-f4c6-4573-9959-aa829df95ffc)

The deployed [HAPPYPHARMACY](https://happypharmacy-1309edb52292.herokuapp.com/)

The [GitHub repository](https://github.com/dsouths/happypharmacy)



## Project goals

This is my 5th project under the Code Institute Diploma in Full Stack Development program.
This website is a fictional Online Pharmacy selling vitamins, supplements & some healthcare products called HAPPYPHARMACY. It is designed to be responsive and accessible on a variety of devices for the ease of use of the site by potential users.


## UX - User Experience
### User Stories

### Admin 

- As an admin I want a panel to:
  - create a blog post.
  - edit a blog post.
  - delete a blog post.
  
- As an admin I want to be able to:
  - log in so that I can access superuser privileges
    
- As an admin I want a product:
  - upload form so that I can upload products on the site.
  - edit form so that I can edit products on the site.
  - delete so that I can delete products on the site.
 
### User

- As a user I can:
  - create an account so that I can save and secure my details.
  - log in & log out so that I can access my account.
  - view products so that I can choose one to buy.
  - view product details to give more detail about an item.
  - filter feature so that I can filter the products.
  - have a search feature so that I can search the database of products.
  - leave a review on the product so that I can give feedback.
  - have a review edit button so that I can ammend my mistakes.
  - have a review delete button so that I can delete a review.
  - want a shopping bag so that I can add prodcts to it.
  - want an edit bag/delete item button so that I can edit/delete quantity in my shopping bag.
  - I want a total so that I can see the total cost of my shopping bag.
  - want a checkout so that I can checkout securely.
  - want a contact page so that I can send a message to the admin.
  - want a navigation bar that is intuitive so that I can nav the website.
  - FAQ's page so that I can find out more info or common questions users may have
  - have access to a privacy policy so that I can know my rights.
  - can view the social media page so that I can share the site.
  - have a landing page so that I can land at the site homepage.
  - I have system messages so that I can receive feedback on my actions e.g. you have logged in successfully
  - can avail of a responsive design so that I can view the app on mobile or desktop devices.

### Overall Goals
* Create an e-commerceweb application to sell vitamins, supplements & other healthcare products online.
* Create & allow a superuser access to full CRUD (create, read, update and delete) functionality on reviews and products
* Supply users to with a targeted product selection functionality to create smooth customer experience when shopping.

### Strategy
* Happy Pharmacy is focused on selling B2C products to end users. Habits of the consumers have changed in the last number of years with more consumers being more health conscious & the vitamin & supplement industry booming with over €31m spent in Ireland in 2023 already. This is where Happy Pharmacy aims to benefit consumers by offering in demand products direct to their door.

### Site User / Target Audience / Demographic
* Target market is aimed at health conscious individuals who like to look after themselves & family/friends.
* People with healthcare needs. I have provided a few products in the "Pharmacy" sections under Allergy, Eye & Ear, Oral Care & First Aid. I plan to develop these further & include more products if the site is to be taken into production. The few products included give an idea of how the site could benefit users & how product range could be expanded to include other ailments  

### Site Goals
* The site's main purpose is immediately clear, "Happy Pharmacy" to help users "Nourish, Thrive, and Glow" by buying vitamins & supplements to optimize their body's nutrional needs.
* Simple navigation that allows the user to find information and resources intuitively
* User authentication
* CRUD functionality for superuser(s)

## Architecture
### Database Schema

![Happy Pharmacy - database schema](https://github.com/dsouths/happypharmacy/assets/105642587/5cb0f8db-930a-4c58-a48b-edd8fc3a6e1f)

## Design

### Wireframes
### Mobile Nav

![mobile navbar](https://github.com/dsouths/happypharmacy/assets/105642587/4012010e-e01d-41d5-be52-76639fce5c58)


### Homepage

![HP - landing page ](https://github.com/dsouths/happypharmacy/assets/105642587/b7c35d15-ea72-4cfa-9521-4ce4e5ce62ca)


### Products

![HP - products page ](https://github.com/dsouths/happypharmacy/assets/105642587/28f9e72a-44d0-4227-a62b-5f60d0a24ecc)


### Product Detail

![HP - product detail page ](https://github.com/dsouths/happypharmacy/assets/105642587/1713ffa0-5216-4ade-ba56-7ccec27d8d43)


### Contact

![HP - contact   testimonials page ](https://github.com/dsouths/happypharmacy/assets/105642587/ff33569b-5c68-4948-aaba-0e381a178c8e)


## Navigation

![HP - Entity Relationship Diagram ](https://github.com/dsouths/happypharmacy/assets/105642587/4bf42687-da7b-4137-a4ed-888009299b07)


## Colour Pallete

![colos co](https://github.com/dsouths/happypharmacy/assets/105642587/282e4b51-82c7-4e99-ba08-517e49cae710)

## Typography
The site uses "Montserrat" and "Lato" from Google Fonts.

## Features
### Existing Features
### Homepage

We can see the nav bar along with the authentication options. The hero section has a CTA "buy now" leading users to the products section where they can make a purchase. Nav bar and footer are visible here. The user can also sign up to the mailing list.
Landing page (top)
![landing page (top)](https://github.com/dsouths/happypharmacy/assets/105642587/0c6f0b2a-1c02-4906-a001-b199ab1fb0e9)

Landing page (bottom)
![landing page (bottom)](https://github.com/dsouths/happypharmacy/assets/105642587/eed65b2a-5ea2-453a-abe3-6d44c3836c64)

### Products
Here products are listed. Clicking the item image leads to the product detail page & out of stock items are marked to inform the user

![products page](https://github.com/dsouths/happypharmacy/assets/105642587/dd5d6da5-cd03-434c-9fcf-005fb6f607b1)

### Product Detail
Here is the more detailed view of the product. Superusers can edit or delete a product. Logged in users can review a product, which are displayed at the bottom of the page, if the admin approves it.  I have used Javascript to make sure that the buttons don't let you add more items than are in stock. The issue with this is that if you reload the page, you can add them again. Products are not removed from the inventory until sold. 

![product detail page](https://github.com/dsouths/happypharmacy/assets/105642587/638d6cf3-acc1-440b-acbc-43293b53c59a)

### Contact

Contact/testimonial form that stores messages/testimonials in the database. This can only be accessed if the user is logged in.

![contact us_testimonial page](https://github.com/dsouths/happypharmacy/assets/105642587/db83db42-f75f-4cc5-a440-a276b80a084d)

### FAQs
I have included the page to improve SEO for the site & inform the user if they may have any questions about some of the products sold or general health care areas. This will improve the overall usefulness of the site to the user

![faq page](https://github.com/dsouths/happypharmacy/assets/105642587/d1a62544-d467-4a37-a6ee-d22c796a0d09)

### Profile
Users profile info. Their default address will auto fill at checkout. This can also be amended by the user if necessary.

![my profile page](https://github.com/dsouths/happypharmacy/assets/105642587/3b6d7c75-baac-4cdd-b894-58dd6d8af0d0)

### Shopping Bag
Items placed in the bag are displayed and the checkout can be accessed from here. I have added logic so that if the user has more product quantity than is in stock, the product quantity will be reduced to the number left in stock and a message displayed.

![shopping bag ](https://github.com/dsouths/happypharmacy/assets/105642587/3cfd109d-5bb6-43ef-929d-c6261ee5192a)

### Checkout
Fill out personal & payment details to buy the products in the bag. Test values noted above can be used to make a payment. 

checkout (top)
![checkout (top)](https://github.com/dsouths/happypharmacy/assets/105642587/e8432934-a988-45fd-b485-2c761f5f1cb3)

checkout (bottom)
![checkout (bottom)](https://github.com/dsouths/happypharmacy/assets/105642587/6cc66972-22bf-4e3b-8c4a-1e0058f27e96)

### Checkout Success
If Order was successfully placed a confirmation email is sent. This logic is triggered by Stripe webhooks ensuring that the order is created should the user close the page during payment processing. 

![checkout success](https://github.com/dsouths/happypharmacy/assets/105642587/d7acbef8-564e-4a94-ac65-78d733ed60f9)

### Product Management
Admin can add a product & include all necessary details price, pack size, stock quantity, image, etc

![product management](https://github.com/dsouths/happypharmacy/assets/105642587/4060168e-be7e-4e14-84f0-f23e7e9663c4)

### Log In

![sign in ](https://github.com/dsouths/happypharmacy/assets/105642587/f709d645-dfae-44e2-8ee7-945d3eb7caf9)


### Log Out

![sign out](https://github.com/dsouths/happypharmacy/assets/105642587/a17743ed-bde5-488e-b935-3aa42f62db6d)


### Sign Up

![sign up](https://github.com/dsouths/happypharmacy/assets/105642587/6b91dbe3-7375-4ee0-b2d4-274e4bdd65ea)


### Forgot Password
![forgot password](https://github.com/dsouths/happypharmacy/assets/105642587/b89a735b-99d2-4874-809b-a274056c5c53)


## Web Marketing / Marketing Strategies
### SEO

I used Google keyowrd search to research words associated with Pharmacy, Vitamins & Supplements to help otimise pages & content in the FAQs to increase ranking in search engine. Both long & short-tail words were used. 

![SEO](https://github.com/dsouths/happypharmacy/assets/105642587/a47b571a-867f-4034-849f-459be744e16d)

### Social Media Marketing

I created a Facebook business page to help generate growth organically by building a community of interested customers/user and encourage loyalty amongst our target market. It is free and quick to set up a Facebook page, it has a large audience & a business can connect with customers directly via the Facebook platform and wider global audience, quite easily. The main aim of the Facebook page is to build and maintain relationship with target audience by creating content that will engage them.

![HP facebook](https://github.com/dsouths/happypharmacy/assets/105642587/1945d0a6-22df-45a1-8b74-b3ae99e51fb0)

### Email Marketing

Mailchimp provides an effective platform for gaining new customers and retaining existing ones through newsletter campaigns. By tracking signups and engagement, Mailchimp allows us to monitor the performance of our marketing efforts. Customers/users must opt-in to receive our newsletter, & are automatically enrolled in weekly mail outs. This strategy was chosen because its free to set up with the current level of business and can scale quickly as the business grows therefore increase conversions and generate more revenue for the business. Overall, Mailchimp enables us to boost conversions and revenue through targeted email marketing, with no or minimal upfront investment.

### Frameworks, Libraries & Programs Used

* [amiresponsive](http://ami.responsivedesign.is/) to see how responsive the site is on different devices.
* [Balsamiq](https://balsamiq.com/) was used to create the Wireframes.
* [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) v4.6 was used to help build responsive, mobile-first design.
* [Color-hex](https://www.color-hex.com/) once I identified the colors I wanted I used color-hex to generate the palette.
* [Django](https://www.djangoproject.com/) free and open-source, Python-based web framework that follows the model–template–views architectural pattern.
* [Font Awesome](https://fontawesome.com/) was used for icons for aesthetic and UX purposes on the buttons.
* [Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub](https://github.com/) GitHub is used to store the projects code after being pushed from Git.
* [Gitpod](https://www.gitpod.io/) An online IDE linked to the GitHub repository used to write my code.
* [Google Chrome Dev tools](https://developer.chrome.com/docs/devtools/) for debugging.
* [Google Fonts](https://fonts.google.com/about) for typography.
* [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) used for audits to measure the quality of web pages.
* [Google Keyword Planner](https://ads.google.com/aw/keywordplanner/home?)
* [Heroku](https://www.heroku.com/) used to deploy this app, a cloud platform as a service supporting several programming languages.
* [Pexels](https://www.pexels.com/) Images for this project were sourced from Pexels.
* [Privacy Policy Generator](https://www.privacypolicygenerator.info/) Free Privacy Policy Generator.
* [Meaghers Pharmacy](www.meaghers.pharmacy.ie) - images were taken borrowed from this website for educational purposes only. If taken into production all appropriate copyrights will be adhered to 
* [Stripe](https://stripe.com/en-ie) Integrated with Stripe to facilitate online payments.
* [SQLite](https://www.sqlite.org/index.html) database used in local development was a SQLLite database.
* [Terms and Conditions Generator](https://www.termsandconditionsgenerator.com/) Free terms and conditions generator.
* [Unsplash](https://unsplash.com/) Images for this project were sourced from Unsplash.
* [WAVE](https://wave.webaim.org/extension/) Browser Extension testing.
* [Wordtracker](https://www.wordtracker.com/)
* [a11y](https://color.a11y.com/) Color Contrast Accessibility Validator.


## Testing
### Lighthouse


### HTML Validation
HTML files that have been validated with W3.
- index.html
- products.html
- product_detail.html
- bag.html
- checkout.html
- checkout_success.html
- contact.html
- profiles.html
- 404.html

### W3C CSS Validator
W3C CSS Validator user to ensure there were no errors or warnings present.

### Python Validation
Autopep8 to validate all the Python files and checked them with Flake8.

### JSHint
JS files checked with JSHint for conformity.

### Color Contrast Accessibility Validator
The site passed the color contrast test on https://color.a11y.com/ 

Here is the test cases rewritten for an online pharmacy website called Happy Pharmacy:

| Feature | Test  | Expected Result | Actual Result |
|-|-|-|-|  
| Happy Pharmacy logo | Selecting logo on homepage | directs user back to homepage | Pass |
| Navigation Links | Selecting navigation links | directs user to relevant categories & pages | Pass | 
| All categories | Selecting All for each category | directs user to show all relevant categories on the same page | Pass |
| Sort By | Selecting the filter Sort by for each category | successfully alters the search by price, name and category options reflects results accordingly on page | Pass |
| Contact Us | Selecting Contact Us | directs user to Contact Us page | Pass |
| Buy Now | Selecting Buy Now | directs user to full products list page | Pass | 
| Submitting Review Form | Editing details in review form on Products | successfully edits message to admin and displays success message | Pass |
| Submitting Edit Review Form | Submitting details in review form on Products | successfully sends message to admin and displays success message | Pass |
| User Access | Logged in as user | I can leave a review comment on products | Pass |
| User Access | Logged in as user and author | I can edit a review comment on products | Pass | 
| User Access | Logged in as user and author | I can delete a review comment on products | Pass |
| Form Validation Required fields | Filling in form on /contact page | requires name, email and body and contact reason selected to send to Django admin | Pass |
| Contact form submission | submit contact form | successfully sends data to Django admin as expected | Pass |
| Register | Register for an account | selecting Register in my account directs user to /accounts/signup/ page | Pass |
| Login | Login to an account | selecting Login in my account directs user to /accounts/Login/ page | Pass |
| Search | Using the search box | Entering a search returns expected result | Pass |
| Back to top | Back to top box | Selecting the back to top box on the products pages brings the user back to the top of the page | Pass | 
| Search no results | No search results | Entering a no results search returns error message and shows all products | Pass |
| New User | Registering as a new user | Registering as a new user entering form validation works | Pass |
| Admin | Logging in as superuser / admin | Logging in as superuser / admin directs user to admin access, shows product management page | Pass |
| Login Message | log-in Success | "successfully signed in as (user name)" message shown to user | Pass |
| Add Product | Adding a new product | Adding a new product on the product management page successfully adds product | Pass |
| Add Product | no image is selected | default image is used | Pass |
| Deleting Product | Deleting selected product | removed product from search | Pass |
| Deleting Message | Deleting product confirmation | Confirmation message of deletion is shown when successfully deleted | Pass |
| Defensive Programming | Test for SQL Injection attacks | Users not permitted to access create/update/delete products articles or reviews if they don't have access permission | Pass |
| Logging out | message shown | Logging out as a user / admin prompts "are you sure" message | Pass |
| Successfully signed out | signed out message shown | "You have signed out" message shows to user when successfully signed out | Pass |
| Logging out | Logging out and redirect | Logging out as a user / admin directs user to homepage | Pass |
| Footer | social media links | Clicking on the social media icons in the footer open the link in a new tab | Pass |
| Footer | Privacy Policy links | Clicking on the Privacy Policy link in the footer diverts user to the /privacy/ page | Pass |

### Responsiveness Browser Compatibility

|  | Chrome | Firefox | Edge | Safari | Pass/Fail |
| ------------- |-------------| -----|  ---------- |  -----| :----: |
| Expected Appearance   | yes | yes  | yes  | yes | Pass |
| Expected Layout   | yes | yes  | yes  | yes | Pass |

## Bugs / Errors encountered during development

Many many bugs were encountered along the way, here are a few examples:
- 
