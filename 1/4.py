listing = [1, 2, 3, 4, 5, 6]
print "Displaying the list:",listing
# for i in listing:
#     print i, ","
print "printing third char to last of string",listing[2:]    
# for i in range(2,len(listing)):
#     print i
listing.insert(len(listing)/2,40)
listing.append(100)
print("After inserting 40 and 100 the list is:",listing)
# for i in listing:
#     print i
print "3rd, 4th and 5th elt of list are:",listing[2],",",listing[3],",",listing[4]