import requests
from bs4 import BeautifulSoup as bs
import random

#payload = "I was born with a dick in my brain yeah fucked in the head"# My stepfather said that I sucked in the bed Til one night he snuck in and said We are going out back, I want my dick sucked in the shed Cannot we just play with Teddy Ruxpin instead? After I fuck you in the butt, get some head Bust a nut, get some rest The next day my mother said I do not know what the fuck is up with this kid! The bastard will not even eat nothing he is fed He just hung himself in the bedroom he is dead Debbie do not let that fucker get you upset Go in there, stick a fucking cigarette to his neck I bet you he is faking it, I bet you I bet he probably just wants to see how upset you would get I will go handle this of course, unless you object Ahh go fuck his brains out, if any is left "
#payload = "Let it go let it go Cannot hold it back any more "#Let it go let it go Turn away and slam the door I do not care what they are going to say Let the storm rage on The cold never bothered me anyway"#"The snow glows white on the mountain tonight Not a footprint to be seen A kingdom of isolation And it looks like I am the queen The wind is howling like this swirling storm inside"# Could not keep it in heaven knows I have tried Do not let them in do not let them see Be the good girl you always have to be Conceal do not feel do not let them know Well, now they know Let it go let it go Cannot hold it back anymore Let it go let it go Turn away and slam the door I do not care what they are going to say Let the storm rage on The cold never bothered me anyway Let it go let it go Cannot hold it back anymore Let it go let it go Turn away and slam the door Let it go  Let it go Let it go Let it go It is funny how some distance makes"
#payload = "Amazing grace how sweet the sound That saved a wretch like me I once was lost but now am found Was blind but now I see was grace that taught my heart to fear And grace my fears relieved How precious did that grace appear The hour I first believed Through many dangers toils and snares I have already come is grace hath brought me safe thus far And grace will lead me home The Lord has promised good to me His word my hope secures He will my shield and portion be As long as life endures Yeah when this flesh and heart shall fail and mortal life shall cease I shall possess within the veil A life of joy and peace When we have been there ten thousand years Bright shining as the sun We have no less days to sing God praise Than when we have first begun"
#payload = "Oh what a night Late December back in sixty three What a very special time for me As I remember what a night Oh what a night You know I didn not even know her name But I was never gonna be the same What a lady what a night Oh I I got a funny feeling when she walked in the room Hey my As I recall it ended much too soon Oh what a night Hypnotizing mesmerizing me She was everything I dreamed she would be Sweet surrender what a night And I felt a rush like a rolling bolt of thunder Spinning my head around and taking my body under Oh what a night Oh I Got a funny feeling when she walked in the room Hey my As I recall it ended much too soon Oh what a night Why did it take so long to see the light Seemed so wrong but now it seems so right What a lady what a night Oh I felt a rush like a rolling bolt of thunder Spinning my head around and taking my body under"
#payload = "Calling all comas Prisoner on the loose Description A spitting image of me Except for a heart shaped hole where the hope runs out Shock me awake Tear me apart Pinned like a note in a hospital gown Prison of sleep Deepened now A rabbit hole never to be found Again Where are you hiding my love Cast off like a stone Feelings raw and exposed when I am out of control Pieces were stolen from me But dare I say given away Watching the water give in As I go down the drain I appear missing now I go missing No longer exist One day I hope I am someone you had met Shock me awake Tear me apart Pinned like a note in a hospital gown Deeper I sleep Further down A rabbit hole never to be found It is only falling in love Because you hit the ground Dancing on wire both ends are on fire Cut me loose Nowhere to run no more room to pretend Wandering along the road in the summer night I go missing No longer exist One day I hope I am someone you had met Shock me awake Tear me apart Pinned like a note in a hospital gown Deeper I sleep Further down A rabbit hole never to be found Do not cry With my toes on the edge it is such a lovely view Inside I never loved anything until I loved you Inside I am over the edge what can I do Inside I never loved anything until I loved you Do not cry With my toes on the edge it is such a lovely view Inside I never loved anything until I loved you Inside I am over the edge what can I do Inside I have fallen through"
#payload = "Ain't nothing gonna break my stride Nobody gonna slow me down oh no I got to keep on moving Ain't nothing gonna break my stride I am running and I will not touch ground Oh no I got to keep on moving"
#payload = "Who loves you"# Ask yourself the question Who loves you sweetheart And tell me who thinks of you A million times a day And who is blue and lonely honey When you are away Say who needs you Needs you every minute Who fell for you from the start Oh who just longs for your caresses You do not have to take three guesses Who loves you sweetheart"
#payload = "We are no strangers to love You know the rules and so do I A full commitment is what I am thinking of You would not get this from any other guy I just wanna tell you how I am feeling Gotta make you understand Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you We have known each other for so long Your heart has been aching but You are too shy to say it Inside we both know what has been going on We know the game and we are gonna play it And if you ask me how i am feeling Don't tell me you're too blind to see Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give never gonna give Never gonna give never gonna give we have known each other for so long Your heart has been aching but You're too shy to say it Inside we both know what has been going on We know the game and we are gonna play it I just wanna tell you how i am feeling Gotta make you understand Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you"
#payload = "the nighe is dark i am afraid of the waves this savage whirlpool terrifies me you who walk on the distant shore light burdened what do you know of my inner state"
payload = "All that is gold does not glitter Not all those who wander are lost The old that is strong does not wither Deep roots are not reached by the frost From the ashes a fire shall be woken A light from the shadows shall spring Renewed shall be blade that was broken The crownless again shall be king"
payload = payload.lower()
payload = payload.split(" ")

notwords = ["Ain't", "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

it = 0
it2 = 0
it3 = 0
it4 = 0
itt = 0
wordnum = 0
arr = []
arr2 = []
arr3 = []
arr4 = []
arr5 = []
rand = 0
synonymised = ""

for x in payload:
    r = requests.post(f'https://www.thesaurus.com/browse/{x}')
    soup = bs(r.text, "html.parser")
    words = soup.select(".css-133coio")
    
    if x not in notwords:
        for word in words:
            if True:
                    arr.append([it, x])
                    arr.append([it,word.text.strip()])
                    #synonymised += word.text.strip() + " "
                    #print(type(word.text.strip()))
                    #print(word.text.strip())
                    itt = 1
                    wordnum+=1
    else:
        arr.append([it,x])
        wordnum+=1
        #synonymised += x + " "
            
            
    print(wordnum)
    itt = 0
    it+=1
    
for word in arr:
    arr3.append(word[0])

for x in arr3:
    if x not in arr4:
        arr4.append(x)
for o in arr4:
    if arr3.count(o) <= 44:
        arr5.append(arr3.count(o))
    else:
        arr5.append(44)
    
print(arr5)
        
for word in payload:
    for drow in arr:
        if it3<len(arr5):
            rand = random.randint(0,arr5[it3]-1)
        else:
            rand = 0
        if drow[0] == it3 and it2 == it3:
            arr2.append(arr[it4+rand][1])
            synonymised += arr[it4+rand][1] + " "
            it2+=1
        it4+=1
    it4 = 0
    it3+=1
print(arr2)
print(synonymised)
