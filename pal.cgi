#!/usr/bin/python

# Import modules for CGI handling
import cgi
import cgitb

# Import regular expression module
import re

print "Content-type: text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<link rel='stylesheet' href='/sqf7007/ju/Style.css'>"
print "<title>Online Palindromic Sequences Finder</title>"
print "</head>"

print "<header>"
print "<h1>Palindromic Sequences Finder</h1>"
print "<p>This is an online palindromic sequences finder which will detect non-spacer and spacer palindrome in the DNA sequence obtained from" 
print "user input. Length of the palindrome is at least 4bp and the spacer is at most 26bp.<br>"
print "Make sure the sequence is in only one line!</p>"
print "</header>" 

print "<body>"

print "<form action='seqTesting2.cgi' method='post'>"
print "<center><p><i>Step 1 - Enter the sequence</i></p>"
print "<textarea rows=10 cols=80 id=sequence name=sequence required placeholder ='Type your sequence here..'></textarea><br></p>"
print "<input type=submit id=run name=run value=Find onclick=runAnalysis()>&nbsp;&nbsp;&nbsp;"
print "<button type='reset'>Clear</button>&nbsp;&nbsp;&nbsp;"
print "</form>"

print "</body>"
print "</html>"
