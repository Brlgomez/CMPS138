@auth.requires_login()
def index():
    grid = SQLFORM.smartgrid(db.image,linked_tables=['post'],deletable=False,editable=False,csv=False,create=False)
    return dict(grid=grid)
    #images = db().select(db.image.ALL, orderby=db.image.title)
    #return dict(images=images)

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
    db.post.image_id.default = image.id
    form = SQLFORM(db.post)
    if form.process().accepted:
        response.flash = 'your comment is posted'
    comments = db(db.post.image_id==image.id).select()
    return dict(image=image, comments=comments, form=form)

@auth.requires_login()
def download():
    return response.download(request, db)

def user():
    return dict(form=auth())

@auth.requires_membership('Manager')
def manage():
    grid = SQLFORM.smartgrid(db.image,linked_tables=['post'])
    return dict(grid=grid)
