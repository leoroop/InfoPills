#### Pillola informatica #0

Partiamo dal primo *concetto fondamentale* senza in quale non ci sarebbe possibile proseguire col resto:
- un computer è un attrezzo stupido che fa calcoli
- fa sempre e solo ciò che gli si dice di fare.
- è molto molto rapido ad eseguire i suddetti calcoli

Quindi possiamo fargli fare un'infinità di operazioni tutte in fila (per semplicità diciamo una alla volta, non è sempre così ma per quello che ci serve possiamo assumere che le faccia una per una)
Detto ciò viene da sé che scrivere un software non è altro che "dire al pc una serie di calcoli che vogliamo che faccia". Immagino che la domanda sorga spontanea: *\"ok, ma come faccio ?!?\"* . Senza scendere in dettagli che riguardano l'elettronica, ricordiamo al volo che il computer sa ragionare solo **0** ed **1**, il famoso *__codice binario__*. Ci sono tutta una serie di regole poco utili al momento che ci permettono di passare da un linguaggio comprensibile agli umani a quello comprensibile al computer: questo tipo di operazione si chiama compilazione ,  in pratica c'è un software (che con molta fantasia si chiama compilatore) che prende un file di testo (come quelli che vedi nello screenshot di sopra, in particolare quello a sinistra, quello a destra ha regole un po' diverse, ma ci arriviamo fra un attimo) che si occupa di leggere e tradurre quel testo (detto sorgente) in un file fatto di 0 ed 1 comprensibile e pronto per essere eseguito (eseguibile). Questo è quello che succede, per esempio, con i file scritti in linguaggio C (quello dell'esempio), **C++**, **Java** e con tutti quei linguaggi che appartengono alla grande famiglia dei *__linguaggi compilati__*. Quindi, volendo riassumere, succede una cosa di questo tipo:
*Scrivo file sorgente -> compilatore [più altra roba che non ci serve] -> eseguibile -> PC fa girare il programma*.

Diciamo che questo è il modo *\"classico\"* di far le cose, ma la tecnologia evolve ed è successo (già decenni fa) che qualcuno volesse fare le cose in maniera un pochettino più "snella" in un certo senso, quindi menzioniamo quelli che sono i cosiddetti *__linguaggi interpretati__* , l'esempio principe e che hai già sentito nominare (ed è quello dello screenshot a destra) è il **python**, ma tanto per aggiungere un paio di esempi famosi possiamo citare **javascript** e **php**. In questo caso quello che succede è che c'è un software che si chiama interprete che si va a leggere il tuo file sorgente e fa eseguire direttamente i comandi al pc *man mano che li legge*.

I due approcci di cui sopra sono molto diversi ed ognuno presenta i suoi vantaggi ed i suoi svantaggi, ma magari questi li discutiamo quando siamo un po' più dentro l'argomento. Però distinguiamo 2 situazioni abbastanza tipiche in cui si sceglie uno o l'altro approccio. Tenendo conto che non è una legge universale che vale dappertutto, ogni situazione va gestita poi di volta in volta, possiamo dire che:
- Quando hai bisogno di un software che abbia *prestazioni molto elevate* pur facendo un botto di calcoli è molto probabile che la via giusta sia un linguaggio compilato
- Quando hai bisogno di un software da *mettere in campo alla svelta perdendo poco tempo per scriverlo* un linguaggio interpretato ti permette di fare generalmente prima



#### Pillola informatica #1

Facciamo una breve carrellata di quelli che sono gli **elementi** che compongono un **programma**. Non ci aiuteranno ancora del tutto a capire come scriverne uno, ma possiamo pensarla come una piccola *raccolta* di parole chiave generiche che pongono le basi per andare più spediti mentre procediamo in questo viaggio. Cominciamo quindi col dire cos'è una **variabile**: senza appellarci a concetti strani, una variabile *di fatto* è una *scatola*, un contenitore che possiamo utilizzare per *\"mettere da parte\"* qualcosa ed utilizzarlo in un secondo momento e, come dice anche il nome, **può cambiare nel tempo**.

Facciamo un esempietto di applicazione di questa cosa: vogliamo fare un programma che *calcola l'area di un cerchio* il cui raggio non ci è noto a priori perché vogliamo che venga inserito dall'utente via tastiera. Senza entrare nei dettagli dell'inserimento da tastiera e della visualizzazione del risultato, ci concentriamo un attimo sulla formula, come si fa in matematica. La formula sarà quindi -> *__area = 3.1415 * r * r__*. Viene facile vedere che in questo caso, le variabili che utilizziamo sono 2: area e raggio , che non sono altro che le "scatole" in cui andremo a mettere:

1. Il valore del raggio che ci fornisce l'utente

1. Il risultato del calcolo, che useremo più avanti per fare altre cose fichissime

Capito cosa sono le variabili, riguardiamo per un secondo la formula, perché da questa possiamo ricavare altri 2 mattoncini che compongono, a livello logico, un programma, in particolare guardiamola secondo questo punto di vista:
*__3.1415 * r * r__* , questa è ciò che viene detta **espressione** (e si torna alle medie di cattiveria) , ed è di fatto una roba che una volta che hai il numero da mettere al posto delle lettere puoi calcolare a tutti gli effetti ed ottenere un *risultato*. Fare questo tipo di calcolo si dice in gergo tecnico *__valutare l'espressione__* , che è appunto una formuletta che ci fornisce un risultato.

Il terzo mattoncino che ci serve lo vediamo sempre riprendendo la formuletta di prima, ma stavolta guardandola così:
*__qualcosa = qualcos'altro__*
questo è ciò che viene chiamato uno **statement** , che in italiano traduciamo spesso con **istruzione** , ma a livello logico sarebbe più corretto chiamarla *\"affermazione\"* , in pratica stai dicendo al pc *\"fai questo"\* , che volendo analizzarlo più nel dettaglio possiamo tradurre in:
" metti dentro alla variabile area il risultato che ottieni valutando l'espressione *__3.1415 * r * r__* .

Com'è ovvio che sia, ci sono praticamente *infinite espressioni ed infiniti statement possibili*, ma, in linea di massima, con queste 3 cose (**variabili**, **statement** ed **espressioni**) siamo virtualmente in grado di scrivere a livello di software qualsiasi cosa ci piaccia, darla in pasto ad un computer e farglielo eseguire. Mi rendo conto che adesso è ancora un po' tutto fumoso, ma un pezzetto alla volta spero di fare chiarezza. Con la prossima pillola recap di come funziona tutto l'accrocchio PC ed iniziamo a parlare in modo molto vago di **python**, così poi gli esempi possiamo farli scrivendoli in quel linguaggio, che è a mio modo di vedere di cose il più semplice per cominciare.



#### Pillola informatica #2

Ripartiamo dalla puntata precedente e facciamo un piccolo recap di un paio di concetti che mi sembra utile tenere sotto mano prima di proseguire col resto. Vediamo velocemente *com'è fatto un computer*, poi, in ultima battuta, iniziamo a parlare di **python** come strumento per scrivere programmi.

In soldoni, senza rifarci troppo a nomi altisonanti della teoria dell'informatica, un computer è fatto, *__a livello logico__*, di 3 *"pezzi"* fondamentali di cui dobbiamo tenere conto quando facciamo i programmi:
- L'**unità di calcolo** (conosciuta anche come *processore* o *CPU*), brutalmente un sasso appiattito coi fulmini dentro. E' il *cervello* ed colui che esegue davvero le istruzioni che vogliamo far fare al computer.

- La **memoria centrale** (la *ram*, il posto in cui il computer tiene tutto quello che sta maneggiando mentre esegue un programma)

- La **memoria di massa** (detta spesso anche storage o "hard disk") è dove vengono salvati i file che possiamo leggere e/o utilizzare.

Quando lo accendiamo, il computer fa letteralmente (anche se descritte MOOOLTO a spanne) questa serie di operazioni:

- Va a cercare nella **memoria di massa** la roba che gli serve per funzionare

- Carica quella roba in **memoria centrale**

- Esegue tutto quello che deve eseguire secondo questa logica:
  - *leggi istruzione*
  - *esegui istruzione*
  - *leggi istruzione*
  - *esegui istruzione*
  - etc. etc.

Ora, un linguaggio come il **C** richiede al programmatore di sapere con un certo grado di dettaglio com'è fatta la struttura logica della memoria centrale e qualche altro dettaglio, ma al momento stiamo parlando di *programmazione* e non di *architettura dei calcolatori*, quindi questa parte, almeno per ora, ce la risparmiamo.

In nostro soccorso viene **python**, che si smazza tutta la gestione della memoria da solo nelle retrovie, col risultato che possiamo preoccuparci di meno di combattere col computer e possiamo concentrarci sul problema che il nostro programma deve risolvere.

La parte difficile della programmazione non è tanto scrivere le azioni che il PC deve fare in sé e per sé, lo è molto di più *__organizzare le informazioni__* del nostro problema in modo tale per cui risulti rappresentabile in modo comprensibile tanto per noi quanto per il computer che, ricordiamolo, è una macchina **stupida**, ed essendo stupido ha bisogno di partire da alcuni elementi fondamentali per rappresentare i dati in modo semplice, starà poi a noi organizzarli in modo opportuno per tirare fuori ragionamenti complessi. Vediamo quindi quali sono i tipi di dato fondamentali che python ci permette di utilizzare per fare quello che ci interessa.
- **Numeri interi** , detti int, che sono i numeri col segno: 3, 4, 5, -1, -2 etc.
- **Numeri reali** , detti float (da floating point, virgola mobile), che sono i numeri con la virgola e anche il segno, rappresentabili in 102308094328 modi diversi, ma ora non ci interessa.
- **Stringhe** , brutalmente "pezzi di testo" racchiusi tra virgolette, queste vengono interpretate alla "parla come mangi" cioè col testo che ci scrivi dentro.
- **Booleani** , variabili binarie che possono assumere "True" o "False" e servono per implementare tutta la logica tradizionale a livello di codice
- **Liste** , sequenze di dati, per esempio una lista di int, sono tanti numeri, messi in fila, che possiamo salvare dentro ad una sola variabile e portarceli in giro tutti insieme.
- **Dizionari** , questo è più complicato, magari lo trattiamo a parte, ma ricordiamoci che c'è.

Ci sono poi i costrutti logici, che sono quelli che ci permettono di esprimere dei "pezzi di ragionamento" che il nostro programma può fare per cambiare comportamento a seconda di alcune condizioni che saremo noi a definire. Ne vediamo **3**:

- Costrutto: **if** *condizione* **:** *allora fai X* **else :** *fai Y* , dovrebbe essere abbastanza 1:1 capire cosa fa, se *__"condizione"__* (che, facendo riferimento alla pillola di ieri, sarà un'espressione che una volta valutata dà un valore booleano) è  verificata, quindi il **booleano** di cui sopra ha valore **True**, allora esegue il pezzo di codice X, al contrario se il booleano ha valore False viene eseguito il pezzo di codice Y.
- Costrutto: **for** , non ne vediamo la sintassi perchè si può fare in un sacco di modi, ma sostanzialmente si scorre un **elenco** e *__per ogni elemento dell'elenco__* si fa ciò che c'è scritto dopo il for, serve quindi per ripetere delle parti di codice per un certo numero di volte. Vediamo un esempio nella prossima pillola, è più semplice di quanto si pensa.
- Costrutto **while** , anche questo serve per ripetere parti di codice, ma invece che scorrere un elenco gli si specifica una **condizione** (come nel caso dell'if) ed il codice che segue viene ripetuto *__finchè tale condizione è vera__*. Nel momento in cui la condizione diventa falsa le ripetizioni cessano ed il programma va avanti. Anche per questo costrutto vediamo un esempio la prossima volta.



#### Pillola informatica #3

Vediamo gli ultimi 2 concetti puramente teorici riguardo la **programmazione in generale**, ma che sono concetti cardine per quanto riguarda **python**, senza avere almeno idea di cosa siano ci sarebbe impossibile capire quello che stiamo facendo.
Iniziamo quindi col dire cos'è una **funzione**:
rifacendoci alla buona vecchia definizione *matematica*, una funzione la possiamo descrivere in questo modo:  *__y = f(x)__* ,
se la guardi così sai benissimo che **f** è una formuletta che fa diverse operazioni su **x** e la *"macina"* fino a che non ottieni un valore, che è il tuo *y*.

In informatica funziona esattamente allo stesso identico modo, solo che al posto di operazioni prettamente matematiche la nostra *"f"* può essere composta da un *mix di operazioni* che abbiamo visto durante la pillola scorsa e come risultato ritorna un (o più, ma lo vedremo scrivendo del python) **valore** che puoi mettere dentro ad una **variabile** e riutilizzare in un secondo momento.
Probabilmente in matematica hai visto, magari anche solo di sfuggita, anche cose di questo tipo: **z = f(x, y)** , dove la funzione prende come **argomenti** due valori distinti.
Come ultima cosa ricordiamo che f è soltanto una specie di etichetta con cui identifichiamo quello che fa la nostra funzione. (Sempre tornando alla matematica, sicuramente avrai visto robe come: *__y = cos(x)__* )

Viene abbastanza da sé che le funzioni ci fanno comodo nel momento in cui vogliamo una *"fetta di codice"* da poter riutilizzare ogni volta che ci serve cambiandone solo i **parametri in ingresso** (cioè scrivendo qualcosa al posto della x, per ottenere y).
Facciamo quindi un veloce esempio di come possiamo definire una funzione (l'esempio è in python, in altri linguaggi cambia qualche sfumatura, ma la sostanza è abbastanza universale) che possiamo riutilizzare quante vogliamo:

```python
def calcolo(a, b, mode):
    if mode == '+' :
        return a+b
    else:
       return a-b
```

Questo è un esempio di una piccola **funzione** che, prendendo in ingresso **3 argomenti**, in particolare **2 numeri** ed **1 carattere** testuale, restituisce come risultato la somma o la sottrazione dei 2 numeri dati in ingresso a seconda del valore dell'argomento (detto anche parametro) mode. Una volta che nel nostro programma abbiamo definito questa funzione, la possiamo utilizzare semplicemente chiamandola col suo nome e passandovi gli argomenti su cui ci interessa che essa operi. Ad esempio:

```python
k = calcolo(5 , 13, '+')
h = calcolo(15, 5, '*')
```

Come piccolo esercizio ti chiedo di calcolare quanto valgono k e h, così possiamo verificare se hai capito.

Il *concetto numero 2*, che ci tormenterà per diverso tempo, è quello di **oggetto**, in pratica un oggetto puoi immaginartelo come una specie di *"strumento"*, che ha dei *dati interni* (detti **campi**) ed espone delle *funzioni* (dette **metodi**) che ti permettono di interagire con l'oggetto. Facciamo un esempio semi-pratico e analizziamo il *__Clini5__* secondo questo punto di vista.

Il **Clini5**, semplificando molto, ha:
- Un *__database clienti__* che puoi consultare
- Un *__database risultati__* che puoi consultare
- Può *__eseguire dei test__*

Quindi, immaginando di avere creato in modo opportuno (lo vediamo più avanti come si fa) un oggetto Clini5 noi nel nostro programma python potremo fare qualcosa del genere:

```python
print(Clini5.clienti)
print(Clini5.risultati)
Clini5.do_glicata(sangue_di_tiziocaio)
```

per consultare i *"campi"* **clienti** e **risultati** ed utilizzare il *"metodo"* **do_glicata()**

Soprattutto ques'ultima parte mi rendo conto sia molto molto fumosa, ma la svisceriamo piano piano man mano che programmiamo perché si tratta di un capitolo enorme e coprirlo tutto in una pillola sola sarebbe impossibile. Per ora concentrati sul capire le funzioni e sul fatto che se abbiamo un oggetto (e in **python** letteralmente **TUTTO è un oggetto**) accediamo alle sue proprietà (campi e metodi) utilizzando l'operatore "**.**" (**punto**).



#### Pillola informatica #4

Oggi ci mettiamo nelle condizioni di poter iniziare a scrivere dei programmi con l'ormai famigerato linguaggio **python**. La prima cosa da fare quindi è installarlo sul nostro computer in modo da trovarci un ambiente all'interno del quale poter far girare l'**interprete** e dargli in pasto i sorgenti dei programmi che andremo a scrivere.

Senza ulteriori indugi, apriamo il nostro browser e andiamo all'indirizzo:
https://www.python.org/downloads/

Al quale troveremo una schermata molto simile a questa:

![Download di python 1](img/004/python_dl.jpg)
<!-- <div style="text-align:center"><img src="img/004/python_dl.jpg" /></div> -->

A questo punto clicchiamo su **Download Python 3.7.x** dove *x* è un altro numero. Nell'immagine è riportato il 4 ma non è detto che nel giro di poco venga rilasciata un'altra versione. Non è comunque qualcosa di cui preoccuparci al momento.

Dopo aver cliccato, il sistema dovrebbe proporci qualcosa di simile:
<!-- ![Download di python 2](img/004/python_exe.jpg) -->
<div style="text-align:center"><img src="img/004/python_exe.jpg" /></div>
<div/>
A questo punto clicchiamo su **Salva file** ed attendiamo la fine del download. Una volta concluso andiamo nella cartella Downloads del pc (o quella impostata nel browser per il download dei file) e lanciamo il file **python-3.7.x.exe** che abbiamo scaricato.  [**nota:** è possibile anche lanciarlo direttamente dal broser, basta andare nell'elenco dei download e cliccarci su].

Una volta lanciato ci troveremo davanti qualcosa di questo tipo:

<!-- ![Download di python 2](img/004/start_install.jpg) -->
<div style="text-align:center"><img src="img/004/start_install.jpg" /></div>
<div/>

**ATTENZIONE:** Prima di cliccare su *Install Now* e cominciare l'installazione è conveniente mettere la spunta su  
 *__"Add Python 3.7 to PATH"__* , questa operazione dirà al sistema dove viene installato tutto il materiale relativo a *python*, permettendoci così di utilizzarlo da linea di comando (lo vediamo fra un attimo) senza doverci preoccupare di specificare il percorso tutte le volte (che sarebbe uno sbattimento immane, al punto di far passare la vogliadi programmare). Prima di procedere quindi, verifichiamo di aver messo la spunta:

 <!-- ![Installazione di python](img/004/add_path.jpg) -->
<div style="text-align:center"><img src="img/004/add_path.jpg" /></div>
<div/>

Ora siamo pronti per cliccare finalmente su **Install Now**. Una volta fatto dovremo avere un po' di pazienza ed aspettare che sia tutto finito, l'installer ci informerà del progesso con una sipatica barra verde, come quella qui sotto:

<!-- ![Installazione di python 2](img/004/wait_python.jpg) -->
<div style="text-align:center"><img src="img/004/wait_python.jpg" /></div>
<div/>

Una volta concluso la finestra cambierà avvisandoci che tutto è andato secondo i piani:

<!-- ![Installazione di python 3](img/004/end_python.jpg) -->
<div style="text-align:center"><img src="img/004/end_python.jpg" /></div>
<div/>

A questo punto, per verificare che tutto abbia funzionato correttamente e di aver eseguito i passaggi nel modo giusto possiamo fare 2 cose:

- Apriamo il **Menu Start** di *Windows* e controlliamo se nelle applicazioni aggiunte di recente è comparso qualcosa di relativo a **python** , dovremmo avere qualcosa di simile:

<!-- ![Applicazioni recenti](img/004/recents.jpg) -->
<div style="text-align:center"><img src="img/004/recents.jpg" /></div>
<div/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
se così fosse saremmo già sulla buona strada, ma possiamo effettuare (anche direttamente volendo) un altro &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
controllo.

- Apriamo il famoso **Prompt dei comandi** conosciuto anche come **cmd**, ci troveremo davanti la più temuta (da parte di chi non è ancora navigato) delle finestre, qualcosa di simile:

<!-- ![Prompt 1](img/004/prompt_1.jpg) -->
<div style="text-align:center"><img src="img/004/prompt_1.jpg" /></div>
<div/>

A questo punto digitiamo **python** a lina di comando e poi premiamo **[Invio]**.

<!-- ![Prompt 2](img/004/prompt_2.jpg) -->
<div style="text-align:center"><img src="img/004/prompt_2.jpg" /></div>
<div/>

Se l'installazione di **python** è andata a buon fine ci troveremo davanti una scritta con informazioni di diversa natura, tra cui la versione di python installata, a dimostrazione del fatto che l'interprete python è stato trovato ed è pronto ad eseguire i nostri comandi.

<!-- ![Prompt 3](img/004/prompt_3.jpg) -->
<div style="text-align:center"><img src="img/004/prompt_3.jpg" /></div>
<div/>

**CONGRATULAZIONI!** Adesso siamo (quasi) in grado di scrivere dei programmi e automatizzare un sacco di operazioni noiose :)

#### Bonus: Installazione di atom

In precedenza abbiamo visto che i *sorgenti* di un programma sono costituiti da dei file di testo. Per scrivere in questi file abbiamo bisogno quindi di un **Editor**, cioè un programma per scrivere. Qualcuno potrebbe pensare al classico *Word*, ma quest'ultimo in realtà non va bene. Questo perchè *Word* non si limita a scrivere il testo che digitiamo dentro al file, ma aggiunge dei dati che gli servono per gestire correttamente la formattazione del testo e un sacco di altra roba che all'*interprete python* (ma anche ad un compilatore) darebbe fastidio, impedendoci di raggiungere il risultato sperato.

Un'alternativa percorribile potrebbe essere quella di utilizzare il **Blocco note** di *Windows* , ma in questo caso avremmo solo un foglio bianco e spoglio che non ci darebbe alcun tipo di aiuto a capire meglio cosa stiamo scrivendo.

Per ovviare a questi problemi la soluzione che ti propongo è quella di utilizzare **Atom** , un editor di testo molto potente e molto flessibile, creato dai programmatori per i programmatori. Presenta molti difetti (tra i quali le prestazioni non esattamente eccellenti), ma supporta nativamente molti linguaggi (tra cui python) senza bisogno di effettuare alcun setup particolare ed è molto molto semplice da installare, motivo per cui l'ho trovato adatto per quello che dobbiamo fare.

In modo molto simile a *python*, come prima cosa vai con il browser all'indirizzo: https://atom.io/ dove vedrai qualcosa di molto simile:

<!-- ![Download Atom 1](img/004/atom_dl.jpg) -->
<div style="text-align:center"><img src="img/004/atom_dl.jpg" /></div>
<div/>

A questo punto ti verrà chiesto di confermare il download in modo simile a prima:

<!-- ![Download Atom 2](img/004/atom_exe.jpg) -->
<div style="text-align:center"><img src="img/004/atom_exe.jpg" /></div>
<div/>

Confermiamo il download e lanciamo l'eseguibile, a questo punto partirà automaticamente l'installazione, con una simpatica animazione che indica che l'installazione di Atom è in corso e che una volta terminata il programma verrà avviato automaticamente:

<!-- ![Install Atom](img/004/wait_atom.jpg) -->
<div style="text-align:center"><img src="img/004/wait_atom.jpg" /></div>
<div/>

Una volta terminata l'installazione **Atom** si avvierà e dovremmo trovarci davanti qualcosa del genere:

<!-- ![Atom](img/004/atom_ready.jpg) -->
<div style="text-align:center"><img src="img/004/atom_ready.jpg" /></div>
<div/>

Adesso siamo veramente pronti per programmare!

**NOTA BENE:** Atom non è l'unico editor in circolazione che si utilizza per programmare. Ce ne sono un sacco e di diversa natura, ma questo è completamente gratuito, *open source* (vedremo cosa vuol dire più avanti) e, ultimo ma non meno importante, io lo uso per lavorare (e per scrivere le pillole), il che ci permette di lavorare con lo stesso strumento e quindi posso darti una mano con le sue funzioni se ne avessi bisogno. Ma vediamo come installarlo.

Nella prossima puntata vedremo un paio di funzioni utili per cominciare ad utilizzare *Atom* e come scrivere il nostro primo programma in **python** !
