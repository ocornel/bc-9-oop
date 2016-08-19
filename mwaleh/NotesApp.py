class NotesApplication(object):
	notes_list = []
	author = 'Cornel'
	def __init__(self):
		pass
	
	def create(self, note_content):
		note_content = str(note_content)
		NotesApplication.notes_list.append(note_content)
		return NotesApplication.notes_list

	def list(self):
		author = NotesApplication.author
		for ids in range(len(NotesApplication.notes_list)):	#instead of print use return
			print ('Note ID: \t %d\n%s\n\nBy Author %s\n-------------------' %(ids, NotesApplication.notes_list[ids], author) )
			print()
			return 	'The ID of this note is: '+ids

	def get(self, note_id):
		if NotesApplication.notes_list[note_id] in NotesApplication.notes_list:
			return NotesApplication.notes_list[note_id]
		else:
			return ('note with id %d doesn\'t exist' %(note_id))

	def search(self, search_text):
		author = NotesApplication.author
                
		for ids in range(len(NotesApplication.notes_list)):
			found = NotesApplication.notes_list[ids].find(search_text)
			if found != -1:
				print ('Note ID: \t %d\n%s\n\nBy Author %s\n-------------------' %(ids, NotesApplication.notes_list[ids], author) )
				print()	
				return 	'The ID of this note is: '+ids

	def delete(self, note_id):
		if NotesApplication.notes_list[note_id] in NotesApplication.notes_list:
			NotesApplication.notes_list.remove(NotesApplication.notes_list[note_id])
			return ('note with id %d deleted' %(note_id))

		else:
			return ('note with id %d doesn\'t exist' %(note_id))

	def edit(self, note_id, new_content):
		if NotesApplication.notes_list[note_id] in NotesApplication.notes_list:
			NotesApplication.notes_list[note_id] = new_content
			return ('Note with id %d edited' %(note_id))

		else:
			return ('note with id %d doesn\'t exist' %(note_id))