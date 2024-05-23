"""
A number of students are members of a club that travels annually to exotic locations. Their destinations
in the past have included Indianapolis, Phoenix, Nashville, Philadelphia, San Jose, and Atlanta. This
spring they are planning a trip to Eindhoven.
The group agrees in advance to share expenses equally, but it is not practical to have them share
every expense as it occurs. So individuals in the group pay for particular things, like meals, hotels, taxi
rides, plane tickets, etc. After the trip, each student’s expenses are tallied and money is exchanged so
that the net cost to each is the same, to within one cent. In the past, this money exchange has been
tedious and time consuming. Your job is to compute, from a list of expenses, the minimum amount of
money that must change hands in order to equalize (within a cent) all the students’ costs.
Input
Standard input will contain the information for several trips. The information for each trip consists of
a line containing a positive integer, n, the number of students on the trip, followed by n lines of input,
each containing the amount, in dollars and cents, spent by a student. There are no more than 1000
students and no student spent more than $10,000.00. A single line containing 0 follows the information
for the last trip.
Output
For each trip, output a line stating the total amount of money, in dollars and cents, that must be
exchanged to equalize the students’ costs.
Sample Input
3
10.00
20.00
30.00
4
15.00
15.01
3.00
3.01
0
Sample Output
$10.00
$11.99

"""

def solve(arr):
    avg = sum(arr)/len(arr)
    pos_diff, neg_diff = 0.0, 0.0
    for num in arr:
        val = int((num - avg) * 100.0) / 100.0
        if val < 0:
            neg_diff += val
        else:
            pos_diff += val
    neg_diff *= -1
    res = neg_diff if neg_diff > pos_diff else pos_diff
    return '${0:.2f}'.format(res)

if __name__ == '__main__':
    while True:
        try:
            N = int(input())
            if N == 0:
                break
            arr = []
            for _ in range(N):
                arr.append(float(input()))
            print(solve(arr))
        except EOFError:
            break

