from dataclasses import dataclass

@dataclass
class Contact:
    id: int
    name: str
    phone: str # not int because we can add +, some times (), -() or starts with 0 so int cannot store these values  
    fav: bool = False