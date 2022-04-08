# Python Driver Code

def solve(n: int) -> str:
  while (n%2==0):
n=n//2
while (n%7==0):
n=n//7
if (n==1):
  # Your code goes here
  # n is the given input
  return "Special"
else
return "regular"
# The following snippet reads the input in the required format. 
# Just complete the solve function above. 

T = int(input())
for i in range(T):
  test_case = input()
  answer = solve(test_case)
  print(answer)
