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

class Item():
	def __init__(self,name,descrip=None):
		holder=None#container is more logical but to avoid conflicts its holder
		self.name=name
		self.descrip=descrip
		self.holder=holder
	def setHolder(self,newholder):
		#TODO:flesh out/more security
		if isinstance(newholder, container):
			self.holder=newholder

class Container():
	def __init__(self,name,descrip=None):
		inventory=None
		self.name=name
		self.descrip=descrip
		self.inventory=inventory
	def TransferItem(self,item,newcontainer):
		#Verifies existence of new container, iniate RecieveItem for recipient, and finally removes item from self upon confirmation by recipient
		if isinstance(newcontainer,container):
			if newcontainer.RecieveItem(item,self):
				inventory.remove(item)
			else:
				pass
	def RecieveItem(self,item,src):
		#Reciever of items from TransferItem,must confirm reception of item before finalization.
		#TODO: Add default security/auth for item reception.
		if isinstance(src,container):
			try:
				inventory.append(item)
				item.setHolder(self)
				return True
			except:
				return False
			
	def _InitItem(self,item):
		#Only to be used for initial setup!
		#Similair in functionality as Recieve item,but explicitly and only for the initial population of a container by a board/manager.
		if isinstance(item, Item):
			try:
				inventory.append(item)
				item.setHolder(self)
				return True
			except:
				return False
				#for added security,if strict was enabled raise error for unauthorized item moving: possible cheating
