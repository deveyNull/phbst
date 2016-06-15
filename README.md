# p.h.b.s.t. Blue Ribbon
##Perceptual Hashing Binary Similarity Tool

ssdeep? More like, ssderp.

A perceptual hash is a function that is able to transform a given image into a hash of a specified length based off of the image's visual properties, which means that similar images return similar hashes and visually identical images return matching hashes. Queries to a database of these hashes returns the hash of the image that is most similar to the queried one. My method of storing the database allows a constant time lookup instead of the customary order n lookup, allowing perceptual hashing to be implemented at scale. The main branch of this project is located at <html> https://github.com/deveyNull/phistOfFury </html>.

One day I realized I could do to files what I have been doing to images, and after about an hour I had a working POC, which I haven't updated since.

I've used this to match corrupted files with uncorrupted versions, match carved files from memory to files on disc, carved files from unallocated space to files on disc, identify never before seen versions of all sorts of "polymorphic" malware, and most sexily, correlate malware from memory to malware on disc.

This is a side project of a side project, but tell me it ain't sexy.

###Quick description of each file:

**phbst.py** = The guts of the tool, an absolute pile of functions that make everything else work

**phbstTerminal.py** = A terminal wrapper for the phbst functions, just to demonstrate how easy it is to integrate them
