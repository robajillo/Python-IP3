import unittest
from app.models import Comment

# class CommentTest(unittest.TestCase):
class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.new_comment = Comment()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))

# def setUp(self):
#     self.new_comment = Comment(1,'errors be gone','1','1')
    
# def test_check_instance_variables(self):
#     self.assertEquals(self.new_comment.id,1)
#     self.assertEquals(self.new_comment.comment,'errors be gone')
#     self.assertEquals(self.new_comment.pitch_id,1)
#     self.assertEquals(self.new_comment.user_id,1)
    
# def test_save_pitch(self):
#     self.new_comment.save_comment()
#     self.assertTrue(len(Pitch.query.all())>0)
    
# def test_get_comment_by_id(self):

#     self.new_comment.save_comment()
#     got_comment = Comment.get_comment(1)
#     self.assertTrue(len(got_comment) == 1)
    