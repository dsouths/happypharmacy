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
