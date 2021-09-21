# Python for Data Analysis 101
## Homework
### Instructor: Evelyn J. Boettcher, DiDacTex, LLC
### Week 2, Lecture 1, Problem 3
### Student: Capt Stephen Stumpf
### Using open , create a new file that records user input (min 1, max 4 inputs) and then opens
### that file and APPENDS the following “Received User Input”

f = open("inputbuffer.txt", 'w')
myinput = [0, 0, 0, 'a']
for i in range(4):
    try:
        myinput[i] = input("Enter #" + str(i+1) + " of 4 inputs (or Ctrl+C to stop): ")
    except KeyboardInterrupt:
        break
    f.write(myinput[i] + "\n")


f.close()
f = open("inputbuffer.txt", 'a')
f.write("Received User Input\n")
f.close()

print("\nDone")
