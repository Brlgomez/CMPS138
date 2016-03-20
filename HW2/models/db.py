db = DAL("sqlite://storage.sqlite")
#db = DAL('sqlite://db.ajaxdb')

db.define_table('image',
   Field('file', 'upload'),
   Field('title', unique=True),
   Field('price', default=0.00),
   Field('for_sale', default=True),
   Field('category'),
   Field('description'),
   Field('date_posted', 'datetime', default = request.now, requires = IS_DATETIME(format=('%d/%m/%Y %H:%M'))),
   Field('name',default='anonymous'),
   Field('contact'),
   Field('votes', 'integer', default=0),
   format = '%(title)s')

db.define_table('morePictures',
    Field('image_id', 'reference image'),
    Field('file', 'upload'))

db.define_table('post',
   Field('image_id', 'reference image'),
   Field('author'),
   Field('email'),
   Field('body', 'text'))

db.image.title.requires = IS_NOT_IN_DB(db, db.image.title)
db.image.price.requires = IS_FLOAT_IN_RANGE(0, 100000, error_message='The price should be in the range 0..100000')
db.image.for_sale.requires = IS_IN_SET(["True", "False"], zero=T('choose one'), error_message='Pick a category')
db.image._format = '%(name)s/%(id)s'
db.image.description.requires = IS_NOT_EMPTY()
db.image.category.requires = IS_IN_SET(["Car", "Bike", "Computer", "Phone", "Furniture","Art", "Music", "Clothing", "Kitchenware", "Games", "Other"], zero=T('choose one'), error_message='Pick a category')
db.image.name.requires = IS_NOT_EMPTY()
db.image.contact.requires = IS_EMAIL()
db.post.image_id.requires = IS_IN_DB(db, db.image.id, '%(title)s')
db.post.author.requires = IS_NOT_EMPTY()
db.post.email.requires = IS_EMAIL()
db.post.body.requires = IS_NOT_EMPTY()


db.post.image_id.writable = db.post.image_id.readable = False
db.morePictures.image_id.writable = db.morePictures.image_id.readable = False
#db.image.rating.writable = False
#db.image.amountOfRating.writable = False

from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=True)
