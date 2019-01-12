from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup

print('Enter the path of exported Google+ Stream data post folder (Takeout/Google+ Stream/Posts):')
postpath = input()
posthtmls = [filename for filename in listdir(postpath) if isfile(join(postpath, filename)) and filename.endswith(".html") and filename != "archive.html"]

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

outfile = open(join(postpath, "archive.html"), "w+", encoding="utf-8")

sketch = BeautifulSoup(open(join(postpath, posthtmls[0]), "r", encoding="utf-8"), "html.parser")
sketch.body.clear()
sketch.title.string.replace_with("Google+ Archive")
posthtmls.reverse()
for filename in posthtmls:
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

outfile.write(sketch.prettify())
outfile.close()
print("The generated HTML file is saved as " + join(postpath, "archive.html"))
print("Upload the file with all image filed under posts folder to serve it online")
