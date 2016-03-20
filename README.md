# CMPS183
Web Applications

The World-Wide Web is one of the main mechanisms by which computer applications are delivered to users. This course provides an introduction to the design of Web applications. Students learn the main technologies involved, and build web applications as part of homework assignments and group class projects. Prerequisite(s): course 12B and 12M. (General Education Code(s): PR-E (Practice: Collaborative Endeavor)).

  HW1:

Using the Image Blog example in the web2py book as a guideline, build a for-sale listing site in web2py. The data model is slightly more complex than in the Image Blog but not all that much.
Requirements
For-Sale Listings
A for-sale listing should contain at least the following information:
Seller name and contact info (email/phone/ …)
Date posted
Listing title
Listing description
Optional: listing image
Listing category: one of Car, Bike, Book, Music, Outdoors, Household, Misc.
Price
Listing status: sold or still available
User actions
View all items
Add an item, if user is logged in.
[Bonus: View all still available items]
Resources and Advice
Storing Data (Model)
Uploading images. Follow the approach in the Image Blog example.
Listing status. Use a ‘boolean’ field type with default False. 
Note: (Boolean value False must capitalized in Python.)

Contact info. Must include email and phone number. To validate these data items, use validators.
For email, there is a predefined validator IS_EMAIL. For phone numbers, use the IS_MATCH validator with an appropriate regular expression.

Listing price. Use a ‘double’ field type.
Use db.forsale.price.requires = IS_FLOAT_IN_RANGE(0, 100000.0, error_message='The price should be in the range 0..100000')  validator. 

Listing category. Use a validator of the form described here, something like
db.forsale.category.requires = IS_IN_SET("Car", "Bike", ...)


User registration and authentication. Review Chapter 9, Access Control, of the web2py book.
(it may also help to take a look at the Welcome application, especially the model file db.py). 
How to enforce user login before adding a listing see in particular the section on Decorators. 

Controller and Views
To display the listing items and to add listings you can use SQLFORM.grid as described here.  It may be useful to also review the section Model-View-Controller in the web2py book.

  HW2:
  
For-Sale Listings
Update your For-Sale Listings data model as follows:
Allow any number of images for each listing
Add an integer-valued ratings attribute to the data for sellers, initially set to zero.
Update the For-Sale listing view as follows:
Show the images associated with a listing as a table of thumbnails
Show the current rating for the seller of each listing, and a thumbs-up and a thumbs-down button or image to increase or decrease the rating
User actions
Update the user actions as follows:
Users that are logged in can click the thumbs-up button or image to increase the rating of the seller (by one for each click), and the thumbs-down button to decrease the rating of a seller (by one for each click). Update the seller rating without reloading the entire page.
Clicking on the thumbnail of an image will display a larger version of the image.
Resources and Advice
Storing Data (Model)
Image thumbnails. See http://www.w3schools.com/bootstrap/bootstrap_images.asp for classes and techniques for dealing with images using Bootstrap.
Model for images. Use a separate table for all images; link each image record via a foreign key to the corresponding listing record. To display the images for a listing, you need to select the image records from the image table whose foreign listing key equals the id of the desired listing.

Updating the seller rating. See the testjquery and testajax apps discussed in class (and available on Piazza > Resources > General Resources) for using web2py’s ajax function to accomplish this.
A couple of wrinkles to pay attention to:
A user must be logged in to change seller ratings.
At a minimum, ensure that the ratings display gets update for the listing in which a user clicks the thumbs-up or thumbs-down button/image. A better solution ensures that the ratings display gets updated in all listings for that seller (a seller may have multiple listings).
