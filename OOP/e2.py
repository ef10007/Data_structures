import numpy as np 

def twin_string(s1, s2):
    len1 = len(s1) 
    len2 = len(s2) 
        
    if (len1 != len2) : 
        return False
  
    previous = -1
    current = -1
        
    count = 0 
    i = 0
    while i < len1 : 
        if (s1[i] != s2[i] ) : 
            count = count + 1

            if (count > 2) : 
                return False
 
            previous = current
            current = i 
        i += 1
         
    return (count == 2 and s1[previous] == s2[current] and s1[current] == s2[previous]) 


def mark_scores(test1, test2):
    distinctions = 0
    passes = 0
    failures = 0

    total = np.sum([int(test1), int(test2)])
    print(f'The total score of the first student is {total}.')

    while total <= 100:

        print(" Next student (first test):")
        test1 = input()
        print("(second test):")
        test2 = input()
        total = np.sum([int(test1), int(test2)])

        if total <= 100:
            print(f'The total score of this student is {total}.')

        if total >= 70:
            distinctions += 1
        elif total >= 50 and total < 70:
            passes += 1
        elif total < 50:
            failures +=1
        else:
            distinctions -= 1
            break

    print(f'Finishing marking scores program. \n You have {distinctions} distinctions, {passes} passes and {failures} failures.')
    

if __name__ == "__main__":
    first_student1 = 31
    first_student2 = 41
    mark_scores(first_student1, first_student2)




