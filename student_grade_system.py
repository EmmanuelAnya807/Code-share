def main():
	score = input("Enter your score: ")
	score = int(score)
	
	grade_system(score)
	
	print("Submit.")

	
def grade_system(score):
	if score >= 70:
		print("A")
		
	elif score >= 60 and score <= 69:
		print("B")
		
	elif score >= 50 and score <= 59:
		print("C")
		
	elif score >= 45 and score <= 49:
		print("D")
		
	elif score < 45 and score >= 0:
		print("F")
		
	else:
		print("Re-run the program and re-enter the score")
		

main()
