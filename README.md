#Information security
##Scapy
Kenny Embrechts & Jente Adams

3EA1

##Voorwoord

We hebben voor dit project gekozen omdat het een uitdaging ging vormen. We hadden de programeer taal Python nog nooit gebruikt en we moesten Python ook nog kunnen gebruiken in een website om gemakkelijk de interface die op de Raspberry Pi zit, te tonen op een andere computer.


# Inhoudsopgave

[1. Inleiding](#Inleiding)</br>
[2. Specificaties](#Specificaties)</br>
>[2.1. Python](#Python)</br>
>>[2.1.1. Scapy](#Scapy)</br>
>>>[2.1.1.1. ping.py](#ping)</br>
>>>[2.1.1.2. tcp.py](#TCP)</br>
>>>[2.1.1.3. arp.py](#ARP)</br>

>>[2.1.2. Flask](#Flask)</br>

>[2.2. Raspbian](#raspbian)</br>

[3. CodeGenie deployen](#deploy)

[4. Conclusie](#Conclusie)

#1. Inleiding

Het is een project dat op school kan gebruikt worden voor de 1ste jaars elektronica-ICT om zo hun packet sniffing skills te verbeteren. Er dient naar een website gesurft te worden gehost op de Raspberry Pi en dan de juiste instellingen kiezen, wat met al een klein beetje netwerk kennis geen enkel probleem zou mogen zijn en dan sniffen maar.

#2. Specificaties

We moesten werken met een Raspberry pi waar we Raspbian op geïnstaleerd hebben. Rasbian hebben we geïnstalleerd omdat deze Linux distributie gebasseerd is op Debian en omdat Debian gemakkelijk is om mee te leren werken en werken. We hadden Python nodig met de Scapy library geïnstaleerd. Om de Scapy library te instaleren hadden we nog een aantal andere programma's nodig waaronder: tcpdump, graphviz, imagemagick, python-gnuplot, python-crypto en python-pyx. Dez programma's worden gebruikt door Scapy om een aantal functies uit te voeren. Wij hebben namelijk enkel met tcpdump gewerkt om paketten te versturen, bewerken en te ontvangen. Daarnaast hadden we nog iets nodig om onze website mee op te bouwen. We hebben gekozen voor Flask, omdat Flask een Python framework is konden we gemakkelijk onze scripts geschreven in Python laten uitvoeren door Flask met het voordeel dat we geen data moesten gaan omvormen en rare dingen moesten doen in onze code om alles te laten werken. We gaan de component hieronder uitleggen, en dan toelichten hoe wij deze hebben gebruikt in ons project.

##<a id="Python"></a>2.1. Python

Python is een programeer taal en een scripting taal. Wat Python anders maakt dan ander programeertalen en scriptingtalen is dat het zorgt voor een goede leesbaarheid van de code en dat het sneller is om te schrijven, een nadeel is echter de tijd om te compileren, maar doordat je snellere code schrijft wordt dit nadeel opgeheven en kan je sneller je project klaar hebben dan in andere talen.

###<a id="Scapy"></a>2.1.1. Scapy

Scapy is een pakket manipulatie tool geschreven in Python waarmee je paketten kan versturen, wijzigen, ontvangen. Maar ook aanvallen mee kunt opzetten, traceroutes mee kan doen en nog veel meer. Wij gebruiken Scapy enkel om paketten mee te verzenden. Een hele goede guide voor Scapy is [The Very Unofficial Dummies Guide To Scapy](http://scapy-guide.googlecode.com/files/ScapyGuide.pdf). Hieronder leg ik de code van de scripts uit.

####<a id="ping"></a>2.1.1.1. ping.py
![ping.py](screenshots/pingScript.png)

Met `packet = IP(dst=ip, ttl=20)/ICMP()`<br/> gaan we het pakket opbouwen. Het is een IP paket met een destination address gelijk aan de waarde in de ip variabele een time to live van 20 hops en we hangen aan het ip pakket ook een ICMP pakket voor de ping te versturen.<br/>
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


##<a id="Rasbian"></a>2.2 Raspbian
