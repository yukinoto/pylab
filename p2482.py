import sys

class card_poll:
	def __init__(self):
		self.poll=input().split()
		return
	def get(self):
		ans=self.poll[0]
		if len(self.poll)>1:
			self.poll=self.poll[1:]
		return ans

class pig:
	id=[]
	n=0
	def __init__(self,pignum):
		cache=input().split()
		self.blood=4
		self.type=cache[0]
		self.card=cache[1:]
		if id==[]:
			for i in range(0,pignum):
				id.append('unknow')
			id[0]='master'
		n=pignum
		return
	def if_dead(self):
		return self.blood==0
	def p(self):
		if 'P' in self.card:
			self.blood+=1
			self.card.remove('P')
			return True
		return False
	def injury(self):
		self.blood-=1
		if self.blood==0:
			if self.p():
				pass
			else:
				raise Exception('dead')
		return
	def d(self):
		if 'D' in self.card:
			self.card.remove('D')
			return True
		return False
	def ask_d(self):
		if self.if_dead():
			raise Exception('dead')
		if self.d():
			pass
		else:
			self.injury()
		return
	def ask_k(self):
		if self.if_dead():
			raise Exception('dead')
		if 'K' in self.card:
			self.card.remove('K')
			return True
		else:
			self.injury()
			return False
	def k(self.target)
