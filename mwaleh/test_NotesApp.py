from unittest import TestCase
import NotesApp

class NotesAppTest (TestCase):
	#Arbitrary Strings
	Note1 = 'This is the first note I save in my Notes application'
	Note2 = 'The moment I tried Python programming, I realized it wa the best thing that ever was.'
	Note3 = 'Cultivate the habit of speaking well of others'
	Note4 = 'Dwell upon the good qualities of those with whom you associate, and see as little as possible of their errors and failings.'
	Note5 = 'When tempted to complain of what some one has said or done, praise something in that person\'s life or character. Cultivate thankfulness.'
	Note6 = 'raise God for His wonderful love in giving Christ to die for us. It never pays to think of our grievances.'
	Note7 = '5 + 7'
	Note8 = '[this is a list]'

	#Error Messages
	CreateErMsg = 'The App should Add the entry specified'
	GetErMsg = 'The App should give the user the Expected Note'
	DelErMsg = 'The App Failed the Delete Test'
	EditErMsg = 'The App Failed the Edit Test. Check again.'
	ListErMsg = 'The App should give a list of all the notes.'
	SearchErMsg = 'The App did not pass the Search Test.'
	EditErMsg = 'The App did not pass the Edit Function Test'

	def TestCreate1(self):
		''' Tests the create funcion of the NotesApp '''
		self.assertEqual(create(NotesAppTest.Note1), [NotesAppTest.Note1], NotesAppTest.CreateErrMsg)

	def TestCreate2(self):
		self.assertEqual(create(NotesAppTest.Note2), [NotesAppTest.Note1, NotesAppTest.Note2], NotesAppTest.CreateErrMsg)

	def TestCreate3(self):
		self.assertEqual(create(NotesAppTest.Note3), [NotesAppTest.Note1, NotesAppTest.Note2, NotesAppTest.Note3], NotesAppTest.CreateErrMsg)

	def TestCreate4(self):
		self.assertEqual(create(NotesAppTest.Note7), [NotesAppTest.Note1, Note2, NotesAppTest.Note3, NotesAppTest.Note7], NotesAppTest.CreateErrMsg)

	def TestCreate5(self):
		self.assertEqual(create(NotesAppTest.Note8), [NotesAppTest.Note1, NotesAppTest.Note2, NotesAppTest.Note3, NotesAppTest.Note7, NotesAppTest.Note8], NotesAppTest.CreateErrMsg)

	def TestList(self):
		'''Tests the List function of the NotesApp '''
		for ids in range(len(NotesApplication.notes_list)):
			self.assertEqual(List(), 'The ID of this note is: %d'%(ids), NotesAppTest.ListErMgs)

	def TestGet1(self):
		'''Tests the Get Function '''
		self.assertEqual(get(2), NotesAppTest.Note3, NotesAppTest.GetErMsg)

	def TestGet2(self):
		self.assertEqual(get(25),'note with id 25 doesn\'t exist', NotesAppTest.GetErMsg)

	def TestSearch1(self):
		'''Tests the Search Function '''
		search_text = NotesAppTest.Note1[1:5]	#slices a part of note1 to make sure we have some valid search
		for ids in range(len(NotesApplication.notes_list)):
			found = NotesApplication.notes_list[ids].find(search_text)
			if found != -1:
				self.assertEqual(search(search_text), 'The ID of this note is: %d' %(ids), NotesAppTest.SearchErMsg)

	def TestSearch2(self):
		'''Tests the Search Function when search gets nothing'''
		search_text = 'nl3*((#0?|X|!#_/*'		#There are none in a million chances that one will write this as notes
		for ids in range(len(NotesApplication.notes_list)):
			found = NotesApplication.notes_list[ids].find(search_text)
			if found != -1:
				found += 1
		if found == 3 * -1:						#If this is true then it means the string search never returned anything
			self.assertEqual(search(search_text), None, NotesAppTest.SearchErMsg)

	def TestDelete1(self):
		'''Tests the Delete Function'''
		del_list1 = NotesApplication.notes_list.remove(NotesApplication.notes_list[1])
		self.assertEqual(delete(1),del_list1 == NotesApplication.notes_list, NotesAppTest.DelErMsg)

	def TestDelete2(self):
		self.assertEqual(delete(65), 'note with id 65 does\'t exist', NotesAppTest.DelErMsg)

	def TestEdit1(self):
		'''Tests the Edit function of the app '''
		ed_id = len(NotesApplication.notes_list) -1	#this ensures that the id passed into the test function is valid
		NotesApplication.notes_list[ed_id] = 'This is the new string that changes the value at index'
		self.assertEqual(Edit(ed_id), 'This is the new string that changes the value at index', NotesAppTest.EditErMsg)

	def TestEdit2(self):
		'''Tests the Edit function of the app '''
		ed_id = len(NotesApplication.notes_list) + 2	#this ensures that the id passed into the test function is valid
		self.assertEqual(Edit(ed_id), 'note with id %d doesn\'t exist' %(ed_id), NotesAppTest.DelErMsg)
