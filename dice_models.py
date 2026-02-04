from dataclasses import dataclass

@dataclass
class Die:
    die_type: str      
    face: str        
    exploded: bool = False 

    def is_explosive(self) -> bool:
        return "🎯" in self.face
