import sys,os
from subprocess import run, CalledProcessError
try:
    import pmText,re,requests
    from pmText import color
    from bs4 import BeautifulSoup
except (ImportError,ImportWarning):
    if sys.version_info <= (3, 0): #need to use text in the file here due to python2 or missing pmText errors
        print("Make sure you are running this script with"
          " Python3. Use: python3 /path/to/pmt.py")
        exit()
    if not os.path.isfile("pmText.py"):
        print("Please place pmText.py in the same directory as pmt.py.")
        exit()
    print(pmText.noPackage)

def home():
    global page
    answer=None
    while (True):
        if (answer == None):
            try:
                answer = input(pmText.optionsA)
            except ValueError:
                print("\n")
                exit()
        if answer in ['m', 'M'] and search != '':
            page += 75
            retrieve()
        elif answer in ['x', 'X']:
            if myPPA():
                packageInspect()
        elif not otherOption(answer,printSearch):
            try:
                if int(answer) >= len(s_Results) or int(answer) < 0:
                    print(pmText.outOfRange)  # load more results
                else:
                    resultPage(int(answer))
            except ValueError:
                pass
        answer = None

def otherOption(a, printFun):
    global page
    if a in ['s', 'S']:
        startSearch()
        return True
    if a in ['dup','DUP','Dup']:
        try:
            run(['apt-get','dist-upgrade']).check_returncode()
            return True
        except CalledProcessError:
            print(pmText.processFail)
        except FileNotFoundError:
            print(pmText.noCommand)
    if a in ['u','U']:
        try:
            run(['apt-get', 'update']).check_returncode()
            return True
        except CalledProcessError:
            print(pmText.processFail)
        except FileNotFoundError:
            print(pmText.noCommand)
    if a in ['p','P'] and printFun != None:
        try:
            temp = page
            page = 0
            printFun()
            page = temp
            return True
        except:
            pass
    if a in ['q', 'Q']:
        quit()

def startSearch():
    global search, page
    search = input(pmText.searchTerm)
    page = 0
    html[:] = s_Results[:] = []  # empties list
    if search !=  '':
        retrieve()

def retrieve(): #grabs html and preps it
    url = 'https://launchpad.net/ubuntu/+ppas?name_filter=' + search + '&start=' + str(page)
    try:
        soup = BeautifulSoup(requests.get(url).text, "lxml")
        tables = soup.find('table', class_='listing sortable')
        for i in tables.findAll("tr"):
            cells = i.findAll('td')
            if len(cells) >= 1:
                html.append(str(cells))
    except NameError:
        print(pmText.noPackage + color.END)
    except ConnectionError:
        print(pmText.noConnect + url + color.END)
        home()
    except ImportError:
        print(pmText.noPackage + color.END)
    except AttributeError:
        print(pmText.noResults)
        pass
    else:
        for x in range(page, len(html)):
            a = BeautifulSoup(html[x], "lxml")
            s_Results.append([])
            s_Results[x].append(a.find('a')['href'])  # link
            s_Results[x].append(a.find('a').contents[0])  # href text/item name
            s_Results[x].append(str(html[x][16:]).split('/')[0]) #start at char 16, Split up file by '/'. Get author
        printSearch()

def printSearch():
    for i in range(page, len(s_Results)):
       print(pmText.searchPrint[0] + str(i) + pmText.searchPrint[1] + s_Results[i][1] +
             pmText.searchPrint[2] + s_Results[i][2] + pmText.searchPrint[3])

def resultPage(num):
    ppa_url = 'https://launchpad.net' + s_Results[num][0]
    try:
        soup = BeautifulSoup(requests.get(ppa_url).text, "lxml")
    except:
        print(pmText.noConnect + ppa_url + color.END)
        home()
    for p in soup.findAll('p'):
        print(''.join(p.findAll(text=True)))  # prints description text
    command = str(soup.find('pre').contents[0]) #finds the 'apt-add-repository' command on ppa page
    print(ppa_url) #print page url
    print(color.CYAN + command + color.END) #print command for user to see
    while (True):
        try:
            answer = input(pmText.optionsB) #choose to add ppa or do other stuff
            if answer in ['a', 'A']:
                command = command.replace("\n", " ") #converts the multi-line command from the website to single line
                i = re.compile('(ppa.*)s').findall(command)
                run(["apt-add-repository"] + i).check_returncode()
            else:
                otherOption(answer,printSearch)
                break
        except CalledProcessError:
            print(pmText.processFail)
        except FileNotFoundError:
            print(pmText.noCommand)
            pass
        except ValueError:
            print("\n")
            exit()

def myPPA(): #lists ppa's in system
    global listFile
    try:
        dirPPA = os.listdir(dir)
        if not dirPPA:
            print(pmText.noPPA)
    except:
        print(pmText.noFolder + "\n" + pmText.noCommand)
        home()
    def rePrint():
        for i in range(0, len(dirPPA)):
            if (dirPPA[i].endswith('.list') or dirPPA[i].endswith('.save')) and not os.path.isdir(dir + dirPPA[i]):
                print(color.RED + color.BOLD + str(i) + "\t" + color.END + dirPPA[i])
            else: #finds file that doesnt have .list or .list.save or is a dir
                print(color.BLUE + color.BOLD + str(i) + "\t" + dirPPA[i] + pmText.weirdPPA + dirPPA[i] + color.END)
    rePrint()
    while(True):
        try:
            num = input(pmText.optionsC)
            if int(num) not in range(0, len(dirPPA)):
                break
        except:
            otherOption(num,rePrint)
            break
        answer = input(pmText.optionsD) #addmore
        if answer in ['z','Z']:
            removePPA(dirPPA,num)
        elif otherOption(answer,rePrint) or answer not in ['m', 'M']:
            return
        else: #open .list file
            with open(dir + dirPPA[int(num)],'r') as f:
                for i in f:
                    if not i.startswith('#') and not i.startswith('deb-src'): #compare .list to package file
                        listFile = i.split(None) #split by spaces A B C = ['A','B','C']
                        if i.startswith('deb ['): #deb [---] http://---- stable main
                            listFile[:] = listFile[2:] #chop off beginning items
                        else:
                            listFile[:] = listFile[1:] #chop off beggining deb
                        listFile.insert(1, 'dists') #put dists after url end
                        if listFile[0].endswith('/'):
                            listFile[0]= listFile[0][::-1].replace("/", "", 1)[::-1]
                        listFile = '_'.join(listFile).replace("/", "_")[7:] #join items with _.Remove last '/'replace'_'
                        print(str(listFile))
                        return True

def removePPA(E,num):
    if os.geteuid() == 0:
        try:
            if input(pmText.optionsRemoveConfirmA[0] + E[int(num)] + pmText.optionsRemoveConfirmA[1]) in ['y', "Y"]:
                for i in range(0, len(E)):  # checking for .list.save and .list if the alternate is chosen
                    if E[int(num)] + '.save' == E[i] and input(str(E[i]) + pmText.optionsRemoveConfirmB) in ['y', 'Y']:
                        os.remove(dir + E[i])
                        print(pmText.removed + E[i] + color.END)
                    if E[int(num)][:-5] == E[i] and input(str(E[i]) + pmText.optionsRemoveConfirmB) in ['y', 'Y']:
                        os.remove(dir + E[i])
                        print(pmText.removed + E[i] + color.END)
                if not os.path.isdir(dir + E[int(num)]):
                    os.remove(dir + E[int(num)])
                else:
                    os.rmdir(dir + E[int(num)])
                print(pmText.removed + E[int(num)] + color.END)
            else:
                print(pmText.cancelled)
                return
        except ValueError:
            pass
    else:
        print(pmText.noRootB)

def packageInspect():
    global listFile
    p_info=[]
    p_infoAll=[]
    file=[]
    page=75
    pkgListDir='/var/lib/apt/lists/'
    ppaInfo=os.listdir(pkgListDir) #equals all ppa info files
    lim = -1
    def rePrint2():
        for i in range(0,len(ppaInfo)): #loop through all file names
            if listFile in ppaInfo[i] and not ppaInfo[i].endswith('gz'):
                print(color.RED + color.BOLD + str(len(file)) + "\t" + color.END + ppaInfo[i])
                file.append(ppaInfo[i])
    rePrint2()
    answer = input(pmText.optionsE)
    try:
        if int(answer) not in range(0, len(file)):
            return
    except:
        otherOption(answer,rePrint2)
        return
    else:
        with open(pkgListDir + file[int(answer)],'r') as f: #open matching ppa file
            for j in f: #loop through lines in file
                    if j.startswith('Package:'): #if line starts with that
                        p_info.append([])
                        p_infoAll.append([])
                        lim+=1
                    if j.startswith(('Package','Version', 'Maintainer:', 'Section', 'Description',
                                     'Architecture','Pre-Depends','Depends','Homepage')):
                        p_info[lim].append(j[:-1])
                    else:
                        p_infoAll[lim].append(j[:-1])
    while(True):
        if len(p_info) < page:
            page = len(p_info)
        def rePrint3():
            for j in range(0, page):
                for i in range(0, len(p_info[j])):
                    if p_info[j][i].startswith('Package:'):
                        print("\n" + color.BOLD + color.RED + str(j) + "\t" + color.END +
                              color.CYAN + p_info[j][i] + color.END)
                    elif p_info[j][i].startswith('Size'):
                        print(p_info[j][i] + " (in bytes)")
                    else:
                        print(p_info[j][i])
        rePrint3()
        answer = input(pmText.optionsF)
        if answer in ['m','M']:
            page+=75
        elif otherOption(answer,rePrint3) or answer in ['t', 'T']:
            break
        try:
            if int(answer) in range(0,page):
                while(True):
                    answer2 = input(pmText.optionsG)
                    if answer2 in ['i','I']:
                        try:
                            run(["apt-get", "install", p_info[int(answer)][0][9:]]).check_returncode()
                        except CalledProcessError:
                            print(pmText.processFail)
                        except FileNotFoundError:
                            print(pmText.noCommand)
                    elif answer2 in ['o','O','0']:
                        try:
                            for i in range(len(p_infoAll[int(answer)])):
                                print(p_info[int(answer)][i])
                                print(p_infoAll[int(answer)][i])
                        except:
                            pass
                    else:
                        otherOption(answer2,rePrint3)
                        break
        except:
            pass

dir = "/etc/apt/sources.list.d/"
s_Results = []
html=[]
page=0
search=''
if os.geteuid() != 0:
    print(pmText.noRootC)
try:
    if len(sys.argv) == 1:  # if search term is NOT in the script's arguments
        #startSearch()
        home()
    else:
        search = str(sys.argv[1 - len(sys.argv)])  # If search term is in args
        home()
except KeyboardInterrupt: #cleanly exits when Ctrl+C
    print("\n")
    exit()
except NameError:
    print(color.YELLOW + pmText.noPackage + color.END)
    home()
