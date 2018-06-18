# -*- coding: utf-8 -*-
import math
from tkinter import *

class Stack:
	def __init__ (self):
		self.items = []
	def isEmpty (self):
		return self.items == []
	def push (self, item):
		self.items.append (item)
	def pop (self):
		return self.items.pop ()
	def peek (self):
		return self.items [-1]
	def size (self):
		return len (self.items)

class Calculator (Stack):
	s = Stack ()

	exprsn = "0"        #这是当我们按下按钮时会在计算器上显示的表达式
	act_exprsn = ""     #这是程序运行时计算的实际数学表达式
	state = 0           #这个变量表示计算器的状态：0 - 重置或在开始时；1 - 在输入表达式过程中；2 - 计算刚刚完成，结果返回

	def __init__ (self):
		#创建窗口
		self.root = Tk ()
		self.root.title ("科学计算器")
		self.root.resizable (0,0)

		self.calccredit = Label (self.root, text = "\nDesigned by Ankan Poddar", font = "Verdana 7 italic", justify = RIGHT, anchor = "e", width = 40)
		self.calccredit.grid (row = 8, column = 0, columnspan = 6)

		#设置表达式格式
		self.calcexpr = Label (self.root, text = "", font = "Helvetica 13 italic", anchor = "e", width = 25)
		self.calcexpr.grid (row = 0, column = 0, columnspan = 5)
		self.calcexpr.bind ('<KeyRelease>', self.handleKeypress)
		self.calcexpr.focus_set()

		#设置结果格式
		self.calcans = Label (self.root, text = self.exprsn, bg = "white", font = "Helvetica 16", anchor = "e", width = 21, relief = RIDGE)
		self.calcans.grid (row = 1, column = 0, columnspan = 5, pady = 10)

		#0-9按钮
		self.zero = Button (self.root, text="0", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.zero.grid (row = 7, column = 1, pady = 2)
		self.zero.bind ('<Button-1>', lambda event: self.putDigit (event, 0))

		self.one = Button (self.root, text="1", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.one.grid (row = 6, column = 1, pady = 2)
		self.one.bind ('<Button-1>', lambda event: self.putDigit (event, 1))

		self.two = Button (self.root, text="2", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.two.grid (row = 6, column = 2, pady = 2)
		self.two.bind ('<Button-1>', lambda event: self.putDigit (event, 2))

		self.three = Button (self.root, text="3", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.three.grid (row = 6, column = 3, pady = 2)
		self.three.bind ('<Button-1>', lambda event: self.putDigit (event, 3))

		self.four = Button (self.root, text="4", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.four.grid (row = 5, column = 1, pady = 2)
		self.four.bind ('<Button-1>', lambda event: self.putDigit (event, 4))

		self.five = Button (self.root, text="5", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.five.grid (row = 5, column = 2, pady = 2)
		self.five.bind ('<Button-1>', lambda event: self.putDigit (event, 5))

		self.six = Button (self.root, text="6", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.six.grid (row = 5, column = 3, pady = 2)
		self.six.bind ('<Button-1>', lambda event: self.putDigit (event, 6))

		self.seven = Button (self.root, text="7", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.seven.grid (row = 4, column = 1, pady = 2)
		self.seven.bind ('<Button-1>', lambda event: self.putDigit (event, 7))

		self.eight = Button (self.root, text="8", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.eight.grid (row = 4, column = 2, pady = 2)
		self.eight.bind ('<Button-1>', lambda event: self.putDigit (event, 8))

		self.nine = Button (self.root, text="9", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.nine.grid (row = 4, column = 3, pady = 2)
		self.nine.bind ('<Button-1>', lambda event: self.putDigit (event, 9))

		#括号
		self.openpar = Button (self.root, text="(", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.openpar.grid (row = 3, column = 1, pady = 2)
		self.openpar.bind ('<Button-1>', self.putOpenPar)

		self.closepar = Button (self.root, text=")", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.closepar.grid (row = 3, column = 2, pady = 2)
		self.closepar.bind ('<Button-1>', self.putClosePar)

		#常量π、e按钮
		self.pi = Button (self.root, text="π", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.pi.grid (row = 2, column = 3, pady = 2)
		self.pi.bind ('<Button-1>', lambda event: self.putConstant (event, "π", repr (math.pi)))

		self.e = Button (self.root, text="e", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.e.grid (row = 3, column = 3, pady = 2)
		self.e.bind ('<Button-1>', lambda event: self.putConstant (event, "e", repr (math.e)))

		#button for decimal point
		self.decimal = Button (self.root, text=".", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.decimal.grid (row = 7, column = 2, pady = 2)
		self.decimal.bind ('<Button-1>', self.putDecimal)

		#小数点
		self.factorial = Button (self.root, text="!", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.factorial.grid (row = 2, column = 0, pady = 2, padx = (3,0))
		self.factorial.bind ('<Button-1>', self.calcFactorial)
		
                #开方
		self.sqrt = Button (self.root, text="√", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.sqrt.grid (row = 2, column = 2, pady = 2)
		self.sqrt.bind ('<Button-1>', self.calcSqrt)

		#三角函数
		self.sin = Button (self.root, text="sin", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.sin.grid (row = 3, column = 0, pady = 2, padx = (3,0))
		self.sin.bind ('<Button-1>', lambda event: self.putUnaryOper (event, "sin"))

		self.cos = Button (self.root, text="cos", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.cos.grid (row = 4, column = 0, pady = 2, padx = (3,0))
		self.cos.bind ('<Button-1>', lambda event: self.putUnaryOper (event, "cos"))

		self.tan = Button (self.root, text="tan", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.tan.grid (row = 5, column = 0, pady = 2, padx = (3,0))
		self.tan.bind ('<Button-1>', lambda event: self.putUnaryOper (event, "tan"))

		#对数
		self.ln = Button (self.root, text="ln", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.ln.grid (row = 6, column = 0, pady = 2, padx = (3,0))
		self.ln.bind ('<Button-1>', lambda event: self.putUnaryOper (event, "ln"))

		self.log = Button (self.root, text="log", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.log.grid (row = 7, column = 0, pady = 2, padx = (3,0))
		self.log.bind ('<Button-1>', lambda event: self.putUnaryOper (event, "log"))

		#加减乘除、指数
		self.add = Button (self.root, text="+", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.add.grid (row = 7, column = 4, pady = 2, padx = (0,3))
		self.add.bind ('<Button-1>', lambda event: self.putBinaryOper  (event, "+", "+"))

		self.subtract = Button (self.root, text="-", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.subtract.grid (row = 6, column = 4, pady = 2, padx = (0,3))
		self.subtract.bind ('<Button-1>', lambda event: self.putBinaryOper  (event, "-", "-"))

		self.multiply = Button (self.root, text="x", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.multiply.grid (row = 5, column = 4, pady = 2, padx = (0,3))
		self.multiply.bind ('<Button-1>', lambda event: self.putBinaryOper  (event, "*", "x"))

		self.divide = Button (self.root, text="÷", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.divide.grid (row = 4, column = 4, pady = 2, padx = (0,3))
		self.divide.bind ('<Button-1>', lambda event: self.putBinaryOper  (event, "/", "÷"))

		self.exponent = Button (self.root, text="^", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.exponent.grid (row = 2, column = 1, pady = 2)
		self.exponent.bind ('<Button-1>', lambda event: self.putBinaryOper  (event, "^", "^"))

		#清除
		self.allclear = Button (self.root, text="AC", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.allclear.grid (row = 2, column = 4, pady = 2, padx = (0,3))
		self.allclear.bind ('<Button-1>', self.clearAll)

		self.clear = Button (self.root, text="C", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.clear.grid (row = 3, column = 4, pady = 2, padx = (0,3))
		self.clear.bind ('<Button-1>', self.delete)

		#等于
		self.equals = Button (self.root, text="=", font = "Verdana 12", relief = RAISED, bd = 3, width = 2)
		self.equals.grid (row = 7, column = 3, pady = 2)
		self.equals.bind ('<Button-1>', self.evaluate)

		self.root.mainloop ()

	#检查实际表达式列表中的最后一个标记是否是一个数字; 数字返回True，非数字返回False
	def chcknum (self, token):
		try:
			t = float (token)
			return True
		except ValueError:
			return False

	#按键
	def handleKeypress (self, event):
		if event.char in "0123456789":
			try:
				self.putDigit (event, int (event.char))
			except ValueError:
				pass
		elif event.char in "+-*/^":
			oper_sym = {'+': '+', '-': '-', '*': 'x', '/': '÷', '^': '^'}
			self.putBinaryOper (event, event.char, oper_sym [event.char])
		elif event.char == ".":
			self.putDecimal (event)
		elif event.char == '(':
			self.putOpenPar (event)
		elif event.char == ')':
			self.putClosePar (event)
		elif ord (event.char) == 8:
			self.delete (event)
		elif ord (event.char) == 127:
			self.clearAll (event)
		elif ord (event.char) == 13:
			self.evaluate (event)

	#处理数字
	def putDigit (self, event, digit):
		ls = self.act_exprsn.split ()
		if self.state == 0 or self.state == 2:
			self.act_exprsn = repr (digit)
			self.exprsn = repr (digit)
			self.state = 1
		elif len (ls) > 0 and ls[-1] in ')!':
			self.act_exprsn += " * " + repr (digit)
			self.exprsn += repr (digit)
		else:
			self.act_exprsn += repr (digit)
			self.exprsn += repr (digit)
		self.calcans.config (text = self.exprsn)

	#将显示表达式和计算表达式进行转换
	def putConstant (self, event, symbol, val):
		ls = self.act_exprsn.split ()
		if self.state == 0 or self.state == 2:
			self.act_exprsn = val + " "
			self.exprsn = symbol
			self.state = 1
		elif len (ls) > 0 and (ls[-1] in ')!' or self.chcknum (ls[-1]) in [0,1]):
			self.act_exprsn += " * " + val
			self.exprsn += symbol
		else:
			self.act_exprsn += val
			self.exprsn += symbol
		self.calcans.config (text = self.exprsn)

	def putOpenPar (self, event):
		ls = self.act_exprsn.split ()
		if self.state == 0 or self.state == 2:
			self.act_exprsn = "( "
			self.exprsn = "("
			self.state = 1
		elif len (ls) > 0 and self.chcknum (ls[-1]):
			self.act_exprsn += " * ( "
			self.exprsn += "("
		else:
			self.act_exprsn += " ( "
			self.exprsn += "("
		self.calcans.config (text = self.exprsn)

	def putClosePar (self, event):
		if self.state == 0 or self.state == 2:
			self.act_exprsn = ") "
			self.exprsn = " )"
			self.state = 1
		else:
			self.act_exprsn += " ) "
			self.exprsn += ")"
		self.calcans.config (text = self.exprsn)

	def putDecimal (self, event):
		ls = self.act_exprsn.split ()
		if self.state == 0 or self.state == 2:
			self.act_exprsn = "0."
			self.exprsn = "."
			self.state = 1
		elif len (ls) > 0 and ls[-1] in '(+-*/':
			self.act_exprsn += " 0."
			self.exprsn += "."
		elif '.' not in ls[-1]:
			self.act_exprsn += "."
			self.exprsn += "."
		self.calcans.config (text = self.exprsn)

	def putBinaryOper (self, event, operator, symbol):
		ls = self.act_exprsn.split ()
		if self.state == 0:
			self.act_exprsn = "0 " + operator + " "
			self.exprsn = symbol
			self.state = 1
		elif self.state == 2:
			self.act_exprsn = self.exprsn + " " + operator + " "
			self.exprsn += symbol
			self.state = 1
		elif len (ls) > 0 and (ls[-1] == ')' or self.chcknum (ls[-1]) in [0,1]):
			self.act_exprsn += " " + operator + " "
			self.exprsn += symbol
		elif len (ls) > 0 and ls[-1] in '+-*/^!':
			ls[-1] = operator
			self.act_exprsn = ' '.join (ls)
			self.exprsn = ''.join (ls[:-1]) + symbol
		elif len (ls) > 0 and ls[-1] == '(':
			if operator in "+-":
				self.act_exprsn += " 0 " + operator + " "
			else:
				self.act_exprsn += operator + " "
			self.exprsn += symbol
		self.calcans.config (text = self.exprsn)

	def putUnaryOper (self, event, operator):
		ls = self.act_exprsn.split ()
		if self.state == 0 or self.state == 2:
			self.act_exprsn = operator + " ( "
			self.exprsn = operator + "("
			self.state = 1
		elif ls[-1] in '(+-*/^': #or len (ls) == 0
			self.act_exprsn += " " + operator + " ( "
			self.exprsn += operator + "("
		elif self.chcknum (ls[-1]) or ls[-1] in ')!':
			self.act_exprsn += " * " + operator + " ( "
			self.exprsn += operator + "("
		self.calcans.config (text = self.exprsn)

	def calcSqrt (self, event):
		ls = self.act_exprsn.split ()
		if self.state == 0 or self.state == 2:
			self.act_exprsn = "√ "
			self.exprsn = "√"
			self.state = 1
		elif ls[-1] in '(+-*/^': #or len (ls) == 0
			self.act_exprsn += " √ "
			self.exprsn += "√"
		elif self.chcknum (ls[-1]) or ls[-1] in ')!':
			self.act_exprsn += " * √ "
			self.exprsn += "√"
		self.calcans.config (text = self.exprsn)

	def calcFactorial (self, event):
		ls = self.act_exprsn.split ()
		if self.state == 0 or self.state == 2:
			self.act_exprsn = "0 ! "
			self.exprsn = "0!"
			self.state = 1
		elif len (ls) > 0 and ls[-1] in '+-*/^!':
			ls[-1] = "!"
			self.act_exprsn = ' '.join (ls)
			self.exprsn = ''.join (ls)
		else:#elif (len (ls) > 0 and ls[-1].isdigit ()):
			self.act_exprsn += " ! "
			self.exprsn += "!"
		self.calcans.config (text = self.exprsn)

	def delete (self, event):
		ls = self.act_exprsn.split ()
		if self.state == 0 or self.state == 2:
			pass
		elif len (ls) > 0:
			t = ls.pop ()
			if t == "/":
				t = ""
				self.exprsn = self.exprsn[:-1]
			elif t not in map (repr, [math.pi, math.e]):
				t = t[:-1]
				ls.append (t)
			self.act_exprsn = ' '.join (ls)
			self.exprsn = self.exprsn[:-1]
			if len (self.exprsn) == 0:
				self.exprsn = "0"
				self.state = 0
		self.calcans.config (text = self.exprsn)

	def clearAll (self, event):
		self.act_exprsn = ""
		self.exprsn = "0"
		self.state = 0
		self.calcans.config (text = self.exprsn)
		self.calcexpr.config (text = "")

	def evaluate (self, event):
		try:
			res = self.infixEval ()
			self.calcexpr.config (text = self.exprsn + '=')
			self.calcans.config (text = repr (res))
			self.act_exprsn = repr (res) + " "
			self.exprsn = repr (res)
			self.state = 2
		except (IndexError, ValueError) as e:
			self.calcexpr.config (text = "")
			self.calcans.config (text = "Error")
			self.act_exprsn = ""
			self.exprsn = ""
		except (ZeroDivisionError, OverflowError) as e:
			self.calcexpr.config (text = self.exprsn)
			self.calcans.config (text = "∞")
			self.act_exprsn = "∞ "
			self.exprsn = "∞"
			self.state = 2

	#通过将中缀表达式转换为后缀来评估中缀表达式，然后使用堆栈解决它
	def infixEval (self):
		s = Stack ()
		outlst = []
		tokenlst = self.act_exprsn.split ()

		prec = {}
		prec ['sin'] = 5
		prec ['cos'] = 5
		prec ['tan'] = 5
		prec ['log'] = 5
		prec ['ln'] = 5
		prec ['√'] = 5
		prec ['!'] = 5
		prec ['^'] = 4
		prec ['/'] = 3
		prec ['*'] = 3
		prec ['+'] = 2
		prec ['-'] = 2
		prec ['('] = 1

		oplstbin = ['/', '*', '+', '-', '^']
		oplstun = ['sin', 'cos', 'tan', 'log', 'ln', '√', '!']

		s.push ('(')
		tokenlst.append (')')

		for token in tokenlst:
			if token == '(':
				s.push (token)
			elif token == ')':
				if not s.isEmpty ():
					topToken = s.pop ()
				while topToken != '(':
					outlst.append (topToken)
					topToken = s.pop ()

			elif token in oplstbin:
				if prec [s.peek ()] == prec [token]:
					if outlst [-1] not in oplstbin or outlst [-1] not in oplstun:
						num2 = float (outlst.pop ())
					if outlst [-1] in oplstbin or outlst [-1] in oplstun:
						outlst = outlst + [repr (num2)]
					else:
						num1 = float (outlst.pop ())
						t = s.pop ()
						res = 0
						if t == '+':
							res = num1+num2
						elif t == '-':
							res = num1-num2
						elif t == '*':
							res = num1*num2
						elif t == '/':
							res = num1/num2
						elif t == '^':
							res = math.pow (num1, num2)
						outlst = outlst + [repr (res)]
				while prec [s.peek ()] > prec [token]:
					outlst.append (s.pop ())
				s.push (token)

			elif token in oplstun:
				s.push (token)

			else:
				outlst.append (token)

		while not s.isEmpty ():
			if s.peek () == '(':
				s.pop ()
			else:
				outlst.append (s.pop ())

		for token in outlst:

			if token in oplstbin:
				num2 = float (s.pop ())
				num1 = float (s.pop ())
				res = 0
				if token == '+':
					res = num1+num2
				elif token == '-':
					res = num1-num2
				elif token == '*':
					res = num1*num2
				elif token == '/':
					res = num1/num2
				elif token == '^':
					res = num1**num2
				s.push (repr (res))

			elif token in oplstun:
				num = float (s.pop ())
				res = 0
				if token == 'sin':
					res = math.sin (num)
				elif token == 'cos':
					res = math.cos (num)
				elif token == 'tan':
					res = math.tan (num)
				elif token == 'log':
					res = math.log10 (num)
				elif token == 'ln':
					res = math.log (num)
				elif token == '√':
					res = math.sqrt (num)
				elif token == '!':
					if math.floor (num) == math.ceil (num):
						res = float (math.factorial (int (num)))
					else:
						res = float (math.factorial (num))
				s.push (repr (res))

			else:
				s.push (token)

		result = round (float (s.pop ()), 15)
		if math.floor (result) == math.ceil (result) and not abs(result)//10**16:
			return int (result)
		else:
			return result

		
def main ():
	mycalc = Calculator ()

if __name__ == "__main__":
	main ()
