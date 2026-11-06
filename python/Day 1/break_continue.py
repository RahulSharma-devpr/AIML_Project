for n in range(1, 10):
    if n == 3:
        continue      # skip 3
    if n == 7:
        break         # stop the loop at 7

    if n== 5:
        print("5 is skipped")
        continue
    print(n)

# else runs only if the loop was NOT stopped by break
for n in range(2, 7):#2 is inclusive and 7 is exclusive
    if n == 6:
        print("break")
        break
else:
    print("No break happened")