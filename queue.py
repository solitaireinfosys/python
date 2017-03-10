class queue:
	"""Class for Queue Imlementation In Python"""

	__size=0
	__innerqueue=[]	
	
	def __init__(self,size=0):	
		if(size>0):
			self.__size=size
		if(size<0):
			return "Invalid Argument Supplied"
		if(size==0):
			pass

	def push(self,ele):
		if(self.__size==0):
			self.__innerqueue.insert(0,ele)
			return True
		if(self.__size>0):
			if(self.__size>len(self.__innerqueue)):
				self.__innerqueue.insert(0,ele)
			if(self.__size==len(self.__innerqueue)):
				return "Queue Full"
		if(self.__size<0):
			return "Invalid Queue"

	def pop(self):
		if(len(self.__innerqueue)>0):
			return self.__innerqueue.pop()
		else:
			return "Invalid Operation, Queue is Empty"

	def count(self):
		if(len(self.__innerqueue)>0):
			return len(self.__innerqueue)
		else:
			return 0

	def peek(self):
		if(len(self.__innerqueue)>0):
			return self.__innerqueue[len(self.__innerqueue)-1]
		else:
			return "Invalid Operation, Queue is Empty"



	def size(self,newsize=False):
		if(newsize==False):
			if(self.__size > 0):
				return self.__size
			else:
				return "Size not defined" 
		if(newsize!=False):
				self.__size=newsize
				return True


	def isEmpty(self):
		if(len(self.__innerqueue) ==0):
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
			if(len(self.__innerqueue) ==self.__size):
				return True
			else:
				return False		
		else:
			return True
