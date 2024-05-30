#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb

# Import regular expression, string and system module
import re, string  
import sys

cgitb.enable()

# Retrieve the input sequence from the form
form = cgi.FieldStorage()
inSeq = form.getvalue('sequence')

print "Content-type: text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<link rel='stylesheet' href='/sqf7007/ju/Style.css'>"
print "<title>Palindromic Sequence Results</title>"
print "</head>"
print "<body>"

# inSeq.upper() convert the input to capital
inSeq_cap = inSeq.upper()

# Define a function "seqcheck" to check whether the sequence input by user is DNA (in uppercase)
def seqcheck(inSeq_cap):
	for char in inSeq_cap: 
		valid_seq = ['A', 'C', 'G', 'T'] 
		if char not in valid_seq:  
            		print("<div align=center><p><br><br><br><b>Invalid sequence input!&nbspPlease enter a valid input.</b></p>")
			print("<button type=back id='back' name='back' onclick=window.location.href='/./test-cgi/sqf7007/jane/Project2/pal.cgi';>Back to Query Page</button></div>")
			sys.exit()		
	return True
	
# Function to calculate reverse complement
def rev_complement(inSeq_cap):
    	script = string.maketrans('ACGT', 'TGCA')  
    	complement = inSeq_cap.translate(script)  
    	revComp = complement[::-1]  
	return revComp

# Store the return values of rev_complement(inSeq_cap) variable named revComp
revComp = rev_complement(inSeq_cap)


# Main function
def main():
    # inSeq.upper() converts the input to capital
    inSeq_cap = inSeq.upper()

    # to check if the input sequence is a DNA sequence or not
    seqcheck(inSeq_cap)

    # Define the maximum number of characters per line
    max_chars_per_line = 80

    # Split the input sequence into lines with a maximum number of characters
    lines = [inSeq_cap[i:i+max_chars_per_line] for i in range(0, len(inSeq_cap), max_chars_per_line)]
    # Split the reverse complement into lines with a maximum number of characters
    liness = [revComp[i:i+max_chars_per_line] for i in range(0, len(revComp), max_chars_per_line)]

    spacer_count = 0
    non_spacer_count = 0
    print("<html>")
    print("<head>")
    print("<title>Palindromic Sequence Results</title>")
    print("<link rel='stylesheet' href='/sqf7007/ju/Style.css'>")
    print("</head>")
    print("<body>")
    print("<h1>Palindromic Sequence Results</h1>")
    print("<h3>Input Sequence:</h3>")
    print("<pre>")

    # Print each line of the input sequence
    for line in lines:
        print(line)
    print("</pre>")
    print("<h3>Reverse Complement:</h3>")
    print("<pre>")

    # Print each line of the reverse complement
    for line in liness:
        print(line)
    print("</pre>")

    # Print the length of input sequence that has entered in the textarea inside the form   
    print("<h3>Length of DNA Sequence entered is:</h3> {}<br><br>".format(len(inSeq_cap)))
    print("<h2><u>Palindromic Sequences:</u></h2>")

    # below for loop are to extract non-spacer palindrome
    i = 0  # initialization
    count = 1
    print("<table>")
    print("<tr>")
    print("    <th>No.</th>")
    print("    <th>From</th>")
    print("    <th>To</th>")
    print("    <th>Length</th>")
    print("    <th>Type</th>")
    print("    <th>Palindromes</th>")
    print("</tr>")
    for n in inSeq_cap:
        paliSeq = ""  # to store palindromes
        k = i

        # this while loop is intended to extract only sequences that are longer than 4 bp
        while k < len(inSeq):
            paliSeq = paliSeq + inSeq_cap[k]

            # condition to select only sequences longer than 4 bp
            if len(paliSeq) >= 4:
                if rev_complement(paliSeq) == paliSeq:  # if the sequence is equal to its reverse complement, it is a palindrome
                    print("<tr>")
                    print("    <td>{}</td>".format(count))
                    print("    <td>{}</td>".format(i + 1))
                    print("    <td>{}</td>".format(k + 1))
                    print("    <td>{}</td>".format(k - i + 1))
                    print("    <td>NON-SPACER</td>")
                    print("    <td>{}</td>".format(paliSeq))
                    print("</tr>")
                    count += 1
                    non_spacer_count += 1
            k = k + 1
        i = i + 1

    # below for loop are to extract spacer palindrome
    i = 0  # initialization

    for n in inSeq_cap:
        paliSeq = ""  # to store palindromes
        k = i

        # this while loop is intended to extract only sequences that are longer than 5 bp
        while k < len(inSeq):
            paliSeq = paliSeq + inSeq_cap[k]

            # condition to select only sequences longer than or equal to 5 bp, as it is the shortest possible spacer palindrome
            # the spacer region is at most 26bp length
            if 30 >= len(paliSeq) >= 5:
                # condition to select spacer palindrome, as spacer palindrome won't have their sequence exactly the same due to the presence of spacer in the middle
                if paliSeq != rev_complement(paliSeq):
                    # condition to filter out only palindrome sequences that have the same left and right residue
                    if (paliSeq[0:2] == rev_complement(paliSeq)[0:2]) and (paliSeq[-2:-1] == rev_complement(paliSeq)[-2:-1]):
                        index = 0
                        index2 = 0
                        countSP = 0
                        left = ""  # temporary storage for the first half of the palindrome sequence
                        right = ""  # temporary storage for the second half of the palindrome sequence

                        # this for loop is to extract the palindrome sequence before the spacer
                        for base in paliSeq:
                            if index < len(paliSeq):
                                if base == rev_complement(paliSeq)[index]:  # to identify the first half (left side) of the palindrome sequence
                                    left += base
                                    index += 1
                                elif base != rev_complement(paliSeq)[index]:
                                    index2 = index  # store current index in "index2"
                                    break  # break out of the for loop once the base does not equal to its reverse complement

                        # this for loop is extracting the spacer region and use '_' to represent all of them,
                        # then continue to the palindrome sequence after the spacer
                        for base in paliSeq[index2:len(paliSeq)]:
                            if index2 < len(paliSeq):
                                if base != rev_complement(paliSeq)[index2]:  # to identify the spacer region
                                    index2 += 1
                                elif base == rev_complement(paliSeq)[index2]:  # to identify the second half (right side) of the palindrome sequence
                                    right += base
                                    index2 += 1

                        #spacer_palindrome = "{}_{}"

                        print("<tr>")
                        print("    <td>{}</td>".format(count))
                        print("    <td>{}</td>".format(i + 1))
                        print("    <td>{}</td>".format(k + 1))
                        print("    <td>{}</td>".format(k - i + 1))
                        print("    <td>SPACER</td>")
                        print("    <td>{}</td>".format(paliSeq))
                        #print("    <td>{}</td>".format(spacer_palindrome.format(left, right[-len(left):])))
                        print("</tr>")
                        count += 1
                        spacer_count += 1
                        break

            k = k + 1
        i = i + 1

    print("</table><br><br>")

    print("<p>A total of <b>{}</b> spacer palindromes and <b>{}</b> non-spacer palindromes found</p><br>".format(spacer_count, non_spacer_count))
    print("<br><br><button type=back id='back' name='back' onclick=window.location.href='/./test-cgi/sqf7007/jane/Project2/pal.cgi';>Back to Query Page</button><br>")
    print("<br><br></body>")
    print("</html>")

# Call the main function
try:
    main()
except Exception as e:
    print("Content-Type: text/html")
    print()
    print("<html>")
    print("<body>")
    print("<p>An error occurred: {}</p>".format(e))
    print("</body>")
    print("</html>")
