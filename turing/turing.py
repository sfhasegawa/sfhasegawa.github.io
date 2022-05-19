class Machine:
    def __init__(self):
        self.step = 0
        self.status = 0
        self.position = 0


    def print_status( self, tape ):
        print( "Step", self.step )
        print( *tape, sep="" )
        print( " " * self.position , "M(", self.status, ")", sep="" )

        
    def finish( self ):
        if self.status == -1 :
            return True
        else:
            return False

        
    def read( self, tape ):
        self.step += 1
        mydata = tape[ self.position ]
        if self.status == 0 and mydata == 0:
            self.position +=1
            self.status = 1
        elif self.status == 1 and mydata == 0:
            self.position += 1
            self.status = -1
        elif self.status == 1 and mydata == 1:
            tape[ self.position ] = 0
            self.position += 1
            self.status = 2
        elif self.status == 2 and mydata == 0:
            self.position += 1
            self.status = 3
        elif self.status == 2 and mydata == 1:
            self.position += 1
            self.status = 2
        elif self.status == 3 and mydata == 0:
            tape[ self.position ] = 1
            self.position += 1
            self.status = 4
        elif self.status == 3 and mydata == 1:
            self.position += 1
            self.status = 3
        elif self.status == 4 and mydata == 0:
            tape[ self.position ] = 1
            self.position +=1
            self.status = 5
        elif self.status == 5 and mydata == 0:
            self.position -=1
            self.status = 6
        elif self.status == 6 and mydata == 0:
            self.position -= 1
            self.status = 7
        elif self.status == 6 and mydata == 1:
            self.position -= 1
            self.status = 6
        elif self.status == 7 and mydata == 0:
            tape[ self.position ] = 1
            self.position += 1
            self.status = 1
        elif self.status == 7 and mydata == 1:
            self.position -= 1
            self.status = 7
            
            
mytape =[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

machine = Machine()
machine.print_status( mytape )

while machine.finish() == False:
    machine.read( mytape )
    machine.print_status( mytape )
