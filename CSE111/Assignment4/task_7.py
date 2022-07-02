class Match:
    def __init__(self, name):
        self.name = name
        self.new_name = self.name.split("-")
        self.match_run = 0
        self.match_over = 0
        self.wicket = 0
        print("5..4..3..2..1.. Play!!!")

    def add_run(self, run):
        self.match_run += run
        self.sum_run = self.match_run

    def add_over(self, over):
        self.match_over += over
        self.sum_over = self.match_over

    def add_wicket(self, wicket):
        self.wicket = wicket

    def print_scoreboard(self):
        print(f"Batting Team: {self.new_name[0]}")
        print(f"Bowling Team: {self.new_name[1]}")
        return f"Total Runs: {self.sum_run} Wickets: {self.wicket} Over: {self.sum_over}"


match1 = Match("Rangpur Riders-Cumilla Victorians")
print("=========================")
match1.add_run(4)
match1.add_run(6)
match1.add_over(1)
print(match1.print_scoreboard())
print("=========================")
match1.add_over(5)
print("=========================")
match1.add_wicket(1)
print(match1.print_scoreboard())



15

class FinalT6A:
    def __init__(self, x, p):
        self.temp, self.sum, self.y = 4, 0, 1
        self.temp += 1
        self.y = self.temp - p
        self.sum = self.temp + x
        print(x, self.y, self.sum)
    def methodA(self):
        x = 0
        y = 0
        y = y + self.y
        x = self.y + 2 + self.temp
        self.sum = x + y + self.methodB(self.temp, y)
        print(x, y, self.sum)
    def methodB(self, temp, n):
        x = 0
        temp += 1
        self.y = self.y + temp
        x = x + 3 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)
        return self.sum

q1 = FinalT6A(2,1)
q1.methodA()
q1.methodA()


17
class Test5:
  def __init__(self):
      self.sum = 0
      self.y = 0
  def methodA(self):
      x=y=k=0
      msg = [5]
      while (k < 2):
          y += msg[0]
          x = y + self.methodB(msg, k)
          self.sum = x + y + msg[0]
          print(x ," " , y, " " , self.sum)
          k+=1
  def methodB(self, mg2, mg1):
        x = 0
        self.y += mg2[0]
        x = x + 3 + mg1
        self.sum += x + self.y
        mg2[0] = self.y + mg1
        mg1 += x + 2
        print(x , " " ,self.y, " " , self.sum)
        return mg1

t1 = Test5()
t1.methodA()
t1.methodA()
t1.methodA()


18
class Test4:
    def __init__(self):
        self.sum, self.y = 0, 0
    def methodA(self):
        x, y = 0, 0
        msg = [0]
        msg[0] = 5
        y = y + self.methodB(msg[0])
        x = y + self.methodB(msg, msg[0])
        self.sum = x + y + msg[0]
        print(x, y, self.sum)
    def methodB(self, *args):
        if len(args) == 1:
            mg1 = args[0]
            x, y = 0, 0
            y = y + mg1
            x = x + 33 + mg1
            self.sum = self.sum + x + y
            self.y = mg1 + x + 2
            print(x, y, self.sum)
            return y
        else:
            mg2, mg1 = args
            x = 0
            self.y = self.y + mg2[0]
            x = x + 33 + mg1
            self.sum = self.sum + x + self.y
            mg2[0] = self.y + mg1
            mg1 = mg1 + x + 2
            print(x, self.y, self.sum)
            return self.sum


t3 = Test4()
t3.methodA()
t3.methodA()
t3.methodA()
t3.methodA()




