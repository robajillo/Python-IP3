from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from ..models import  User,Pitch,Comment
from .forms import UpdateProfile,PitchForm,CommentForm
from .. import db,photos
import markdown2


@main.route('/')
def index():
    # user = User.query.filter_by(username='uname').first()
    pitches = Pitch.query.all()
    promotion = Pitch.query.filter_by(category = 'Promotion').all()
    # job = Pitch.query.filter_by(category = 'Job').all() 
    business = Pitch.query.filter_by(category = 'Business').all()
    # promotion = Pitch.query.filter_by(category = 'Promotion').all()
    return render_template('index.html',promotion=promotion,business=business,pitches=pitches)

@main.route('/pitches')
def pitch():
    # user = User.query.filter_by(username='uname').first()
    pitches = Pitch.query.all()
    promotion = Pitch.query.filter_by(category = 'Promotion').all()
    # job = Pitch.query.filter_by(category = 'Job').all() 
    business = Pitch.query.filter_by(category = 'Business').all()
    # promotion = Pitch.query.filter_by(category = 'Promotion').all()
    return render_template('pitch.html',promotion=promotion,business=business,pitches=pitches)

    
      
    

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pitch/new', methods=['GET','POST'])
@login_required
def new_pitch():

    form = PitchForm()
    
    if form.validate_on_submit():

        pitch = form.pitch.data
        category = form.category.data
        
        
        new_pitch = Pitch(pitch = pitch,category = category,user = current_user)
        new_pitch.save_pitch()
        

        return redirect(url_for('main.index'))

    return render_template('new_pitch.html',pitch_form=form)

# @main.route('/business/<uname>', methods=['GET','POST'])
# def business(uname):
#     pitch_form = Pitch()
#     user = User.query.filter_by(username = uname).first()
#     if pitch_form.validate_on_submit():

#         pitch = Pitch(title = pitch_form.title.data,category = pitch_form.category.data, description = pitch_form.description.data,user = user)
#         db.session.add(pitch)
#         db.session.commit()
#         return redirect(url_for('main.index'))
#     title='Pitches'
#     return render_template('pitch.html',title=title,pitch_form=pitch_form)

@main.route('/pitches/comments/<int:pitch_id>', methods=['GET','POST'])
@login_required
def new_comment(pitch_id):
    comment_form = CommentForm()
    comment = Comment.query.filter_by(pitch_id=pitch_id).all()
    if comment_form.validate_on_submit():
        comments = comment_form.comment.data
        
        pitch_id = pitch_id
        new_comment = Comment(comment=comment,pitch_id=pitch_id,user_id=current_user)
        new_comment.save_comment()
        return redirect(url_for('main.index',comment_form=comment_form,pitch_id=pitch_id))

    return render_template('comment.html',comment_form = comment_form,comment=comment,pitch_id=pitch_id) 
    

    