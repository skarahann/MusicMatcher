##This imports the stuff needed to run Flask. request allows you to get the value, render_template allows
##you to display an html page
from flask import Flask,request,render_template
import random
app = Flask(__name__, template_folder="/home/karahann/MusicMatcher/app/templates")

##This creates the flask app. template_folder is the directory of the folder called templates

##When the someone first goes to the site, the app will load up this template(html page).
@app.route("/")
def index():
    page = random.randint(0,3)

    if page == 0:
	    return render_template('index.html')
    if page == 1:
	    return render_template('index2.html')
    if page == 2:
        return render_template('index3.html')
    if page == 3:
        return render_template('index4.html')

##When someone clicks submit after selecting a value, the html page sends a the slider value to this
@app.route("/test", methods=["POST"])
def test():

     ####################################### GET GENRE

     song = int(request.form["bdylansongwriter"])
     psych = int(request.form["acollctivepsychedelic"])
     rnb = int(request.form["foceanrb"])
     elec = int(request.form["mgmtelectronic"])
     rap = int(request.form["nasrap"])
     pop = int(request.form["miapop"])
     exp = int(request.form["grimesexperimental"])
     rock = int(request.form["radioheadrock"])
     soul = int(request.form["mgayesoul"])
     amb = int(request.form["atwinambient"])

     genreVals = [song, psych, rnb, elec, rap, pop, exp, rock, soul, amb]
     genreList = ["Singer-Songwriter", "Psychedelic", "R&B", "Electronic", "Hip-Hop/Rap", "Pop", "Experimental", "Rock", "Soul", "Ambient"]

     maxVal = song
     index = 0
     favGenre = genreList[0]

     for x in range(10):
          if genreVals[x] >= maxVal:
                  index = x
                  favGenre = genreList[x]
                  maxVal = genreVals[x]

     ####################################### GET SONG

     artistIndex = random.randint(0, 4)
     songIndex = random.randint(0, 2)

     artist = ""
     song = ""

     #ROCK
     rockTOP=["radiohead","pink floyd","the strokes","arcade fire","the killers"]
     radioheadTOP=["let down","idioteque", "there there"]
     pinkfloydTOP=["money","time", "hey you"]
     thestrokesTOP=["someday","time to explain", "new york city cops"]
     arcadefireTOP=["wake up","the suburbs", "ready to start"]
     thekillersTOP=["smile like you mean it","all these things that i've done", "change your mind"]

     if index == 7:
          artist = rockTOP[artistIndex].title()

          if artistIndex == 0:
               song = radioheadTOP[songIndex].title()
          if artistIndex == 1:
               song = pinkfloydTOP[songIndex].title()
          if artistIndex == 2:
               song = thestrokesTOP[songIndex].title()
          if artistIndex == 3:
               song = arcadefireTOP[songIndex].title()
          if artistIndex == 4:
               song = thekillersTOP[songIndex].title()
               if song == "All These Things That I'Ve Done":
                    song = "All These Things That I've Done"

     #electronic
     electronicTOP=["burial","brian eno","MGMT","daft punk","lcd soundsystem"]
     burialTOP=["archangel","in mcdonalds","raver"]
     brianenoTOP=["emerald and stone","signals","stars"]
     mgmtTOP=["kids","electric feel","weekend wars"]
     daftpunkTOP=["instant crush","one more time","around the world"]
     lcdsoundsysTOP=["someone great","home","all my friends"]

     if index == 3:
          artist = electronicTOP[artistIndex].title()
          if artist == "Mgmt":
               artist = "MGMT"
          if artist == "Lcd Soundsystem":
               artist = "LCD Soundsystem"
          if artistIndex == 0:
               song = burialTOP[songIndex].title()
          if artistIndex == 1:
               song = brianenoTOP[songIndex].title()
          if artistIndex == 2:
               song = mgmtTOP[songIndex].title()
          if artistIndex == 3:
               song = daftpunkTOP[songIndex].title()
          if artistIndex == 4:
               song = lcdsoundsysTOP[songIndex].title()

     #hiphop
     hiphopTOP=["kanye west","kid cudi","nas","future","lil uzi vert"]
     kanyeTOP=["runaway","touch the sky","paranoid"]
     kidcudiTOP=["just what i am","soundtrack 2 my life","mojo so dope"]
     nasTOP=["represent","hate me now","N.Y. state of mind"]
     futureTOP=["stick talk","digital dash","i serve the base"]
     liluziTOP=["hi roller","malfunction","scott and ramona"]

     if index == 4:
          artist = hiphopTOP[artistIndex].title()

          if artistIndex == 0:
               song = kanyeTOP[songIndex].title()
          if artistIndex == 1:
               song = kidcudiTOP[songIndex].title()
          if artistIndex == 2:
               song = nasTOP[songIndex].title()
          if artistIndex == 3:
               song = futureTOP[songIndex].title()
          if artistIndex == 4:
               song = liluziTOP[songIndex].title()

     #singer-songwriter
     singerTOP=["bob dylan","sufjan stevens","bon iver","father john misty","mac demarco"]
     bobdylanTOP=["hurricane","tangled up in blue","fourth time around"]
     sufjanstevTOP=["the only thing","chicago","fourth of july"]
     boniverTOP=["holocene","flume","beach baby"]
     fatherjohnmistTOP=["pure comedy","the pellets","strange encounter"]
     macdemarcoTOP=["let her go","salad days","on the level"]

     if index == 0:
          artist = singerTOP[artistIndex].title()

          if artistIndex == 0:
               song = bobdylanTOP[songIndex].title()
          if artistIndex == 1:
               song = sufjanstevTOP[songIndex].title()
          if artistIndex == 2:
               song = boniverTOP[songIndex].title()
          if artistIndex == 3:
               song = fatherjohnmistTOP[songIndex].title()
          if artistIndex == 4:
               song = macdemarcoTOP[songIndex].title()


     #psychedelic
     psychTOP=["beach house","tame impala","the beatles","animal collective","the flaming lips"]
     beachTOP=["lemon glow","myth","zebra"]
     tameTOP=["the less i know the better","eventually","elephant"]
     beatlesTOP=["hey jude","let it be","here comes the sun"]
     animalTOP=["in the flowers","man of oil","fireworks"]
     flamingTOP=["race for the prize","do you realize","yoshimi battles the pink robots part 1"]

     if index == 1:
          artist = psychTOP[artistIndex].title()

          if artistIndex == 0:
               song = beachTOP[songIndex].title()
          if artistIndex == 1:
               song = tameTOP[songIndex].title()
          if artistIndex == 2:
               song = beatlesTOP[songIndex].title()
          if artistIndex == 3:
               song = animalTOP[songIndex].title()
          if artistIndex == 4:
               song = flamingTOP[songIndex].title()

     #r&b
     rbTOP=["frank ocean","prince","michael jackson","solange","the weeknd"]
     foceanTOP=["thinking about you","super rich kids","lost"]
     princeTOP=["purple rain","1999","little red corvette"]
     mjTOP=["beat it","smooth criminal","(i like) the way you love me"]
     solTOP=["cranes in the sky","mad","so be it"]
     weekndTOP=["often","can't feel my face","reminder"]

     if index == 2:
          artist = rbTOP[artistIndex].title()

          if artistIndex == 0:
               song = foceanTOP[songIndex].title()
          if artistIndex == 1:
               song = princeTOP[songIndex].title()
          if artistIndex == 2:
               song = mjTOP[songIndex].title()
          if artistIndex == 3:
               song = solTOP[songIndex].title()
          if artistIndex == 4:
               song = weekndTOP[songIndex].title()

     #pop
     popTOP=["lorde","beyonce","carly rae jepsen","lana del rey","lady gaga"]
     lordeTOP=["ribs","supercut","perfect places"]
     beyonceTOP=["7/11","halo","rockit"]
     carlyrjTOP=["when i needed you","emotion","cut to the feeling"]
     lanaTOP=["born to die","blue jeans","ultraviolence"]
     gagaTOP=["million reasons","applause","the cure"]

     if index == 5:
          artist = popTOP[artistIndex].title()

          if artistIndex == 0:
               song = lordeTOP[songIndex].title()
          if artistIndex == 1:
               song = beyonceTOP[songIndex].title()
          if artistIndex == 2:
               song = carlyrjTOP[songIndex].title()
          if artistIndex == 3:
               song = lanaTOP[songIndex].title()
          if artistIndex == 4:
               song = gagaTOP[songIndex].title()

     #soul
     soulTOP=["stevie wonder","marvin gaye","aretha franklin","nina simone","d'angelo"]
     swonderTOP=["sir duke","look around","love having you around"]
     marvinTOP=["let's get it on","what's going on","i heard it through the grapevine"]
     arethafTOP=["respect","think","i say a little prayer"]
     ninasTOP=["feeling good","baltimore","here comes the sun"]
     dangeloTOP=["really love","sugah daddy","lady"]

     if index == 8:
          artist = soulTOP[artistIndex].title()

          if artistIndex == 0:
               song = swonderTOP[songIndex].title()
          if artistIndex == 1:
               song = marvinTOP[songIndex].title()
          if artistIndex == 2:
               song = arethaTOP[songIndex].title()
          if artistIndex == 3:
               song = ninasTOP[songIndex].title()
          if artistIndex == 4:
               song = dangeloTOP[songIndex].title()

     #ambient
     ambientTOP=["aphex twin","fennesz","moby","the klf","stars of the lid"]
     atwinTOP=["avril 14th","aisatsana","#3"]
     fenneszTOP=["haru","oto","rivers of sand"]
     mobyTOP=["porcelain","why does my heart feel so bad?","natural blues"]
     theklfTOP=["justified & ancient","3 A.M. eternal","last train to trancentral"]
     starslidTOP=["don't bother they're here","a meaning moment through a meaning(less) process","dungtitled(in a major)"]

     if index == 9:
          artist = ambientTOP[artistIndex].title()

          if artistIndex == 0:
               song = atwinTOP[songIndex].title()
          if artistIndex == 1:
               song = fenneszTOP[songIndex].title()
          if artistIndex == 2:
               song = mobyTOP[songIndex].title()
          if artistIndex == 3:
               song = theklfTOP[songIndex].title()
          if artistIndex == 4:
               song = starslidTOP[songIndex].title()

     #experimental
     experimentalTOP=["grimes","flying lotus","alt-j","panda bear","the books"]
     grimesTOP=["kill v. maim","genesis","venus fly"]
     flyinglotTOP=["never catch me","camel","do the astral plane"]
     altjTOP=["tessellate","matilda","left hand free"]
     pandaTOP=["boys latin","mr noah","tropic of cancer"]
     thebooksTOP=["cello song","smells like content","the lemon of pink I"]

     if index == 6:
          artist = experimentalTOP[artistIndex].title()

          if artistIndex == 0:
               song = grimesTOP[songIndex].title()
          if artistIndex == 1:
               song = flyinglotTOP[songIndex].title()
          if artistIndex == 2:
               song = altjTOP[songIndex].title()
          if artistIndex == 3:
               song = pandaTOP[songIndex].title()
          if artistIndex == 4:
               song = thebooksTOP[songIndex].title()

     ####################################### Return

     return '<html><head> <style> body {background-color: #cdfcbd; font-family: Helvetica, sans-serif;} div {z-index: 9999999;} p {margin-left: 115px; font-weight: 100; margin-top: 69px;} </style></head><body> <p>Recommended Genre: %s</p> <p>Recommended Artist: %s</p> <p>Recommended Song: %s</p><break></break><p>Want another recommendation? Go back, refresh the page until a new playlist comes up, and start another survey! </p></body></html>' % (favGenre, artist, song)

     #return "Recommended Genre: " + favGenre + "\n   ||   Recommended Artist: " + artist + "\n   ||   Recommended Song: " + song

if __name__=="__main__":
    app.run()
