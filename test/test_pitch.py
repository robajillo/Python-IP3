from app.models import Pitch
from app import db

def setUp(self):
    self.new_pitch = Pitch(1,'Investors','This is a Pitch','Promotion',10)
    
def test_check_instance_variables(self):
    self.assertEquals(self.new_pitch.id,1)
    self.assertEquals(self.new_pitch.pitch,'test pass')
    self.assertEquals(self.new_pitch.category,"Promotion")
    self.assertEquals(self.new_pitch.pitch_title,'investors')
    self.assertEquals(self.new_pitch.user_id,1)
    
def test_save_pitch(self):
    self.new_pitch.save_pitch()
    self.assertTrue(len(Pitch.query.all())>0)
    
def test_get_pitch_by_id(self):

    self.new_pitch.save_pitch()
    got_pitch = Pitch.get_pitch(1)
    self.assertTrue(len(got_pitch) == 1)
    