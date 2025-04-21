import json
import requests
andmed = {"nimi": "Anna", "vanus": 25, "abielus": False}
json_string = json.dumps(andmed, indent=2, sort_keys=True)
print(json_string)

#lisame failisse
with open ("andmed.json","w") as f:
    json.dump(andmed, f)

#loeme failist
with open ("andmed.json","r") as f:
    andmed_failist=json.load(f)
print(andmed_failist)


klass = {
"opetaja": "Tamm",
"opilased": [
{"nimi": "Mari", "hinne": 5},
{"nimi": "Juri", "hinne": 4}
] }
with open("klass.json", "w") as f:
    json.dump(klass, f, indent=2)

linn=input("Sisesta linna nimi: ")
api_voti="59955a7ce4935d3f3a5e8d286c211cdc"
url=f"http://api.openweathermap.org/data/2.5/weather?q={linn}&appid={api_voti}&units=metric&land=et"
vastus = requests.get(url)
andmed = vastus.json()
if andmed.get("cod") != "404" and "main" in andmed and "weather" in andmed:
    peamine = andmed["main"]
    temperatuur = peamine["temp"]
    niiskus = peamine["humidity"]
    kirjeldus = andmed["weather"][0]["description"]
    tuul = andmed["wind"]["speed"]
    print(f"Ilm linnas {linn}:")
    print(f"Temperatuur: {temperatuur}C")
    print(f"Kirjeldus: {kirjeldus.capitalize()}")
    print(f"Niiskus: {niiskus}%")
    print(f"Tuule kiirus: {tuul} m/s")
else:
    print("Linna ei leitud. Palun kontrolli nime õigekirja.")   
with open("ilm.json", "w", encoding="utf-8") as f:
    json.dump(andmed, f, ensure_ascii=False, indent=4)

with open('andmed.json', 'r') as f:
    andmed = json.load(f)

sisestatud_nimi = input("Sisesta nimi: ")

if andmed.get("nimi", "voti ei ole!") == sisestatud_nimi:
    print(f"\nAutod kasutajal {sisestatud_nimi}: ")
    for auto in andmed.get("autod", []):
        print(F"- {auto['mark']},{auto['muudel']}.{auto['varv']}, number: {auto['number']}")
else:
    print("Selle nimega kasutajat ei leinud.")