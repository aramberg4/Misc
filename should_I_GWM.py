def main():
	enemyAC = 0
	attackMod = 0
	maxSD = 8

	print
	print "Hello Wulfgar, we know math can be hard sometimes."   
	print "That's why we made this nifty little tool to help" 
	print "calculate the probability of landing a Great Weapon Master attack." 
	print "Please provide the following info and we'll give you the odds."
	print

	enemyAC = input("Enemy's AC: ")
	attackMod = input("Your attack modifier: ")
	maxSD = input("Highest Superiority Dice Roll: ")
	print
	calculateProbability(enemyAC, attackMod, maxSD)


def calculateProbability(enemyAC, attackMod, maxSD):
	MAX_ROLL = 20.00
	GWM_PENALTY = 5.00
	MIN_ROLL = 1.00
	probability = 0.00
	float(enemyAC)
	float(attackMod)
	float(maxSD)

	rawProbability = ((MAX_ROLL - enemyAC + attackMod + MIN_ROLL) / MAX_ROLL) * 100
	print "Raw probability of hitting: " + str(rawProbability) + "%"
	print

	GWMProbability = ((MAX_ROLL - enemyAC + attackMod + MIN_ROLL - GWM_PENALTY) / MAX_ROLL) * 100
	print "Probability of hitting using GWM: " + str(GWMProbability) + "%"
	print

	SDGWMProbabilityLow = ((MAX_ROLL - enemyAC + attackMod + MIN_ROLL - GWM_PENALTY + MIN_ROLL) / MAX_ROLL) * 100
	SDGWMProbabilityHigh = ((MAX_ROLL - enemyAC + attackMod + MIN_ROLL - GWM_PENALTY + maxSD) / MAX_ROLL) * 100
	print "Probability of hitting using GWM and Superiority Dice is between " + str(SDGWMProbabilityLow) + "% and " + str(SDGWMProbabilityHigh) + "%"
	print

if __name__=="__main__":
   main()
