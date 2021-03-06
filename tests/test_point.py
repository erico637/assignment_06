import unittest
import random
from .. import point
  
class TestPointClass(unittest.TestCase):
      def setUp(self):
         self.marks = ['Luke', 'Leia', 'Han', 'Chewbacca', 'ObiWan',
                 'Vader', 'Yoda', 'Lando', 'Ackbar', 'Palpatine',
                 'Boba', 'Jabba', 'Piett', 'Wedge', 'Porkins']
                 

      def test_set_coords(self):
          _x = 5
          _y = 120
          point0 = point.Point(_x, _y, random.choice(self.marks))
          self.assertEqual(_x, point0.getx())
          self.assertEqual(_y, point0.gety())
          
      def test_check_coincident(self):
          _x = 5
          _y = 120
         point0 = point.Point(_x, _y, random.choice(self.marks))
         point1 = point.Point(5, 120, random.choice(self.marks))
         point2 = point.Point(_x+3, _y, random.choice(self.marks))
         point3 = point.Point(_x, _y+22, random.choice(self.marks))
         point4 = point.Point(_x+3,_y+22, random.choice(self.marks))
         self.assertTrue(point0.check_coincident(point1.getPoint()))
         self.assertFalse(point0.check_coincident(point2.getPoint()))
         
     def test_shift(self):
          _x = 5
          _y = 120
          point0 = point.Point(_x, _y, random.choice(self.marks))
          point0.shift_point(816, 80085)
          self.assertEqual((_x + 816, _y + 80085), point0.getPoint())
          
     def test_marked_points(self):
         random.seed(12345) 
         randmarks = list()
          for x in range(20):
              randmarks.append(random.choice(self.marks))
  
          randmarkcnt = dict()
          for x in range(len(randmarks)):
