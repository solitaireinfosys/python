class stack:
	"""Class for Stack Imlementation In Python"""

	__size=0
	__innerstack=[]	
	
	def __init__(self,size=0):	
		if(size>0):
			self.__size=size
		if(size<0):
			"Invalid argument"
		if(size==0):
			pass

	def push(self,ele):
		if(self.__size==0):
			self.__innerstack.append(ele)
			return True
		if(self.__size>0):
			if(self.__size>len(self.__innerstack)):
				self.__innerstack.append(ele)
			if(self.__size==len(self.__innerstack)):
				return "Stack Full"
		if(self.__size<0):
			return "Invalid stack"

	def pop(self):
		if(len(self.__innerstack)>0):
			return self.__innerstack.pop()
		else:
			return "Invalid Operation, Queue is Empty"

	def count(self):
		if(len(self.__innerstack)>0):
			return len(self.__innerstack)
		else:
			return 0

	def peek(self):
		if(len(self.__innerstack)>0):
			return self.__innerstack[len(self.__innerstack)-1]
		else:
			return "Invalid Operation, Queue is Empty"


	def size(self,newsize=False):
		if(newsize==False):
			if(self.__size > 0):
				return self.__size
			else:
				return False
		if(newsize!=False):
				self.__size=newsize
				return True


	def isEmpty(self):
		if(len(self.__innerstack) ==0):
			return True
		else:
			return False		


	def isSized(self):
		if(self.__size > 0):
			return True
		else:
			return False		


	def isFull(self):
		if(self.__size>0):
			if(len(self.__innerstack) ==self.__size):
				return True
			else:
				return False		
		else:
			return True
