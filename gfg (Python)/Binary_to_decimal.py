#User function Template for python3

class Solution:
	def binaryToDecimal(self, b):
		# Code here
		decimal = 0
		
		for ch in b:
		    decimal = decimal * 2 + int(ch)
	    return decimal # type: ignore