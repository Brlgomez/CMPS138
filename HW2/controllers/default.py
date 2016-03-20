@auth.requires_login()
def index():
    #grid = SQLFORM.smartgrid(db.image,linked_tables=['post'],deletable=False,editable=False,csv=False,create=False)
    #return dict(grid=grid)
    #for row in db().select(db.image.ALL):
    images = db().select(db.image.ALL, orderby=db.image.title)
    #picture = db(db.morePictures.image_id==row.id).select()
    picture = db().select(db.morePictures.ALL)
    return dict(images=images, picture=picture)

@auth.requires_login()
def user_items():
    grid = SQLFORM.smartgrid(db.image,linked_tables=['post'],deletable=False,field_id=None,csv=False,create=False)
    return dict(grid=grid)

@auth.requires_login()
def post_item():
    form = SQLFORM(db.image)
    if form.process().accepted:
        response.flash = 'your item is posted'
    return dict(form=form)

def show():
    image = db.image(request.args(0,cast=int)) or redirect(URL('index'))
    db.morePictures.image_id.default = image.id
    form = SQLFORM(db.morePictures)
    if form.process().accepted:
        response.flash = 'your picture is posted'
    picture = db(db.morePictures.image_id==image.id).select()
    return dict(image=image, picture=picture, form=form)

@auth.requires_login()
def download():
    return response.download(request, db)

def upvote():
    image = db.image[request.vars.id]
    new_votes = image.votes + 1
    image.update_record(votes=new_votes)
    return str(new_votes)

def downvote():
    image = db.image[request.vars.id]
    new_votes = image.votes - 1
    image.update_record(votes=new_votes)
    return str(new_votes)

def user():
    return dict(form=auth())

@auth.requires_membership('Manager')
def manage():
    grid = SQLFORM.smartgrid(db.image,linked_tables=['post'])
    return dict(grid=grid)
