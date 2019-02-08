# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 02:34:52 2019

@author: Camilo Vega
"""

import requests, re, random, time
from bs4 import BeautifulSoup


for i in range(1,51):
    
    ebook = random.randint((i-1)*100+1,i*100)
    page = requests.get("http://www.gutenberg.org/ebooks/"+str(ebook))
    soup = BeautifulSoup(page.content, 'html.parser')
    
    bibrec = soup.find(class_="bibrec")
    
    noinfo = "No Info" # string usado cuando no haya información respecto a un campo
    
    #Encontrar datos del autor
    print("Ebook No: "+str(ebook))
    author = bibrec.find("th",string="Author")
    authorBirth = 0
    authorDeath = 0
    if(author != None):
        author.next_sibling.next_sibling
        authorLife = [int(s) for s in re.findall(r'\d+',author.get_text())]
        #print(authorLife)
        authorNames = author.get_text().split(",")
        #En algunos casos el autor puede no ser una persona. Por tanto no tiene año de nacimiento
        if len(authorLife) != 0 : 
            authorNames.pop()
            authorBirth = authorLife[0]
            authorDeath = authorLife[1]
         
        authorName = ""
        
        for s in authorNames:
            authorName += s
        
        #print(authorName )
    else:
        authorName = noinfo
        
    
    ##Encontrar Editor
    
    editor= bibrec.find("th",string="Editor")
    if editor != None :
        editor = editor.next_sibling.next_sibling
        editor = editor.get_text()
        #print("\nEditor: " + editor)
    else:
        editor = noinfo
    
    # Encontrar Illustrator
    
    illustrator= bibrec.find("th",string="Illustrator")
    if illustrator != None :
        illustrator = illustrator.next_sibling.next_sibling
        illustrator = illustrator.get_text()
        #print("\nEditor: " + illustrator)
    else:
        illustrator = noinfo
    
    # Encontrar Title
    
    title=bibrec.find(itemprop="headline")
    if title != None:
        title = title.get_text()
        #print("\nTitle: "+title)
    else:
        title = noinfo
    
    # Encontrar Note
    
    note= bibrec.find("th",string="Note")
    if note != None :
        note = note.next_sibling.next_sibling
        note = note.get_text()
        #print("\nNote: " + note)
    else:
        note = noinfo
    
    
    # Encontrar Contents
    
    contents= bibrec.find("th",string="Contents")
    if contents != None :
        contents = contents.next_sibling.next_sibling
        contents = contents.get_text()
        #print("\nContents: " + contents)
    else:
        contents = noinfo
    
    # Encontrar Alternative Title
    
    altTitle=bibrec.find(itemprop="alternativeHeadline")
    if altTitle != None:
        altTitle = altTitle.get_text()
        #print("\nAlternative Title: "+altTitle)
    else:
        altTitle = noinfo
    
    # Encontrar Language
    
    language= bibrec.find("th",string="Language")
    if language != None :
        language = language.next_sibling.next_sibling
        language = language.get_text()
        #print("\nLanguage: " + language)
    else:
        language = noinfo
    ##Encontrar LoC Class
    
    locClass=bibrec.find(datatype="dcterms:LCC")
    if locClass != None:
        locClass = locClass.a.get_text()
        #print("\nLoc Class: "+locClass)
    else:
        subject = noinfo
    
    ##Encontrar Subject
    
    subject = bibrec.find("th",string="Subject")
    if subject != None : 
        subject = subject.next_sibling.next_sibling
        subject = subject.get_text()
        #print("\nSubject: " + subject)
    else:
        subject = noinfo
    
    # Encontrar Category
    
    category = bibrec.find("th",string="Category")
    if category != None : 
        category = category.next_sibling.next_sibling
        category = category.get_text()
        #print("\nCategory: " + category)
    else:
        category = noinfo
    
    # Encontrar Ebook no    
    ##Sacarlo de la url    
    #ebook = i
    
    # Encontrar Release date
    
    release=bibrec.find(itemprop="datePublished")
    if release != None:
        date = release.get_text().split()
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        month = months.index(date[0])+1
        day = re.findall(r'\d+',date[1])[0]
        year = date[2]
        
        
        release=str(month)+"/"+day+"/"+year
        #print("\nRelease Date: "+release)
    else:
        release = "0/0/0"
    
    # Encontrar Copyright status
    
    rights=bibrec.find(property="dcterms:rights")
    if rights != None:
        rights = rights.get_text()
        #print("\nCopyrights: "+rights)
    # Encontrar Downloads
    else:
        rights = noinfo
    
    downloads=bibrec.find(itemprop="interactionCount")
    if downloads != None:
        downloads = int(downloads.get_text().split()[0])
        #print("\nDownloads: "+ str(downloads))
    else:
        downloads = 0
    # Encontrar Price
    
    price=bibrec.find(itemprop="price")
    if price != None:
        price = int(re.findall(r'\d+',price.get_text())[0])
        #print("\nPrice: "+ str(price))
    else:
        price = 0
    
    
    # Encontrar Qr info
    qr = "http://m.gutenberg.org/ebooks/"+str(ebook)
    
    
    
    
    
    
    urlLogin = "http://scraping-test.herokuapp.com/users/login"
    urlForm = "http://scraping-test.herokuapp.com/book/add/"
    
    with requests.Session() as s:
        csrf = s.get(urlLogin).cookies['csrftoken']
#        print(csrf)

        
        loginData = dict(username = 'camilovega',
                       password = 'kYH8CJ3DtP8xEK93DECwxqnyNGAK9vxA',
                       csrfmiddlewaretoken=csrf)#,
        r=s.post(urlLogin,data=loginData)
#        print(r.status_code)

        
        csrf = s.cookies['csrftoken']
#        print(csrf)
        
        bookData = dict(csrfmiddlewaretoken=csrf,
                        book_id = ebook,
                        author_name = authorName,
                        author_birth_year = authorBirth,
                        author_death_year = authorDeath,
                        editor = editor,
                        illustrator = illustrator,
                        title = title,
                        note = note,
                        contents = contents,
                        alternate_title = altTitle,
                        language = language,
                        loc_class = locClass,
                        subject = subject,
                        category = category,
                        ebook_no = ebook,
                        release_date = release,
                        copyright_status = rights,
                        downloads = downloads,
                        price = price,
                        qr_info = qr,
                        test = True,
                        )
        q = s.post(urlForm,data=bookData)
        
        #soupQ = BeautifulSoup(q.content,'html.parser')
        #print(soupQ.prettify)
        print(q.content)
        if i%5 == 0:
            time.sleep(5)
            print("Sleep time in i = "+ str(i))
            