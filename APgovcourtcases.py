'''
Title: This is for my school project, just a quick way to find the info
Author: Riley Carpenter
'''
import os
import sys
global info
info = "Not done"
global case
def clear():
    if sys.platform == "linux" or sys.platform == "posix":
        os.system("clear")
    else:
        os.system("cls")
def wait():
    input()
    clear()
def infomake():
    global case
    global info
    print("What do you want to find out about",case)
    print(""""Do you want to know
    Years and Justice
    Details
    Decision
    Vote Totals
    Why we care
    Constitutional Provisions?
    If you want a new case type Done ")"""
    info = input("What do you want to know? ")
    clear()



def marburyvmadison():
    global info
    global case
    info = ""
    while info != "Done":
        infomake()
        input()
        clear()
        if info == "Years and Justice":
            print("It was argued Feb 11 1803 and Decided Feb 24 1803 in the Marshall court")
            input()
            clear()
        elif info == "Details":
            print("John Adams created a bunch of new offices to annoy Thomas Jefferson and this one guy named Marbury was promised a job, James Madison, Thomas Jefferson's guy, didn't give Marbury the documents needed for the job so Marbury sued Madison over it. The big question asked by this case was whether or not the Supreme Court had a right to order the delievery of the commisions.")
            input()
            clear()
        elif info == "Decision":
            print("They said that while Madison's refusal WAS illegal they couldn't demand Madison to give Marbury the papers because it would go against what was written in the Constitution about the Supreme Court")
            input()
            clear()
        elif info == "Vote Totals":
            print("It was a unanimous decision")
            input()
            clear()
        elif info == "Why we care":
            print("This established judicial review which is the system that the supreme court uses when deciding whether or not something is constitutional")
            wait()
        elif info == "Constitutional Provisions":
            print("Section 13 of the judiciary act of 1789 was used as it conflicted with the article of the constitution which established the supreme court Article III Section 2")
            wait()
        else:
            print("That's not an option IDIOT")




def mccullochvmaryland():
    global info
    global case
    info = ""
    while info != "Done":
        infomake()
        if info == "Years and Justice":
            print("Started arguing on Feb 22 2019 and was Decided March 6 1819. In the Marshall Court")
            wait()
        elif info == "Details":
            print("So the second national bank was chartered (thanks hamilton) and Maryland decided to put taxes on the bank and the cashier of the bank in Baltimore Mr.McCulloch refused to pay the taxes so they took it to court")
            wait()
        elif info == "Vote Totals":
            print("Unanimous Decision")
            wait()
        elif info == "Decision":
            print("Maryland can't tax the bank and congress could create the bank")
            wait()
        elif info == "Why we care":
            print("Loose Constructionism was made the law of the land because Marshall said Congress had powers outside of the constitution")
            wait()
        elif info == "Constitutional Provisions":
            print("Used the Necessary and Proper Clause of the constitution")
            wait()
        else:
            print("That's not a useable Command")




def gibbonsvogden():
    global info
    info = ""
    while info != "Done":
        global case
        infomake()
        if info == "Years and Justice":
            print("It was argued Feb 4 - 9 1824 and was decided March 2 1824 in the Marshall Court")
            wait()
        elif info == "Details":
            print("So these two guys Gibbons and Ogden formed a partner ship for boats and quickly had a pseudo monopoly but it fell apart because Gibbons operated a different steam boat business. Ogden filed a suit against Gibbons and didn't get far because Congress controlls interstate commerce")
            wait()
        elif info == "Decision":
            print("Yep it is decided by congress because it goes between two states even though it is a boat service.")
            wait()
        elif info == "Vote Totals":
            print("Unanimous decision")
            wait()
        elif info == "Why we care":
            print("Reestablished that congress is always over the states when it comes to interstate commerce")
            wait()
        elif info == "Constitutional Provisions":
            print("Constitution Supremecy Clause")
            wait()
        else:
            print("That's not a valid answer")
            wait()
    infomake()





def dredscottvsanford():
    global info
    info = ""
    while info != "Done":
        global case
        infomake()
        if info == "Years and Justice":
            print("It started arguing February 11 1856 and decided March 6 1857 by the Taney Court")
            wait()
        elif info == "Details":
            print("Dred Scott was a slave and he went to a free state and after he left he sued his master to let him free")
            wait()
        elif info == "Decision":
            print("Dred Scott is not an american citizen and therefore could not have sued his former master also missouri comprimise of 1820 is unconstitutional because freed slaves shouldn't be freed just because they went to a new slave")
            wait()
        elif info == "Vote Totals":
            print("7-2 Decision against Dredd Scott")
            wait()
        elif info == "Why we care":
            print("This case furthered the united states towards the civil war and also reversed the line that seperated slave states to free states")
            wait()
        elif info == "Constitutional Provisions":
            print("Slaves are property under the fifth amendment so the Missouri Comprimise is unconstitutional")
            wait()
        else:
            print("That doesn't work")






def expartemilligan():
    global info
    info = ""
    while info != "Done":
        global case
        infomake()
        if info == "Years and Justice":
            print("This case was argued March 5 1866 and was decided April 3 1866 in the Chase court")
            wait()
        elif info == "Details":
            print("This guy named Milligan was sentenced to death by a military council during the civil war and claimed habeas corpus so he wouldn't die")
            wait()
        elif info == "Decision":
            print("Civilians cannot be tried by a military court therefore milligan will be set free")
            wait()
        elif info == "Vote Totals":
            print("It was a unanimous decision in favor of Milligan")
            wait()
        elif info == "Why we care?":
            print("Limited the power of the executive branch during the civil war and submitted that what abraham lincoln was doing was illegal and changed the way the north would approach reconstruction")
            wait()
        elif info == "Constitutional Provisions":
            print("The sixth amendment of the United States was the provision used")
            wait()
        else:
            print("That's not a command that's allowed")







def plessyvferguson():
    global info
    global case
    info = ""
    while info != "Done":
        infomake()
        if info == "Years and Justice":
            print("It was argued April 13 1896 and was decided may 18 1896")
            wait()
        elif info == "Details":
            print("Lousiana enacted a law that created segregated cars for white people and black people, Plessy a 7/8ths white person tried to sit in the whites only car and he was asked to move to the blacks only car, he then sued when he refused")
            wait()
        elif info == "Decision":
            print("Seperate but equal is constitutional if the facilities are completely equal")
            wait()
        elif info == "Vote Totals":
            print("7-1 for Ferguson against plessy")
            wait()
        elif info == "Why we care":
            print("This started segregation in the south by upholding it in the supreme court")
            wait()
        elif info == "Constitutional Provisions":
            print("The fourteenth amendment as it never explicitly said they had to be the same facilities")
            wait()
        else:
            print("That's not allowed")
            wait()







def schenkvus():
    global info
    info = ""
    while info != "Done":
        infomake()
        if info == "Years and Justice":
            print("This was argued Jan 9 and decided March 3 1919 under the White Court")
            wait()
        elif info == "Details":
            print("These two socialists argued that the draft violated the thirteenth amendment and passed out pamphlets saying that it did and then were arrested because of the espionage act, the gov said that they were trying to undermine the military and stop the draft")
            wait()
        elif info == "Decision":
            print("The espionage act does not violate the first amendment because of the fact that america is in a war at the current moment")
            wait()
        elif info == "Vote Totals":
            print("Unanimous decision for the united states")
            wait()
        elif info == "Why we care":
            print("It allowed the US to create laws limiting free speech based on the situation the country was facing")
            wait()
        elif info == "Constitutional Provisions":
            print("The first amendment")
            wait()
        else:
            print("You can't do that")
            wait()








def korematsuvus():
    global info
    info = ""
    while info != "Done":
        infomake()
        if info == "Years and Justice":
            print("Oct 11 1944 was when it was aruged and it was decided dec 18 1944 in the Stone Court")
            wait()
        elif info == "Details":
            print("THe united states was taking away japanese people and putting them in internment camps because of anti-japanese beliefs at the time and this guy Korematsu didn't go and then was charged")
            wait()
        elif info == "Decision":
            print("The need to protect against espionage is greater than an individuals rights so Korematsu was arrested")
            wait()
        elif info == "Vote Totals":
            print("6-3 for United States")
            wait()
        elif info == "Why we care":
            print("Upheld legality of the internment of japanese americans")
            wait()
        elif info == "Constitutional Provisions":
            print("The fifth amendment")
            wait()
        else:
            print("You can't do that")
            wait()







def brownvboardofeducation():
    global info
    info = ""
    while info != "Done":
        infomake()
        if info == "Years and Justice":
            print("Argued Dec 9 1952 and rearuged Dec 9 1953 and finally decided May 17 1954 in the Warren Court")
            wait()
        elif info == "Details":
            print("In 4 seperate cases African American children were being denied admittance to certain schools because of race and so they argued that it violated the Equal Protection Clause of the fourteenth amendment")
            wait()
        elif info == "Decision":
            print("Seperate but equal is never equal")
            wait()
        elif info == "Vote Totals":
            print("Unanimaous decision for Brown against the Board of education")
            wait()
        elif info == "Why we care":
            print("Overturned Plessy V Ferguson and finally almost ended segregation")
            wait()
        elif info == "Constitutional Provisions":
            print("Fourteenth Amendment")
            wait()
        else:
            print("That's not allowed")
            wait()







def plannedparenthoodvcasey():
    global info
    info = ""
    while info != "Done":
        infomake()
        if info == "Years and Justice":
            print("Argued April 22 1992 and decided June 29 1992 in the Rehnquist Court")
            wait()
        elif info == "Details":
            print("Pennsylvania legislature changed their laws so that it was harder to get an abortion and Clinics and physicians disagreed with the law")
            wait()
        elif info == "Decision":
            print("Any law that would place an undue burden on women to get an abortion is unconstitutional and this in turn upheld roe v wade")
            wait()
        elif info == "Vote Totals":
            print("5-4 decision for planned parenthood")
            wait()
        elif info == "Why we care":
            print("This upheld roe v wade and made it easier for women to get an abortion")
            wait()
        elif info == "Constitutional Provisions":
            print("Roe v Wade was used")
            wait()
        else:
            print("That's not allowed")
            wait()







def webstervreproductivehealth():
    global info
    info = ""
    while info != "Done":
        infomake()
        if info == "Years and Justice":
            print("This was argued April 26 1989 and decided July 3 1989 in the Rehnquist Court")
            wait()
        elif info == "Details":
            print("Missouri was just being all kind of restrictive with abortions but mainly they said that life begins at conception and women could only get abortions if it was life threatening")
            wait()
        elif info == "Decision":
            print("None of the argued parts of the bill were unconstitional")
            wait()
        elif info == "Vote Totals":
            print("5-4 for Webster")
            wait()
        elif info == "Why we care":
            print("Allowed states to further restrict a woman's right to get an abortion")
            wait()
        elif info == "Constitutional Provisions":
            print("Fourteenth amendment")
            wait()
        else:
            print("That's not allowed")
            wait()







def gideonvwainright():
    global info
    info = ""
    while info != "Done":
        infomake()
        if info == "Years and Justice":
            print("Aruged Jan 15 1963 and decided March 18 1963 in the warren court")
            wait()
        elif info == "Details":
            print("This guy requested to have cousel in the court but florida said no so he represented himself and he said in habeas corpus that this denied his right to cousel")
            wait()
        elif info == "Decision":
            print("States are required to give counsel to those who need one no matter if the court is state or federal")
            wait()
        elif info == "Vote Totals":
            print("Unanimous Decision")
            wait()
        elif info == "Why we care":
            print("This established the right to counsel in all states and federal courts therefore it was a very important decision. It also implied that the states have to give everyone equal rights throught the fourteenth amendment")
        elif info == "Constitutional Provisions":
            print("The fourteenth amendment for the second part and the sixth amendment for the first part")
        else:
            print("That's not allowed")
            wait()







def mirandavarizona():
    global info
    info = ""
    while info != "Done":
        infomake()
        if info == "Years and Justice":
            print("Argued first february 28 1966 and decided June 13 1966 in the warren court ")
            wait()
        elif info == "Details":
            print("Many cases compiled this but the main one was this guy named miranda who was questioned for involvement in a rape case and was tortured before giving his written confession, this was all before he was read his fifth amendment rights")
            wait()
        elif info == "Decision":
            print("The fifth amendment holds in all situations so an interrogation has to occur with certain responsibilities")
            wait()
        elif info == "Vote Totals":
            print("5-4 majority Miranda")
            wait()
        elif info == "Why we care":
            print("This established the procedure police officers must go through in order to interrogate you")
            wait()
        elif info == "Constitutional Provisions":
            print("Fifth amendment")
            wait()







def engelvvitale():
    global info
    info = ""

    while info != "Done":
        infomake()
        if info == "Years and Justice":
            print("It was argued April 3 1962 and decided June 25 1962 in the Warren Court")
            wait()
        elif info == "Details":
            print("This school was reading a nondenominational kinda bland prayer everyday before school and so the supreme court has to decide whether it breaks the freedom of religion act")
            wait()
        elif info == "Decision":
            print("It's unconstitutional")
            wait()
        elif info == "Vote Totals":
            print("6-1 for Engel")
            wait()
        elif info == "Why we care":
            print("This case established the unconstitutionality of forced religion in schools")
            wait()
        elif info == "Constitutional Provisions":
            print("The first amendment")
            wait()
        else:
            print("That isn't allowed")
            wait()







def roevwade():
    global info
    info = ""
    while info != "Done":
        infomake()
        if info == "Years and Justice":
            print("Argued Dec 13 1971 and Decided Jan 22 1973, it was decided in the Burger Court")
        elif info == "Details":
            print("This person named roe wanted an abortion but because texas law said they could only get one if it was life threatening they couldn't so they sued texas")
            wait()
        elif info == "Decision":
            print("A right to an abortion falls under the right of privacy in the fourteenth amendment")
            wait()
        elif info == "Vote Totals":
            print("7-2 decision for Jane Roe")
            wait()
        elif info == "Why we care":
            print("This is still argued about today whether or not Roe v Wade should be overturned so besides affecting the political climate for years to come it also established the basis for a constitutional argument for a women's right to privacy")
            wait()
        elif info == "Constitutional Provisons":
            print("Fourteenth Amendment")
            wait()
        elif info == "Done":
            print("Good luck on the next case")
            wait()
        else:
            print("That's not allowed")
            wait()







def usvrichardnixon():
    global info
    info = ""
    while info != "Done":
        infomake()
        if info == "Years and Justice":
            print("Argued July 8 1974 and decided July 24 1974 in the Burger Court")
            wait()
        elif info == "Details":
            print("Nixon was subpoenaed to release tapes and claimed executive priveledge so the supreme court had to decide if that was a thing")
            wait()
        elif info == "Decision":
            print("There was nothing in the constitution that said he could do that so he had to give up the tapes")
            wait()
        elif info == "Vote Totals":
            print("Unanimous Decision against Nixon")
            wait()
        elif info == "Why we care":
            print("This case was the cause of nixon's resignation and also established the fact that executive priveledge isn't real")
            wait()
        elif info == "Constitutional Provisions":
            print("The privelege in areas of military or diplomatic affairs granted by the constitution")
            wait()
        elif info == "Done":
            print("Good luck")
            wait()
        else:
            print("That's not allowed")
            wait()







def bakkevucregents():
    global info
    info = ""
    while info != "Done":
        infomake()
        if info == "Years and Justice":
            print("October 12 1977 was when it was first argued and it was decided June 26 1978 in the Burger Court")
            wait()
        elif info == "Details":
            print("This guy was denied access to a college because they were reserving the spots for a person of colour and he sued because he was being 'discriminated' against")
            wait()
        elif info == "Decision":
            print("Race can be used only with other qualifiers not exclusively by itself")
            wait()
        elif info == "Vote Totals":
            print("8-1 decision for Bakke")
            wait()
        elif info == "Why we care":
            print("This affects all college admissions to this day")
            wait()
        elif info == "Constitutional Provisions":
            print("The fourteenth amendment")
            wait()







def bakervcarr():
    global info
    info = ""
    while info != "Done":
        infomake()
        if info == "Years and Justice":
            print("Argued April 19th 1961 and decided March 26 1962 in the undecided court")
            wait()
        elif info == "Details":
            print("A tennessee law about the proportion of seats in the general assembly was ignored")
            wait()
        elif info == "Decision":
            print("The supreme court can interfere in state matters such as these")
            wait()
        elif info == "Vote Totals":
            print("6-2 for Baker")
            wait()
        elif info == "Why we care":
            print("This reestablished that the courts have power over the state governments")
            wait()
        elif info == "Constitutional Provisions":
            print("Fourteenth Amendment")
            wait()
        elif info == "Done":
            print("Bye!")
            wait()
        else:
            print("That's not allowed")
            wait()







def swannvcharlottemecklengerg():
    global info
    while info != "Done":
        infomake()
        if info == "Years and Justice":
            print("It was decided in the burger court and argued Oct 12 1970 and decided 4/20/71")
            wait()
        elif info == "Details":
            print("Schools weren't actually desegregating after Brown v Board and some schools even shut down so this was a court case deciding if a school with 99 percent black population needed to have forced integration")
            wait()
        elif info == "Decision":
            print("The court held that they needed to reintegrate immediately")
            wait()
        elif info == "Vote Totals":
            print("Unanimous Decison")
            wait()
        elif info == "Why we care":
            print("This again reinforced the decision in brown v board")
            wait()
        elif info == "Constitutional Provisions":
            print("Fourteenth Amendment")
            wait()
        elif info == "Done":
            print("Goodbye!")
            wait()
        else:
            print("That's not allowed")
            wait()







while 1 == 1:
    print("Type what court case you want to observe or type CASES to see what cases you can observe")
    case = input("What case? ")
    if case == "CASES":
        print("""
    CASE NUMBER:            CASES:
    M1                Marbury v. Madison
    M2                McCulloch v Maryland
    G1                Gibbons v Ogden
    DS1               Dred Scott v Sanford
    EPM1              Ex parte Milligan
    PF1               Plessy v Ferguson
    SUS1              Schenck v US
    KUS1              Korematsu v US
    BVB2              Brown v Board of Education
    PP1               Planned Parenthood v Casey
    W1                Webster v Reproductive Health
    GVW1              Gideon v Wainright
    MVA1              Miranda v Arizona
    EVV1              Engel v Vitale
    RVW1              Roe v Wade
    USVRN1            US v Richard Nixon
    BVUC1             Bakke v UC Regents
    BVC1              Baker v Carr
    SVCM1             Swann v Charlotte-Mecklenberg
        """)
    elif case == "Marbury v Madison" or case == "M1":
        case = "Marbury v Madison"
        clear()
        marburyvmadison()
    elif case == "Engel v Vitale" or case == "EVV1":
        case = "Engel v Vitale"
        clear()
        engelvvitale()
    elif case == "McCulloch v Maryland" or case == "M2":
        clear()
        case = "McCulloch v Maryland"
        mccullochvmaryland()
    elif case == "Gibbons v Ogden" or case == "G1":
        clear()
        case = "Gibbons vs Ogden"
        gibbonsvogden()
    elif case == "Dred Scott v Sanford" or case == "DS1":
        clear()
        case = "Dred Scott v Sanford"
        dredscottvsanford()
    elif case == "Ex Parte Milligan" or case == "EPM1":
        clear()
        case = "Ex Parte Milligan"
        expartemilligan()
    elif case == "Plessy v Ferguson" or case == "PF1":
        clear()
        case = "Plessy v Ferguson"
        plessyvferguson()
    elif case == "Schenck v US" or case == "SUS1":
        clear()
        case = "Schenck v US"
        schenkvus()
    elif case == "Korematsu v US" or case == "KUS1":
        clear()
        case = "Korematsu v US"
        korematsuvus()
    elif case == "Brown v Board of Education" or case == "BVB2":
        clear()
        case = "Brown v Board of Education 2"
        brownvboardofeducation()
    elif case == "Planned Parenthood v Casey" or case == "PP1":
        clear()
        case = "Planned Parenthood v Casey"
        plannedparenthoodvcasey()
    elif case == "Webster v Reproductive Health" or case == "W1":
        clear()
        case = "Webster v Reproductive Health"
        webstervreproductivehealth()
    elif case == "Gideon v Wainright" or case == "GVW1":
        clear()
        case = "Gideon v Wainright"
        gideonvwainright()
    elif case == "Miranda v Arizona" or case == "MVA1":
        clear()
        case = "Miranda v Arizona"
        mirandavarizona()
    elif case == "Roe v Wade" or case == "RVW1":
        clear()
        case = "Roe v Wade"
        roevwade()
    elif case == "US v Richard Nixon" or case == "USVRN1":
        clear()
        case = "US v Richard Nixon"
        usvrichardnixon()
    elif case == "Bakke v UC Regents" or case == "BVUC1":
        clear()
        case = "Bakke v UC Regents"
        bakkevucregents()
    elif case == "Baker v Carr" or case == "BVC1":
        clear()
        case = "Baker v Carr"
        bakervcarr()
    elif case == "Swann v Charlotte-Mecklenberg" or case == "SVCM1":
        clear()
        case = "Swann v Charlotte-Mecklenberg"
        swannvcharlottemecklengerg()
    else:
        clear()
        print("That's not a valid case name, check spelling")
