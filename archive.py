from os import listdir
from os.path import isfile, join, exists
from bs4 import BeautifulSoup

postpath = input('Enter the path of exported Google+ Stream data post folder (Takeout/Google+ Stream/Posts):')
if not exists(postpath):
    raise Exception('Input path is not valid: ' + postpath)
posthtmls = [filename for filename in listdir(postpath) if isfile(join(postpath, filename)) and filename.endswith(".html") and not filename.startswith("archive")]

def checkfileattr(element, classname, attr):
    if not element.has_attr(attr):
        return False
    if not element.has_attr("class") or element["class"][0] != classname:
        return False
    if element[attr].startswith("https://"):
        return False
    if isfile(join(postpath, element[attr])):
        return False
    return True

def getpagename(pager):
    if pager == 1:
        return "archive.html"
    else:
        return "archive-" + str(pager) + ".html"

sketch = BeautifulSoup(open(join(postpath, posthtmls[0]), "r", encoding="utf-8"), "html.parser")
sketch.body.clear()
sketch.title.string.replace_with("Google+ Archive")
posthtmls.reverse()

pager = 1
postscount = 0
postsperpage = input('How many posts you want to show on one page? Enter -1 if unlimited:') 
try:
    postsperpage = int(postsperpage)
except ValueError:
    print('Your input is not a valid integer, all posts will be shown on the same page.')
    postsperpage = -1

outfile = open(join(postpath, getpagename(pager)), "w+", encoding="utf-8")
for filename in posthtmls:
    if postscount == 0:
        if pager != 1:
            if pager > 2:
                prevpage = sketch.new_tag("a", href=getpagename(pager - 2))
                prevpage.string = "Previous Page"
                sketch.body.append(prevpage) 
            nextpage = sketch.new_tag("a", href=getpagename(pager))
            nextpage.string = "Next Page"
            sketch.body.append(nextpage)
            outfile.write(sketch.prettify())
            outfile.close()
            sketch.body.clear()
            outfile = open(join(postpath, getpagename(pager)), "w+", encoding="utf-8")

    body = BeautifulSoup(open(join(postpath, filename), "r", encoding="utf-8"), "html.parser").body
    
    for image in body.find_all("img"):
        if checkfileattr(image, "media", "src"):
            if isfile(join(postpath, image["src"] + ".jpg")):
                image["src"] += ".jpg"
                image.parent["href"] += ".jpg"
            elif isfile(join(postpath, image["src"] + ".png")):
                image["src"] += ".png"
                image.parent["href"] += ".png"
    body.name = "div"
    sketch.body.append(body)
    postscount += 1
    if postscount == postsperpage:
        postscount = 0
        pager += 1

if postscount == 0:
    pager -= 1
if pager > 1:
    prevpage = sketch.new_tag("a", href=getpagename(pager - 1))
    prevpage.string = "Previous Page"
    sketch.body.append(prevpage) 
outfile.write(sketch.prettify())
outfile.close()
print("The generated HTML file(s) are saved as " + join(postpath, getpagename(1)))
print("Upload the files starting with archive with all image filed under posts folder to serve it online")
