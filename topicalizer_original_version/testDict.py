# text category
textCategory = 'c'

# initialise text categories dictionary
textCategories = dict(a = 'Press: Reportage',
		      b = 'Press: Editorial',
		      c = 'Press: Reviews',
		      d = 'Religion',
		      e = 'Skill and Hobbies',
		      f = 'Popular Lore',
		      g = 'Belles-lettres',
		      h = 'Miscellaneous: Government & House Organs',
		      j = 'Learned',
		      k = 'Fiction: GeneraL',
		      l = 'Fiction: Mystery',
		      m = 'Fiction: Science',
		      n = 'Fiction: Adventure',
		      p = 'Fiction: Romance',
		      r = 'Humour')

# get text category title
textCategoryTitle = textCategories[textCategory]

print textCategoryTitle
