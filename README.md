#Information security
##Scapy
Kenny Embrechts & Jente Adams

3EA1

##Voorwoord

We hebben voor dit project gekozen omdat het een uitdaging ging vormen. We hadden zelf nog nooit geprogrammeerd in Python dus hier gingen we zelf al heel veel van leren. We moesten Python dan gebruiken om via een website, waar je een interface had, scripts aan te roepen die je kan runnen die zich op een Raspberry Pi bevinden.


# Inhoudsopgave

[1. Inleiding](#Inleiding)</br>
[2. Specificaties](#Specificaties)</br>
>[2.1. Python](#Python)</br>
>>[2.1.1. Scapy](#Scapy)</br>
>>>[2.1.1.1. ping.py](#ping)</br>
>>>[2.1.1.2. tcp.py](#TCP)</br>
>>>[2.1.1.3. arp.py](#ARP)</br>

>>[2.1.2. Flask](#Flask)</br>
>>>[2.1.2.1. Scapy.py](#ScapyPy)<br/>
>>>[2.1.2.2. Jinja2](#Jinja2)<br/>
>>>[2.1.2.2. Werkzeug](#Werkzeug)<br/>

>[2.2. Raspbian](#raspbian)</br>
>>[2.2.1. SetCapabilities](#SetCap)<br/>
>>[2.2.2. Start applicatie bij opstarten](#pythonOnBoot)

<<<<<<< HEAD
[3. Gebruiksinstructies](#deploy)
=======
[3. Het project deployen](#deploy)
>>>>>>> 7cd8aeb624c9af6ed4d9cca9f6eb661661a1aa1b

[4. Conclusie](#Conclusie)

#<a id="Inleiding"></a>1. Inleiding

Het is een project dat op school kan gebruikt worden voor de 1ste jaars elektronica-ICT om zo hun packet sniffing skills te verbeteren. Er dient naar een website gesurft te worden, gehost op de Raspberry Pi en dan de juiste instellingen kiezen, wat met al een klein beetje netwerk kennis geen enkel probleem zou mogen zijn en dan sniffen maar.

Op deze manier kan je heel gemakkelijk fictief data verkeer maken. Dit data verkeer kan je opvullen met elk pakketje dat je maar wilt. Zo is het ook heel makkelijk te controleren of je het goede pakket te pakken hebt!

#<a id="Specificaties"></a>2. Specificaties

We moesten werken met een Raspberry pi waar we Raspbian op geïnstalleerd hebben. Rasbian hebben we geïnstalleerd omdat deze Linux distributie gebasseerd is op Debian en omdat Debian gemakkelijk is om mee te leren werken en om mee te werken. We hebben Python gebruikt om de scripts mee te schrijven. Naast Python, hadden we dan ook de Scapy library nodig. Om de Scapy library te installeren hadden we nog een aantal andere programma's nodig waaronder: tcpdump, graphviz, imagemagick, python-gnuplot, python-crypto en python-pyx. Dez programma's worden gebruikt door Scapy om een aantal functies uit te voeren. Wij hebben namelijk enkel met tcpdump gewerkt om paketten te versturen, bewerken en te ontvangen. Daarnaast hadden we nog iets nodig om onze website mee op te bouwen. We hebben gekozen voor Flask, omdat Flask een Python framework is, konden we gemakkelijk onze scripts geschreven in Python laten uitvoeren door Flask, met het voordeel dat we geen data moesten gaan omvormen en rare dingen moesten doen in onze code om alles te laten werken. We gaan de componenten hieronder uitleggen, en dan toelichten hoe wij deze hebben gebruikt in ons project.

##<a id="Python"></a>2.1. Python

Python is een programmeertaal en een scripting taal. Wat Python anders maakt dan andere programeertalen en scriptingtalen is dat het zorgt voor een goede leesbaarheid van de code en dat het sneller is om te schrijven, een nadeel is echter de tijd om te compileren, maar doordat je snellere code schrijft wordt dit nadeel opgeheven en kan je sneller je project klaar hebben dan in andere talen.

Voor Python bestaan er ook vele libraries die je gratis kan downloaden voor data analyse. Aangezien deze tool op deze moment redelijk basis is, is dit dus handig om de tool in te toekomst mee uit te breiden. Omdat Python een 'leesbare' taal is, is het dus ook makkelijk te leren. Vele mensen die de principes van programmeren kennen, zullen dus heel snel weg zijn met Python (We hadden zelf nog nooit Python gebruikt, maar na een paar uurtjes waren we er helemaal mee weg).

###<a id="Scapy"></a>2.1.1. Scapy

Scapy is een pakket-manipulatie-tool geschreven in Python waarmee je paketten kan versturen, wijzigen, ontvangen. Je kan er ook aanvallen mee opzetten, traceroutes mee doen en nog veel meer. Wij gebruiken Scapy enkel om paketten mee te verzenden. Scapy wordt ook veel gebruik om veiligheid van netwerken mee te testen, of van een computer.

Een nadeel daarentegen is dat het Scapy niet snel is in het uitwisselen van data. Dit komt deels door het feit dat het in Python is geschreven. Wij hebben hier nu relatief weinig last van gehad omdat we met heel lichte en simpele scriptjes hebben gewerkt.

Een hele goede guide voor Scapy is [The Very Unofficial Dummies Guide To Scapy](http://scapy-guide.googlecode.com/files/ScapyGuide.pdf). Hieronder leg ik de code van de scripts uit.

####<a id="ping"></a>2.1.1.1. ping.py
![ping.py](screenshots/pingScript.png)

Met `packet = IP(dst=ip, ttl=20)/ICMP()`<br/> gaan we het pakket opbouwen. Het is een IP pakket met een destination address gelijk aan de waarde in de ip variabele, een time to live van 20 hops en we hangen aan het ip pakket ook een ICMP pakket voor de ping te versturen.<br/>
Met `ans, unans = srloop(packet, timeout=TIMEOUT, count=nr, inter=delay)`
gaan we het pakket in een layer 3 loop steken. We geven ook een count mee, deze waarde wordt gebruikt om te definiëren hoeveel pakketen er verstuurd moeten worden, als er niets is ingevuld dan wordt het pakket een oneindig aantal keer verzonden. met `inter=delay` geven we mee hoeveel tijd er tussen de pakketen moet zitten. De loop kan twee antwoorden krijgen ofwel is het pakket beantwoord ofwel is de timeout verstereken.

####<a id="TCP"></a>2.1.1.2. tcp.py
![tcp.py](screenshots/tcpScript.png)

Het tcp.py script is bijna hetzelfde als het ping. py script, met als enig verschil dat we aan ons IP pakket geen ICMP pakket zetten maar een TCP pakket met een destination poort dat hij moet bereiken via `dport=port`.

####<a id="ARP"></a>2.1.1.3. arp.py
![arp.py](screenshots/arpScript.png)

Het grote verschil tussen het arp.py script en de andere scripts is dat inplaats van een layer 3 pakket er nu een layer 2 pakket wordt verzonden. met `packet = ETher(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip)` maken we een Ether() header met als destinaton het broadcst adres. Via `ARP(pdst=ip)` gaan we aan de Ether header een ARP pakket hangen die op zoek gaat naar het ip address mee gegeven in `pdst=ip`.<br/>
met `ans, unans = srploop(packet, timeout=TIMEOUT, iface="eth0", count=nr, inter=delay)` gaan we ons pakket in een layer 2 loop steken. Hier is alles het zelfde buiten `srploop() in plaats van srloop()` en we geven een `iface="eth0"` parameter mee om Scapy te laten weten via welke verbinding hij dit pakket moet verzenden.

###<a id="Flask"></a>2.1.2. Flask

Flask is een micro web applicatie framework dat in Python is geschreven. Het wordt zo genoemd omdat je er geen specifieke tool op library voor nodig hebt om het te laten werken. Als gebruiker van Flask ben je dus volledig vrijstaand welke tools en libraries je gaat gebruiken om je web applicatie mee te maken

Het biedt daarentegen wel veel extensies die je kan gebruiken, om je web applicatie extra features te geven. Indien je onze applicatie nog verder wil uitbreiden, zal Flask je daar genoeg opties voor geven.

Flask is ook volledig open source. Om de werking beter te begrijpen biedt het Flask Core team je de kans om de source code eens te bekijken. Je kan, indien je dit wil, dus ook meebouwen aan Flask. Er wordt altijd al gestimuleerd om, indien je bugs vindt, deze zo snel mogelijk te rapporteren.

####<a id="ScapyPy"></a>2.1.2.1. Scapy.py
####<a id="Jinja2"></a>2.1.2.2. Jinja2
####<a id="Werkzeug"></a>2.1.2.3. Werkzeug

##<a id="Rasbian"></a>2.2. Raspbian

Raspbian is een free software gebaseerd op Debian, geoptimaliseerd om te werken op de architecturen voor de Raspberry Pi. Raspbian voorziet ook 35000 ‘packages’ om te installeren, waardoor je applicaties makkelijker kan maken en ondersteunen. Hoewel Raspbian gereleased is in 2012, worden er nog altijd ‘packages’ gemaakt of ‘vertaald’ van Debian, om de ondersteuning nog groter te maken. Omdat Raspbian gebaseerd is op Debian en Debian niet zo moeilijk is om mee te werken en zeer stabiel is, is dit een zeer goed besturingssysteem voor onze web applicatie.

###<a id="SetCap"></a>2.2.1. SetCapabilities

###<a id="pythonOnBoot"></a>2.2.2. Start applicatie bij opstarten

#<a id="deploy"></a>3 Gebruiksinstructies
#<a id="Conclusie"></a>4 Conclusie
