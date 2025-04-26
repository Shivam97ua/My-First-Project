# # Task 1: Read a File and Handle Errors
try:
    file1=open('sample.txt', 'r')
    reading_file1=file1.readline()
    print("Line 1:",reading_file1)
    reading_file1=file1.readline()
    print("Line 2:",reading_file1)
    file1.close()
except FileNotFoundError:
    print("Error : The File 'sample.txt' was not found.")




# Task 2: Write and Append Data to a File
a=input("Enter text to write to the file:")
b=input("Enter text to write to the file:")
file=open('output.txt ','w')
writing_file=file.write(a + '\n')
print('Data successfully written to output.txt')
file.close()

file=open('output.txt','a')
appending_file=file.write(b)
print('Data Successfully appended.')
file.close()

file=open('output.txt','r')
reading_file=file.read()
print('Final Content of output.txt :')
print(reading_file)
file.close()