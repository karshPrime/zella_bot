#!/usr/bin/env python
from bs4 import BeautifulSoup as soup
import string, random, re, urllib.request
from difflib import SequenceMatcher

#! ==
#! Backend for commands at main file.
#// install "Better Comments" extension to have color coded commments
#// for clearer code understanding.
#! ==

#?                   _       _     _
#?  __   ____ _ _ __(_) __ _| |__ | | ___  ___ 
#?  \ \ / / _` | '__| |/ _` | '_ \| |/ _ \/ __|
#?   \ V / (_| | |  | | (_| | |_) | |  __/\__ \
#?    \_/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/

about = '''Hey I'm Zella! :v:
With me you can do more than just texting on discord'''

confessions = '''DM me your confessions and I'll post em anonymously in the confession channel.
Be civilised; no one would ever find out who made what confession ;)'''

commands = '''
**)confess {message}**
- DM me this with your message and I will post your message in the confession channel anonymously.
- __Aliases__: `)listen {message}` | `)confession {message}`

**)youtube {query}**
- Search for YouTube videos!
- __Aliases__: `)yt {query}` | `)vid {query}`

**)ping**
- Pretty self-explanatory command, I guess?
'''


#! ==

#?   __                  _   _                 
#?  / _|_   _ _ __   ___| |_(_) ___  _ __  ___ 
#? | |_| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
#? |  _| |_| | | | | (__| |_| | (_) | | | \__ \
#? |_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
#?                                             

#! replaces space and other special characters from string with given character
def char_manage(text, new_char):
    modified = re.sub(r'\W+', new_char, text)
    modified = modified.replace(" ", "")
    return modified


#! searches query over youtube and get result link
def youtube(query):
    query = char_manage('-', query)
    html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={query}&persist_gl=1&gl=GB")
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    return(video_ids[0])


#! generates random id for confession message
def random_id():
    length = random.randint(10, 15)
    letters_and_digits = string.ascii_letters + string.digits
    random_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return random_str


#! generates random id for confession message
def welcome_banner():
    gifs = ["https://media.discordapp.net/attachments/824248041472000000/876012017180352512/tumblr_9c5c32a5bb3f8153de0c0000212649c9_cf333092_540.gif", 
    "https://media.discordapp.net/attachments/824248041472000000/876012021269794846/056c584d9335fcabf080ca43e583e3c4.gif",
    "https://media.discordapp.net/attachments/824248041472000000/876012077544796200/giphy.gif",
    "https://thumbs.gfycat.com/LikableYellowGander-max-1mb.gif",
    "https://4.bp.blogspot.com/-egMobIIe0A4/W9nlY--Ti0I/AAAAAAAABWk/hb8jgZVY-48HlS8mhJjZH27i4qQVkOElwCLcBGAs/s1600/HauntingNeighboringBarracuda-size_restricted.gif",
    "https://gifimage.net/wp-content/uploads/2017/09/anime-waving-gif-13.gif",
    "https://media1.tenor.com/images/e70e12421ce18e24afd523e02c9dced1/tenor.gif",
    "https://49.media.tumblr.com/63c2cf52d13e6db473e2a5ad504b1140/tumblr_nr0k9kf6Gt1r69x9to1_500.gif",
    "https://3.bp.blogspot.com/-cWR1N6ovSyU/Ud-cOx4JuGI/AAAAAAAABSU/y61salU94tc/s1600/waving_bye.gif",
    "https://pa1.narvii.com/6357/73a065abe6045d20a82eabec7bbedb33c7e54885_hq.gif",
    "https://i.imgur.com/csNlH4T.gif",
    "https://data.whicdn.com/images/181921048/original.gif",
    "https://25.media.tumblr.com/tumblr_m7tkybMt031qj11udo1_r1_500.gif",
    "https://i.imgur.com/VM9lRSw.gif",
    "https://31.media.tumblr.com/012e040c8f587faa3c3a4a72f807a362/tumblr_inline_nf4s2p40Gs1ried37.gif",
    "https://1.bp.blogspot.com/-KiJJ5veHr-A/VTe9ix5YVHI/AAAAAAAAABI/KLCskDPqvbE/s1600/tumblr_lyq9w0k7tk1r5ye76o1_500.gif",
    "https://c.tenor.com/_M7zXM-HEDMAAAAC/yuudachi-anime.gif",
    "https://c.tenor.com/fdBl0nVdriIAAAAd/fairy-tail-chelia.gif",
    "https://c.tenor.com/TKMqMAkJL8wAAAAC/anime-wave-anime-hi.gif",
    "https://c.tenor.com/o9Ak0TpPek0AAAAC/aikatsu-aikatsu-hello.gif",
    "https://c.tenor.com/MIXsMsU90KMAAAAC/hey-hello.gif",
    "https://c.tenor.com/Rf5v6glMta8AAAAC/hey-waves.gif",
    "https://c.tenor.com/e48wByvWU-IAAAAC/anime-hi.gif",
    "https://c.tenor.com/FMpLzF4UJhwAAAAC/kisumi-wave.gif",
    "https://c.tenor.com/ESVgd3T5YlcAAAAC/demon-slayer-anime.gif",
    "https://c.tenor.com/AuBOgaPV41cAAAAC/shinya-shinyahiragi.gif",
    "https://c.tenor.com/NjsosaK61UIAAAAC/anime-girl.gif",
    "https://c.tenor.com/EERR4LXoJBoAAAAd/hi-wave.gif",
    "https://c.tenor.com/Eok6d6MQhg4AAAAC/cute-smile.gif",
    "https://c.tenor.com/TUFqLtiqhXgAAAAC/sad-smile-smile.gif",
    "https://c.tenor.com/Uyki_ZbnmKwAAAAC/hearts-love.gif",
    "https://c.tenor.com/MZXGjlCbMcwAAAAC/luffy-one-piece.gif",
    "https://c.tenor.com/VluaEmtxm0sAAAAC/anime-darling-in-the-franxx.gif",
    "https://c.tenor.com/W4deQTUzHswAAAAC/anime-smile.gif",
    "https://c.tenor.com/WFxzA4PQTiEAAAAC/smile-anime.gif",
    "https://c.tenor.com/PfMkNZdluAkAAAAC/haru-yoshida-tonari-no-kaibutsu-kun.gif",
    "https://c.tenor.com/Ur_pBB1YBlwAAAAC/himouto-umaru-chan-smile.gif",
    "https://c.tenor.com/MRIkRK5l_coAAAAC/chitoge.gif",
    "https://c.tenor.com/F7auL2aTMrYAAAAC/nejire-hado-pretty.gif",
    "https://c.tenor.com/sPgkxwu-MRsAAAAC/anime-tokyo-revengers.gif",
    "https://c.tenor.com/ZalLZIPLw0EAAAAC/black-clover-smiling.gif",
    "https://c.tenor.com/mTbqykLo0_oAAAAd/kawai-smile.gif",
    "https://c.tenor.com/U1p83COiAPYAAAAC/anime-happy-anime-smile.gif",
    "https://c.tenor.com/3fAZZncIHDQAAAAC/smile-anime.gif",
    "https://c.tenor.com/Q--iyrFnBw8AAAAC/anime-smile.gif",
    "https://c.tenor.com/4OuG2hfJuuEAAAAC/cute-smile-anime-cunning.gif",
    "https://c.tenor.com/OaEPW8_sX1QAAAAC/camie-my-hero-academia.gif",
    "https://c.tenor.com/8-jJyFqnWxwAAAAC/steins-gate-wave.gif",
    "https://c.tenor.com/w_o8CAlY3BAAAAAC/mayuri-steins-gate.gif",
    "https://c.tenor.com/MGatCffhfskAAAAC/gintama-kamui.gif",
    "https://c.tenor.com/xDGL-kz_AsUAAAAC/wave-smile.gif",
    "https://c.tenor.com/oBQgHnlu348AAAAC/hello-chibi.gif",
    "https://c.tenor.com/PcS_tPEeW70AAAAC/bye-jojo.gif",
    "https://c.tenor.com/RfoR1hZMrZ8AAAAC/one-piece-smile.gif",
    "https://c.tenor.com/a_EbF7LvJOgAAAAd/fairy-tail-mirajane-strauss.gif",
    "https://c.tenor.com/om0-IewhKx0AAAAC/luffy-child.gif",
    "https://c.tenor.com/3WNdSEBBeQkAAAAC/ijirinaide-nagatoro-san-please-dont-bully-me-nagatoro-san.gif"]
    return gifs[random.randint(0, (len(gifs) -1))]


#! generates random color
def random_color():
    return random.randint(0, 0xffffff)


#! ==