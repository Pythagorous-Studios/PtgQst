import logger.logger as logger


"""logging"""
def log(msg,lvl=0):
    """wraper for the logger library"""
    if log==True:
        print(logger.inlog(msg=msg,lvl=lvl,src=__name__))
    else:
        logger.inlog(msg=msg,lvl=lvl,src=__name__)

"""error class"""
class InvalidCoords(BaseException):
    pass
class FailedToAddManager(BaseException):
    pass

"""classes"""
class board(): 
    def __init__(self,name): 
        tiles=[] 
        pieces=[]
        self.name=name
        self.tiles=tiles
        self.pieces=pieces
    def addtile(self,til): 
        if isinstance(til,tile): 
            self.pieces.append(til) 
        return isinstance(til,tile) 
        
    def addpiece(self,pce): 
        if isinstance(pce,piece): 
            if pce.addManager(self) == True:
                 self.pieces.append(pce)
                 log("Added piece: "+str(pce)+" to pieces on Board: "+str(self))
            else:
                raise FailedToAddManager
           

        return isinstance(pce,piece) 
        
    def coords_exist(self,x,y): 
        for piece in self.pieces: 
            if (x,y) == (piece.x,piece.y): 
                return True
        return False 
         
    def gattr(self,ix,iy,attr):
        for piece in self.pieces:
            #log((place),(place.x),(place.y))
            if (ix,iy)==(piece.x,piece.y):
                try:
                    if attr=="descrip":
                        log(piece.descrip)
                        return piece.descrip
                except:
                    pass
                 
class tile(): 
    def __init__(self,name,x,y,descrip=None): 
        self.name=name 
        self.y=y 
        self.x=x 
        self.y=y 
        self.descrip=descrip 

        

    
class piece(): 
    def __init__(self,name,x,y): 
        mgeng=None
        self.name=name 
        self.x=x 
        self.y=y 
        self.mgeng=mgeng
    
    def addManager(self,MgEng):
        if isinstance(MgEng,board):
            self.mgeng=MgEng
            return True
        else:
            return False
    def goto(self,x,y): 
        if self.mgeng.coords_exist(x,y): 
            self.x=x 
            self.y=y
        else:
            log('no such coord: '+str((x,y))+' in mg. eng. : '+str(self.mgeng))
    def look(self):
        return self.mgeng.gattr(self.x,self.y,"descrip")
