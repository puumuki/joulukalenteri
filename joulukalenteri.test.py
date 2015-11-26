import unittest
import joulukalenteri
	

class TestJoulukalenteri(unittest.TestCase):
 
    def test_joulukalenteri(self):
    	jaot = joulukalenteri.jako(['Teemu','Juha','Anna'])
        self.assertIn( 'Teemu' , jaot.keys() )
        self.assertIn( 'Anna' , jaot.keys() )
        self.assertIn( 'Juha' , jaot.keys() )
        paivat = jaot['Teemu'] + jaot['Anna'] + jaot['Juha']
        self.assertEqual(len(paivat),24)

        for x in xrange(1,25):
        	self.assertIn(x, paivat)
 
if __name__ == '__main__':
    unittest.main()

