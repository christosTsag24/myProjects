###################
# Απαραίτητα imports
###################
import operator
import os
import random


#############
# Συναρτήσεις
#############
def get_words_from_text(file_path):
    # Άνοιγμα του αρχείου σε λειτουργία ανάγνωσης
    with open(file_path, 'rt', encoding='utf-8') as f:
        # Διαβάζουμε το αρχείο και το επιστρέφουμε ως συμβολοσειρά
        text = f.read()

        # Αντικαθιστούμε όλα τα whitespaces με απλό κενό
        text = ' '.join(text.split())

        # Μετατροπή όλων των γραμμάτων σε πεζά
        text = text.lower()

        # Απαλοιφή σημείων στίξης και αριθμών
        shmeia_stikshs = '''|—!()-[]{};:\'\’\“\”\"\"\,<>./?@#$%^&*_~'''

        for i in text:
            if i in shmeia_stikshs or i.isdigit():
                # Αντικατάσταση του σημείου στίξης με το τίποτα
                text = text.replace(i, '')

        # Απαλοιφή των περιττών whitespaces - που μπορεί να προκύψουν από την απαλοιφή των σημείων στίξης - με space
        text = ' '.join(text.split())

    # Σπάμε το κείμενο με βάση τα κενά και παίρνουμε πίσω μία λίστα με τις λέξεις του
    words = text.split()

    return words


def get_number_of_words(words):
    # Επιστρέφουμε το πλήθος των στοιχείων (λέξεις) της λίστας
    return len(words)


def get_number_of_unique_words(words):
    # Μετατροπή της λίστας σε σύνολο, ώστε να κρατήσουμε τα μοναδικά στοιχεία της λίστας
    # Επιστρέφουμε το πλήθος των στοιχείων (μοναδικές λέξεις) του συνόλου
    return len(set(words))


def get_5_least_frequent_words(words):
    # Δημιουργία λεξικού το οποίο ως key έχει τις λέξεις και ως value το πλήθος των εμφανίσεων τους
    dict_of_occurrences = {}
    for item in words:
        if item in dict_of_occurrences:
            dict_of_occurrences[item] += 1
        else:
            dict_of_occurrences[item] = 1

    # Ταξινόμηση των κλειδιών του λεξικού με βάση το πλήθος των εμφανίσεών τους κατά αύξουσα σειρά
    sorted_list = sorted(dict_of_occurrences.items(), key=operator.itemgetter(1))  
    # Επιστρέφει λίστα με tuples, η οποία είναι ταξινομημένη (αύξουσα σειρά) με βάση το 
    # δεύτερο στοιχείο του tuple

    # Κρατάμε τα 5 πρώτα (πιο σπάνια) στοιχεία της λίστας
    final_list = sorted_list[:5]

    # Δημιουργούμε την τελική κενή λίστα για τις 5 πιο σπάνιες λέξεις
    least_words = []
    # Προσπέλαση της λίστας με τις πλειάδες
    for key, value in final_list:
        least_words.append(key)

    return least_words


#Συνάρτηση για τη δυναμική δημιουργία του γράφου
def graph_add_node(v1, v2):
    #έλεγχος αν πρόκειται για συνεχόμενες ίδιες λέξεις
    if v1 == v2:
        return
    # Έλεγχος για το αν η κορυφή v1 υπάρχει ήδη
    if v1 in my_graph:
        # έλεγχος για το αν η κορυφή v2 υπάρχει ήδη
        if v2 in my_graph[v1]:
            # εύρεση του index του βάρους του ζεύγους
            w_index = my_graph[v1].index(v2) + 1
            # αύξηση του βάρους κατά 1
            my_graph[v1][w_index] = my_graph[v1][w_index] + 1
        else:
            my_graph[v1].append(v2)
            my_graph[v1].append(1)
    else:
        # προσθήκη των νέων κορυφών
        temp_dict = {
            v1: [v2, 1]
        }
        my_graph.update(temp_dict)

#Α' τρόπος λειτουργίας
#Συνάρτηση εύρεσης κορυφαίων Κ λέξεων
def top_k_words(word, K):
    try:
           #λίστα για τις Κ κορυφαίες λέξεις
           top_words = []
           #λίστα που θα χρησιμοποιήσουμε για τις υποψήφιες λέξεις
           cand = []
           #λίστα βαρών
           weights = []
           #λίστα λέξεων
           lekseis = []
           for v in my_graph[word]:
       	   #Αν είναι ακέραιος αριθμός ενημερώνουμε τη λίστα των βαρών
           #Διαφορετικά ενημερώνουμε τη λίστα των λέξεων
               if isinstance(v,int):
                   weights.append(v)
               else:
                   lekseis.append(v)
           #αρχικοποίηση μετρητή για την εύρεση των κορυφαίων λέξεων
           i = 0
           #Δημιουργία αντιγράφων των λιστών που θα χρησιμοποιήσουμε
           #για την εύρεση των υποψήφιων λέξεων
           weights2 = weights.copy()
           lekseis2 = lekseis.copy() 
           while i < K:
                #εύρεση μέγιστου βάρους
                max_w = max(weights)
                cand = []
                #διαπέραση της λίστας για να βρεθούν όλες οι λέξεις
                #που έχουν βάρος ίσο με το μέγιστο
                for w in weights:
                    if w == max_w:
                        #Αν δεν χρησιμοποιήσουμε τα αντίγραφα στις ακόλουθες 
                        #εντολές διαγραφής, οποιαδήποτε αλλαγή θα τροποποιήσει  
                        #τις αρχικές λίστες και το αποτέλεσμα που θα προκύψει 
                        #θα είναι λανθασμένο
                        #εύρεση θέσης του βάρους
                        w_index = weights2.index(w)
                        #εύρεση θέσης της λέξης με βάρος=w και προσθήκη
                        #αυτής στις υποψήφιες
                        cand.append(lekseis2[w_index])
                        #διαγραφή από τις λίστες-αντίγραφα του παραπάνω βάρους και της
                        #παραπάνω λέξης ώστε να μην ληφθούν υπόψιν στην επόμενη επανάληψη 
                        weights2.pop(w_index)
                        lekseis2.pop(w_index)
                #Αν περισσότερες απο μια λέξεις έχουν το μέγιστο βάρος
                #επέστρεψε μια τυχαία, αλλιώς επέστρεψε αυτή με το μέγιστο βάρος
                if len(cand) > 1:
                    #τυχαία επιλογή λέξης από αυτές με το μέγιστο βάρος
                    toappend = random.choice(cand)
                    #προσθήκη επιλαχούσας στην προς επιστροφή λίστα
                    top_words.append(toappend)
                    #εύρεση του δείκτη της επιλαχούσας στην αρχική λίστα
                    l_index = lekseis.index(toappend)
                    #διαγραφή από τις αρχικές λίστες της επιλαχούσας
                    lekseis.pop(l_index)
                    #και του βάρους που της αντιστοιχεί
                    weights.pop(l_index)   
                else:
                    #ίδια διαδικασία με προηγουμένως, τώρα η επιλαχούσα είναι
                    #το 1ο και μοναδικό στοιχείο της λίστας cand
                    toappend = cand[0]
                    top_words.append(toappend)
                    l_index = lekseis.index(toappend)
                    lekseis.pop(l_index)
                    weights.pop(l_index) 
                #ενημέρωση των αντιγράφων, ώστε να μην περιέχουν την επιλαχούσα
                #και το βάρος της για την επόμενη επανάληψη
                weights2 = weights.copy()
                lekseis2 = lekseis.copy()
                #αύξηση του μετρητή κατά ένα, μέχρι να επιλεγούν Κ λέξεις
                i += 1
     
           print('Οι κορυφαίες',K,'λέξεις είναι:')
           print(top_words)
    except:
        #σε περίπτωση που ζητηθούν περισσότερες λέξεις από όσες υπάρχουν
        #το σφάλμα θα αντιμετωπιστεί εδώ
        print('Δεν υπάρχει άλλη λέξη.')
        #εμφάνιση όσων λέξεων έχουν βρεθεί μέχρι το σφάλμα
        print('Οι κορυφαίες',len(top_words),'λέξεις είναι:')
        print(top_words)


#Β' τρόπος λειτουργίας
#Συνάρτηση επιλογής της πιο πιθανής επόμενης λέξης
#δηλαδή αυτής με το μεγαλύτερο βάρος
def graph_next_vertice(current):
	#Δημιουργούμε μια λίστα η οποία θα περιέχει μόνο τα βάρη
	#της αντίστοιχης κορυφής
    w_list = []
    try:
        for w in my_graph[current]:
    	#Επιλέγουμε μόνο τους ακέραιους αριθμούς
    	#δηλαδή τα βάρη
            if isinstance(w,int):
                w_list.append(w)
    
        #βρίσκουμε το μεγαλύτερο βάρος
        max_w = max(w_list)
        #λίστα υποψήφιων λέξεων
        cand = []
        #δημιουργούμε ένα αντίγραφο από το οποίο θα
        #διαγράφουμε τις υποψήφιες λέξεις
        temp_list = my_graph[current].copy()
        #διαπέραση της λίστας για να βρεθούν όλες οι λέξεις
        #που έχουν βάρος ίσο με το μέγιστο
        for w in temp_list:
            if w == max_w:
                #εύρεση του δείκτη της θέσης του βάρους
                w_index = temp_list.index(w)
                #εύρεση της θέσης της αντίστοιχης λέξης και
                #προσθήκη της λέξης στις υποψήφιες
                cand.append(temp_list[w_index - 1])
                #αφαίρεση του βάρους από τη λίστα
                temp_list.pop(w_index)
        #Αν περισσότερες απο μια λέξεις έχουν το μέγιστο βάρος
        #επέστρεψε μια τυχαία, αλλιώς επέστρεψε αυτή με το μέγιστο βάρος
        if len(cand) > 1:
            return random.choice(cand)
        else:
            #εύρεση της θέσης του μέγιστου βάρους
            max_w_index = my_graph[current].index(max_w)
            #εύρεση της αντίστοιχης λέξης και επιστροφή αυτής
            return my_graph[current][max_w_index - 1]
    except:
        print('Δεν υπάρχει επόμενη λέξη.')
        return ''

def seq_words_higher_probability(word, N):
    #προσθήκη της λέξης του χρήστη στο μήνυμα εξόδου
    output = word
    #αρχικοποίηση μεταβλητής που θα χρησιμοποιηθεί για 
    #την εύρεση του επόμενου κόμβου
    next_vertice = word
    while N > 0:
        #κλήση συνάρτησης επιστροφής επόμενου κόμβου
        next_vertice = graph_next_vertice(next_vertice)
        #αν δεν προέκυψε σφάλμα, τότε προσθέτει την
        #επόμενη λέξη στην έξοδο και μειώνει το μετρητή Ν
        if next_vertice != '':
            output += " " + next_vertice
            N = N - 1 
        else:
            #αν προέκυψε σφάλμα ολοκληρώνει την επανάληψη
            break
    print(output)
    
#Γ' τρόπος λειτουργίας
def graph_next_probability_vertice_buckets(current):
    #Δημιουργούμε μια λίστα με τις κορυφές, μια με τα βάρη, μια για τις
    #πιθανότητες και μια που αντιπροσωπεύει το ζάρι
    v_list = []
    w_list = []
    p_list = []
    r=random.random()
    
    try:
        #Διατρέχουμε τη λίστα γειτνίασης για την κορυφή μας
        for i in range(len(my_graph[current])):
            #στις ζυγές θέσεις είναι τα ονόματα των κορυφών
            if i%2==0:
                v_list.append(my_graph[current][i])
            #στις μονές είναι τα βάρη
            else:
                w_list.append(my_graph[current][i])
    
        # Υπολογισμός πιθανοτήτων για κάθε κορυφή
        total_weight = sum(w_list)
        for w in w_list:
            probability = w/total_weight
            p_list.append(probability)
    
        # Χρήση της συνάρτησης choices
        # return random.choices(v_list, weights=p_list, k=1)[0]
    
        # Για κάθε θέση στη λίστα πιθανοτήτων απομείωσε τον r κατά την πιθανότητα
        position = 0
        for i in range(len(p_list)):
            r=r-p_list[i]
            if r<0:
                position = i
                break
    
        # Επιστρέφουμε την επόμενη κορυφή
        return v_list[position]
    except:
        print('Δεν υπάρχει επόμενη λέξη.')
        return ''
    
def seq_words(word, N):
    #προσθήκη της λέξης του χρήστη στο μήνυμα εξόδου
    output = word
    #αρχικοποίηση μεταβλητής που θα χρησιμοποιηθεί για 
    #την εύρεση του επόμενου κόμβου
    next_vertice = word
    while N > 0:
        #κλήση συνάρτησης επιστροφής επόμενου κόμβου
        next_vertice = graph_next_probability_vertice_buckets(next_vertice)
        if next_vertice != '':
            #αν δεν προέκυψε σφάλμα, τότε προσθέτει την
            #επόμενη λέξη στην έξοδο και μειώνει το μετρητή Ν
            output += " " + next_vertice
            N = N - 1 
        else:
            break
    print(output)
    

#Συνάρτηση για την είσοδο του χρήστη και τον έλεγχο αυτής
def user_input():
    word = input('Πληκτρολογήστε τη λέξη: ').lower()
    #έλεγχος εάν η δοθείσα λέξη δεν ανήκει στο σύνολο
    if word not in allwords:
        word = 'usererror'
        num = 'error'
        print('Η λέξη που δώσατε δεν υπάρχει στο σύνολο.')
        print('##########################\n')
        return word, num
    try:
        #έλεγχος εάν η είσοδος είναι ακέραιος αριθμός
        num = int(input('Δώστε ακέραιο αριθμό: '))
    except:
        print('Ο αριθμός που δώσατε δεν ήταν ακέραιος.')
        print('##########################\n')
        num = 'error'
    else:
        #έλεγχος εάν ο ακέραιος αριθμός είναι μικρότερος του συνολικού αριθμού λέξεων
        if num > len(allwords)-1:
            num = 'error'
            print('Ο αριθμός που δώσατε ξεπερνά το πλήθος των διαθέσιμων λέξεων.')
            print('##########################\n')
    return word, num

#Συνάρτηση εμφάνισης μενού
def menu():
    while(True):
        print('Επιλέξτε λειτουργία πληκτρολογώντας το γράμμα που της αντιστοιχεί:\n')
        print('Α - Επιστροφή Κ πιθανότερων λέξεων\n')
        print('B - Παραγωγή ακολουθίας Ν πιθανότερων λέξεων\n')
        print('C - Παραγωγή ακολουθίας Ν λέξεων\n')
        print('D - Τερματισμός προγράμματος\n')
        func = input('Δώστε την επιλογή σας: ')
        
        if func == 'A':
            word, K = user_input()
            if word!= 'usererror' and K != 'error':
                #functionality A
                print('####### Έναρξη λειτουργίας Α #######\n')
                top_k_words(word, K)
                print('####### Τέλος λειτουργίας #######\n')
                pass
            else:
                continue
        elif func == 'B':
            word, N = user_input()
            if word!= 'usererror' and  N != 'error':
                print('####### Έναρξη λειτουργίας Β #######\n')
                seq_words_higher_probability(word, N-1)
                print('####### Τέλος λειτουργίας #######\n')
            else:
                continue
        elif func == 'C':
            word, N = user_input()
            if word!= 'usererror' and  N != 'error':
                #functionality C
                print('####### Έναρξη λειτουργίας C #######\n')
                seq_words(word, N-1)
                print('####### Τέλος λειτουργίας #######\n')
                pass
            else:
                continue
        elif func == 'D':
            break
        else:
            print("Η επιλογή που δώσατε είναι λανθασμένη.\n")


############################
# Έναρξη κυρίως προγράμματος
############################

# Τρέχων φάκελος
current_dir = os.getcwd()

# Λίστα αρχείων στον τρέχοντα κατάλογο
files_in_directory = os.listdir(current_dir)

# Μετρητής για τα αρχεία
file_count = 0

# Τελική λίστα με τις λέξεις
allwords = []

# Προσπέλαση της λίστας με τα αρχεία στον τρέχοντα φάκελο
for file in files_in_directory:
    # Αν το αρχείο είναι αρχείο κειμένου
    if file.endswith('.txt'):
        # Ανάκτηση των λέξεων από κάθε αρχείο
        w = get_words_from_text(file)
        # Ενημέρωση της τελικής λίστας με τις λέξεις
        allwords.extend(w)
        file_count += 1


print('########## Βασικά στατιστικά στοιχεία ##########')
print('Πλήθος αρχείων που εκπαιδεύτηκε: ', file_count)
print('Συνολικό πλήθος λέξεων που διαβάστηκαν: ', get_number_of_words(allwords))
print('Πλήθος μοναδικών λέξεων που διαβάστηκαν: ', get_number_of_unique_words(allwords))
print('Οι 5 πιο σπάνιες λέξεις: ', get_5_least_frequent_words(allwords))
print('##########################\n')
# Δημιουργία του κενού γράφου
my_graph = {}

#Εισαγωγή των κορυφών και υπολογισμός των βαρών στο γράφο
for i in range(len(allwords)):
    #προσθέτει σειριακά τα ζεύγη λέξεων στο γράφο, 
    #αφήνοντας εκτός την τελευταία λέξη που δεν ακολουθείται από άλλη
    if i != len(allwords) - 1:
        graph_add_node(allwords[i], allwords[i + 1])
    else:
        if allwords[i] in my_graph:
            continue
        else:
            temp_dict = {
                allwords[i]: []
            }
            my_graph.update(temp_dict)

#Κλήση συνάρτησης για την εμφάνιση του μενού λειτουργιών
menu()