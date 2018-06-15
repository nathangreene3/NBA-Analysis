



class Player:

	def __init__(self, id=-1, name="none", team="none", fiveStats=[0,0,0,0,0]):
		self.id   = id
		self.name = name
		self.team = team
		self.points   = fiveStats[0]
		self.assists  = fiveStats[1]
		self.steals   = fiveStats[2]
		self.blocks   = fiveStats[3]
		self.rebounds = fiveStats[4]
		self.rank = 0