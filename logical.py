n=int(input("Enter a number:"))
while True:
  n+=1
  if str(n)==str(n)[::-1]:
    print(n)
    break
  