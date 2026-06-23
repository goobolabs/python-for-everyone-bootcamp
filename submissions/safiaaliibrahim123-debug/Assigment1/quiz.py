#welcoming the user
name = input("What is your name ?");
print('Welcome,', name)

# List of all programming language 

languages = [
  "Python",
  "Javascript",
  "Typescript",
  "Java",
  "C",
  "C++",
  "C#",
  "Go",
  "Rust",
  "Kotlin",
  "Swift",
  "Dart",
  "HTML",
  "CSS",
  "Sass",
  "Less",
  "Haskell",
  "Elixir",
  "Erlang",
  "F#",
  "OCaml",
  "Clojure",
  "Scheme",
  "Assembly",
  "Zig",
  "Nim",
  "Ada",
  "Bash",
  "PowerShell",
  "Perl",
  "Ruby",
  "Lua",
  "Objective-C",
  "Flutter (Dart)",
  "R",
  "MATLAB",
  "Julia",
  "SQL",
  "PL/SQL",
  "T-SQL",
  "GDScript",
  "Haxe",
  "Crystal",
  "V",
  "ReasonML",
  "ReScript",
  "Pony",
  "Hack",
  "Solidity",
  "Move"
];

#score count
score = 0

# fist question
lang = input("Q1: what is your favorite programming language ?");

if(lang.capitalize() in languages):
    score +=1
    print("your favorite language is:",lang, "it's amazing!")
else:
    print(f"i think {lang} isn't a programming language or it's new language")
# second question
q2 = int(input(f"Q2:How lang have you been known {lang} lang?"))
if(q2 < 3):
    score+=1;
    print("You're still beginner for",lang, "Good luck!")
elif(q2 > 3 and q2 < 5):
    score+=1
    print(f"You're Intermediate for:",lang, "Keep going!")
else:
    score+=1
    print("You're Expert for:",lang, "lang", "score:",score);

#third question
q3= input(f"What is the biggest challenge you faced while you were learning {lang} language?")
print("in programming without challenge isn't possible!")
score +=1

# show the result
if(score == 3 or score >= 2):
    print(f"congrats {name}!")
    print(f"you have got 3 out {score}")
else:
    print(f"sorry {name} you failed!")
    print(f"you have got 3 out {score}")
