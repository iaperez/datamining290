from collections import Counter
from collections import defaultdict

#The data was extracted from the movieles dataset, 
#and it is the reviews from the first 17 users
#
# sed -n 1,2184p ratings.dat
#
#
#Then, I retrieved the genres for those movies and
#count the genres per user. (movies.dat)
#
#
#Even when I know that pie charts are mostly useless,
# sometimes they can be useful that the data is too sparsed
#http://people.ischool.berkeley.edu/~iaperez/viz.html
#

usersReviews =  defaultdict(list)
with open('rats.dat') as f:
	for line in f:
		lines = line.split("::")
		userid = lines[0]
		movieid = lines[1]
		usersReviews[userid].append(movieid)

def getGenres(movieid):
	with open('movies.dat') as f:
		for line in f:
			lines = line.split("::")
			if int(lines[0])==int(movieid):
				return  lines[-1].strip().split("|")


userGenres = defaultdict(Counter)
generalGenres = Counter()

for userid in usersReviews:
	for movie in usersReviews[userid]:
		genrelist = getGenres(movie)
		for genre in genrelist:
			generalGenres[genre]+=1
			userGenres[userid][genre]+=1

print"user",
for genre in generalGenres:
	print ","+genre.strip(),
print

for userid in userGenres:
	print str(userid).strip(),
	for genre in generalGenres:
		if genre in userGenres[userid]:
			print ","+str(userGenres[userid][genre]).strip(),
		else:
			print ","+str(0).strip(),
	print

#		print str(userid)+","+genre+","+str(userGenres[userid][genre])
