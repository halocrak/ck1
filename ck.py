from colorama import init,Fore
import requests, multiprocessing
import time

class Start:
    run = True
    a = []
    b = []
    SPACING = 23
    start_time = time.time()
    URL = f"https://www.instagram.com/"
    def link(self):
        start_time = time.time()
        print("\033[1;33;40m ","""
                          CHECKER BY XDARKLE
                  instagram: @0fve    snapchat: znecv
                              GOOD LUCK
        """)
        # self.file_name = input("Eneter your list name/path: ")
        start = time.perf_counter()
        with open("list.txt",'r') as f:
            try:
                while True:
                    self.lines = f.readline().strip()
                    self.req = requests.get(f"https://www.instagram.com/{self.lines}")
                    if self.lines == '':
                        f.strip('\n')
                        f.close()
                    if self.req.status_code == 200:
                        print('\033[1;31;40m',' '*self.SPACING, self.lines , '    not avalible')
                        self.b.append(self.lines)
                    elif 404:
                        print(Fore.GREEN, ' '*self.SPACING ,self.lines,'    is Availble')
                        self.a.append(self.lines)
                    else:
                        print('\033[1;36;40m',' '*self.SPACING, self.lines , '    unknown')
            except Exception as e:
                print(Fore.CYAN,  "\n", ' '*12,"ALL USER HAVE BEEN CHECKED SUCCESSFULY \n",' '*18 ,"AND SAVED TO AVALIBLE.TXT",Fore.RESET)
                finish = time.perf_counter()
            except KeyboardInterrupt:
                print('\033[1;31;40m',' '*24,len(self.b),"users unavalible",Fore.RESET)
                print(Fore.GREEN, ' '*25,len(self.a),"users avalible",Fore.RESET)
                print('\033[1;31;40m',' '*27," Aborted.",Fore.RESET)
        self.avalible()
        finish = time.perf_counter()
        print(' '*25,'\033[95m','Finished in ' + str(round(finish-start, 2)))

    def avalible(self):
        with open("avalible.txt",'w') as f:
            for user in self.a:
                f.write("%s\n" % user)
                
checker = Start()
checker.link()
