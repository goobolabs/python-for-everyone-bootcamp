from pathlib import Path
from models.airport import planes, airport
DATA_PATH = Path(__file__).resolve().parent.parent /"data"/ "airport.txt"
FILE_HEADER = "id|name|seats"

def purse_seat(s:str)->list[float]:
    s = s.strip
    if not s:
        return []
    return[float(p.strip) for p in s.split(".")if p.split()]

def is_colum_hearer_line(line:str)->bool:
    return line.strip().lower().replace(" "," ") == FILE_HEADER.lower().replace(" "," ")

def load_airport(path:Path, airport:airport)->None:
    airport.clear()
    try:
        with open(path,"r",encoding="utf-8")as f:
            for row in f:
                line = row.strip()
                if not line or line.startswith("#"):
                    continue
                if is_colum_hearer_line(line):
                    continue
                parts = line.split("|",2)
                if len(parts) !=3:
                    continue
                flen, name, seats_txt = parts[0].strip(), parts[1].strip(), parts(2)
                try:
                    seats = purse_seat(seats_txt)
                except ValueError:
                    continue
                airport.add(planes(fleet_number = flen, name=name, seats=seats))
                
    except FileNotFoundError:
        pass
            
def save_airport(path:Path, airport:airport)->None:
    path.parent.mkdir(parents=True, exist_ok=True)
    line=(f"colums:pipe-separated rows after the headerline\n f(FILE HEADER)\n")
    for s in airport.all():
        seats_txt = ",".join(str(g) for g in s.seats)
        line.append(f"(s.fleet_number) | (s.name)|(seats.txt)\n")
        with open(path, "w", encoding="utf-8")as f:
            f.writelines