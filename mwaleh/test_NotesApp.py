from unittest import TestCase
import NotesApp

class NotesAppTest (TestCase):
	Note1 = 'This is the first note I save in my Notes application'
	Note2 = 'The moment I tried Python programming, I realized it wa the best thing that ever was.'
	Note3 = 'Cultivate the habit of speaking well of others'
	Note4 = 'Dwell upon the good qualities of those with whom you associate, and see as little as possible of their errors and failings.'
	Note5 = 'When tempted to complain of what some one has said or done, praise something in that person\'s life or character. Cultivate thankfulness.'
	Note6 = 'raise God for His wonderful love in giving Christ to die for us. It never pays to think of our grievances.'
	Note7 = '5 + 7'
	Note8 = '[this is a list]'

	def TestCreate1(self):
		''' Tests the create funcion of the NotesApp '''
		self.assertEqual(create(Note1), [Note1], 'The note was not created successfully')

	def TestCreate2(self):
		self.assertEqual(create(Note2), [Note1, Note2], 'The App should Add another Entry')

	def TestCreate3(self):
		self.assertEqual(create(Note3), [Note1, Note2, Note3], 'The App should Add another Entry')

	def TestCreate4(self):
		self.assertEqual(create(Note7), [Note1, Note2, Note3, Note7], 'The App should Add another Entry')

	def TestCreate5(self):
		self.assertEqual(create(Note8), [Note1, Note2, Note3, Note7, Note8], 'The App should Add another Entry')

	def TestList(self):
		'''Tests the List function of the NotesApp '''
		pass

	def TestGet1(self):
		'''Tests the Get Function '''
		self.assertEqual(get(2), Note3, 'The App should give the third note')

	def TestGet2(self):
		self.assertEqual(get(25),'note with id 25 doesn\'t exist','The App should remain silent if the key is above range')

	def TestSearch(self):
		'''Tests the Search Function '''
		pass

	def TestDelete1(self):
		'''Tests the Delete Function'''
		del_list1 = NotesApplication.notes_list.remove(NotesApplication.notes_list[1])
		self.assertEqual(delete(1),del_list1 == NotesApplication.notes_list, 'Your app failed the delete function')

	def TestDelete2(self):
		self.assertEqual(delete(65), 'note with id 65 does\'t exist', 'Your app failed to attempt to delete what isn\'t in the notes')

	def TestEdit(self):
		'''Tests the Edit function of the app '''
		pass



