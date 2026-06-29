# 🎓 Project Developer: Rahmo Abdullaahi Ali

## 🩸 Blood Bank Management System using(Python OOP)

---

## 📝 Sharraxaadda Mashruuca (Project Overview)

Kani waa barnaamij casri ah oo loogu talagalay maamulka iyo kaydinta xogta dadka dhiigga ku deeqaya (**Blood Donors**). Mashruucan waxaa lagu dhisay luuqadda **Python** iyadoo la raacayo mabaadi'da adag ee **Object-Oriented Programming (OOP)** iyo qaab-dhismeed modular ah oo kala saaraya qaybaha barnaamijka (Clean Architecture).

Xogta deeq-bixiyayaasha waxaa loo kaydiyaa si nidaamsan, waxaana barnaamijka lagu dhex daray nidaam difaacaya sugnaanta xogta (**Data Integrity**) gaar ahaan dhanka Aqoonsiga Gaarka ah (**Donor ID / Primary Key**).

---

## 🚀 Sifooyinka Waaweyn (Core Features)

* **1) Add New Donor:** Lagu darayo deeq-bixiye cusub (ID, Name, Blood Group, Age). Barnaamijku wuxuu si automatic ah u hubiyaa inaan ID-gu horay u jirin si looga tanaasulo xog isku dhex qasanta.
* **2) List All Donors:** Wuxuu soo bandhigaa dhammaan dadka diiwaangashan nidaamka.
* **3) Remove Donor:** In nidaamka laga saaro deeq-bixiye kasta iyadoo loo marayo ID-giisa gaarka ah.
* **4) Multi-Criteria Search:** Nidaam raadin aad u jilicsan oo hal meel ka wada baari kara **ID, Name, Blood Group, iyo Age**.
* **5) Secure User Update:** Waxaa si ammaan ah wax looga beddeli karaa Magaca, Dhiigga, iyo Da'da qofka. ID-ga rasmiga ah (Primary Key) waa mid dhowrsan oo aan la beddeli karin si loo ilaaliyo xeerarka rasmiga ah ee badbaadada software-ka.
* **6) Auto-Save & Persistent Storage:** Xogta waxay si automatic ah ugu kaydsantaa fayl text ah (`data/donors.txt`) marka barnaamijka la xiro ama gacanta lagu save-gareeyo.

---

## 📁 Qaab-dhismeedka Faylasha (Project Structure)

Mashruucu wuxuu u habaysan yahay qaab Package ah oo aad u nadiif ah:

```text
Project/
│
├── models/
│   ├── __init__.py      # Wuxuu folder-ka u aqoonsanayaa Python Package
│   └── donors.py        # Waxaa ku dhex jira class-yada Donor iyo BloodBank (OOP Core)
│
├── utils/
│   ├── __init__.py      # Python Package Marker
│   └── storage.py       # Koodhka maamulaya Load iyo Save-ka File Database-ka
│
├── data/
│   └── donors.txt       # Faylka rasmiga ah ee xogtu ku kaydsan tahay
│
├── main.py              # Faylka ugu weyn ee barnaamijka iyo Menu-ga laga kiciyo
└── README.md            # Sharraxaadda mashruuca (Kan aad hadda akhrinayso)
```
