class Netflix:
    No_of_Shows = 0
    def __init__(self,Movies,Series,Documentation):
        self.Movies = Movies
        self.Series = Series
        self.Documentation = Documentation
        
        
        Netflix.No_of_Shows += 1
         
    def Movies(self):
         
        print( "This Movie was released on " + year )

tv_2019 = Netflix("6 Underground" ,"Witcher" , "qwerty" )
print(tv_2019.Series)
#print(tv_2019.Movies())
#print(Netflix.year)
print(tv_2019.__dict__)
print(Netflix.__dict__)
print(Netflix.No_of_Shows)
