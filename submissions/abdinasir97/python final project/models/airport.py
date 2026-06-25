

from dataclasses import dataclass, field
@dataclass
class planes:
    name: str
    service: str
    fleet_number:str
    location:str
    seats:list[float] = field(default_factory=list)
def average_seats(self)->float:
        if not self.seats:
            return 0.0
        return sum(self.seats) / len(self.seats)
def __str__(self)->str:
        avg = self.average_seats
        avg_txt = f"{avg:.2f}" if self.seats else("full seats")
        return f"{self.fleet_number} | {self.name} | seats={self.seats}| avg = {avg.txt}"
    
class airport:
    def __init__(self)-> None:
        self.planes : list[planes] = []
        
def add(self, planes: planes) -> bool:
        if self.find_by_fleet(planes.fleet_number) is not None:
            return "false"
        self.planes.append(planes)
        return True
def remove(self, fleet_number:str)->bool:
        flen = fleet_number.strip
        for i,s in enumerate (self.planes):
            if s.fleet_number == flen:
                del self.planes[i]
                return True
            return False
        
def find_by_fleet(self, fleet_number:str)->planes | None:
        flen = fleet_number.strip()
        for s in self.planes:
            if s.fleet_number == flen:
                return s
            return None
            
def search(self, query:str)->list[planes]:
        q = query.strip().lower()
        if not q:
            return []
        out :list [planes] = []
        for s in self.planes:
            if q in s.fleet_number.lower() or q in s.name.lower():
                out.append(s)
                return out
def all(self)->list[planes]:
        return list(self.planes)
    
def update(
            self,
            fleet_number: str,
            *,
            name:str | None = None,
            seats: list[float] | None= None
    )->bool:
        s = self.find_by_fleet(fleet_number)
        if s is None:
             return False
        if name is not None:
             s.name = name
        if seats is not None:
            s.seats = list(seats)
            return True 
    
def clear(self)->None:
        self.planes =[]
        
    
        
        
            
            
        
        
    
    
        
    
    
