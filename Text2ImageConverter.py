from PIL import Image, ImageDraw, ImageFont
import textwrap
from arabic_reshaper import ArabicReshaper
configuration = {
    'delete_harakat': False,
    '': True,
    'RIAL SIGN': True,  # Replace ر ي ا ل with ﷼
}
reshaper = ArabicReshaper(configuration=configuration)

# -----------------------------------------------------------------------------------------------------
surah_name = "Surah Al-Mujadilah (The Argument)"
file_name = "mujadilah"
Reciter = "Reciter: Sheikh Shuraim"
verse_sajda = ""
# -----------------------------------------------------------------------------------------------------
fil = open("c:/Users/Hamza Tahir/Desktop/Channel/Surahs/"+file_name+".txt",encoding='utf-8')
fil2 = open("c:/Users/Hamza Tahir/Desktop/Channel/Surahs/"+file_name+".txt",encoding='utf-8')

saj = open("c:/Users/Hamza Tahir/Desktop/Channel/Surahs/sajda.txt",encoding='utf-8')
sajda = saj.read()
reshaped_text = reshaper.reshape(sajda)
sajda = reshaped_text[::-1]  # slice backwards 


n = len(fil2.readlines())
fil_tr = open("c:/Users/Hamza Tahir/Desktop/Channel/Translations/" + file_name + ".txt",encoding='utf-"8')
for m in range(0,n):
    x = fil.readline()
    if(m == 0):
        print("Started")
    else:
        fil_tr.readline()
    trans = fil_tr.readline()
    trans_para = textwrap.wrap(trans,width=60)
    t = ""
    an = ""
    ch = False
    for i in x:
        if(i == "("):
            ch = True
            break
        elif(i == ")"):
            break
        if(ch == False):
            t = t+i
        elif(ch == True):
            an = an+i
    st = [an,t]
    ayahs = []
    for i in st:
        text_to_be_reshaped = i
        para = textwrap.wrap(text_to_be_reshaped,width=100)
        ayah = []
        for i in para:
            reshaped_text = reshaper.reshape(i)
            rev_text = reshaped_text[::-1]  # slice backwards 
            ayah.append(rev_text)
            
        ayahs.append(ayah)
    W,HS = (1920,1080)
    # create an image
    out = Image.open("C:/Users/Hamza Tahir/Desktop/Channel/pic2.png")
    d = ImageDraw.Draw(out)
    myFont0 = ImageFont.truetype('C:/Windows/Fonts/times.ttf', 70)
    myFont1 = ImageFont.truetype("C:/Windows/Fonts/times.ttf", 70)
    Font_s = ImageFont.truetype("C:/Windows/Fonts/times.ttf", 30)    
    if(len(ayahs[1]) == 1):
        H = 540-100
        # h2 = 1824-1200
    elif(len(ayahs[1]) == 2):
        w,h = d.textsize(ayahs[1][0], font=myFont1)
        H = 540-100-h-10
        # h2 = 1824-1700
    else:
        w,h = d.textsize(ayahs[1][0], font=myFont1)
        H = 540-100-h-10
        # h2 = 200

    
    w,h = d.textsize(surah_name, font=myFont0)
    h2 = 50
    d.text(((W-w)/2, h2), surah_name, font=myFont0, fill=(255, 255, 255))
    # d.rectangle([(W-w-15)/2,h2,(W+w+15)/2,h2+h+15],outline=(255,255,255),width=3)

    
    for line in ayahs[1]:
        w,h = d.textsize(line, font=myFont1)
        d.text(((W-w)/2, H), line, font=myFont1, fill=(255, 255, 255))
        H = H + h + 10
    if(m == verse_sajda):
        d.text((((W-w)/2)-70,H-80),sajda,font=Font_s,fill=(255, 255,255))

    myFont2 = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 50)

    if(H < 540):
        H = 600
    for line in trans_para:
        w,h = d.textsize(line, font=myFont2)
        d.text(((W-w)/2, H), line, font=myFont2, fill=(255, 255, 255))
        H = H + h + 10
    
    myFont3 = ImageFont.truetype('C:/Windows/Fonts/times.ttf', 40)
    w,h = d.textsize(Reciter, font=myFont3)
    d.text(((W-w)/2, HS-h-15), Reciter, font=myFont3, fill=(255, 255, 255))
    # --------------------------------------------------------------------------------------
    # out.show()
    out.save("C:/Users/Hamza Tahir/Desktop/shotcut_video/"+file_name+"/"+str(m)+".png")
print("completed")