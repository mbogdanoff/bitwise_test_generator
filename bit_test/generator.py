import random
def test_q_1_2(x):
        orig = random.choice([41120, 45232, 49344, 53456, 57568,61680])
        insert = random.choice([10, 11, 12 ,13 ,14 ,15])
        number = random.choice([5,6,7,8])
        a = orig|(insert<<number)
 
        z = open(str(x)+"_test.txt","a")
        z.write(('a = ?      ..........\n'))
        z.write(''.join(('int orig = ',("0x%X")%orig,"\n")))
        z.write(''.join(('int insert = ',("0x000%X")%insert,"\n")))
        z.write(''.join(('int a = orig|(insert << ',str(number),")\n\n")))
 
        z = open(str(x)+"_test_answers.txt","a")
        z.write(''.join(('a = ?      ',("0x%X")%a,'\n')))
        z.write(''.join(('int orig = ',("0x%X")%orig,"\n")))
        z.write(''.join(('int insert = ',("0x000%X")%insert,"\n")))
        z.write(''.join(('int a = orig|(insert << ',str(number),")\n\n")))
 
print 'Enter the amount of tests you require...'
n = raw_input()
n = int(n)
for x in xrange(1,n+1):
        test_q_1_2(x)