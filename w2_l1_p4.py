# Python for Data Analysis 101
## Homework
### Instructor: Evelyn J. Boettcher, DiDacTex, LLC
### Week 2, Lecture 1, Problem 3
### Student: Capt Stephen Stumpf
### Using open , create a new file that records user input (min 1, max 4 inputs) and then opens
### that file and APPENDS the following “Received User Input”

myinput = [0, 0, 0, 0]
with open("inputbuffer.txt", 'w') as f:
    for i in range(len(myinput)):
        try:
            myinput[i] = input("Enter #" + str(i+1) + " of " + str(len(myinput)) + " inputs (Ctrl+C to stop): ")
        except KeyboardInterrupt:
            break
        f.write(myinput[i] + "\n")
    f.close()
    
with open("inputbuffer.txt", 'a') as f:
    f.write("Received User Input\n")
    f.close()

print("\nDone")
