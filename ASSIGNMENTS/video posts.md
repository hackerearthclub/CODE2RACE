Polycarp took n videos, the duration of the i-th video is ai seconds. The videos are listed in the chronological order, i.e. the 1-st video is the earliest, the 2-nd video is the next, ..., the n-th video is the last.

Now Polycarp wants to publish exactly k (1≤k≤n) posts in Instabram. Each video should be a part of a single post. The posts should preserve the chronological order, it means that the first post should contain one or more of the earliest videos, the second post should contain a block (one or more videos) going next and so on. In other words, if the number of videos in the j-th post is sj then:

s1+s2+⋯+sk=n (si>0),
the first post contains the videos: 1,2,…,s1;
the second post contains the videos: s1+1,s1+2,…,s1+s2;
the third post contains the videos: s1+s2+1,s1+s2+2,…,s1+s2+s3;
...
the k-th post contains videos: n−sk+1,n−sk+2,…,n.
Polycarp is a perfectionist, he wants the total duration of videos in each post to be the same.

Help Polycarp to find such positive integer values s1,s2,…,sk that satisfy all the conditions above.

Input
The first line contains two integers n and k (1≤k≤n≤105). The next line contains n positive integer numbers a1,a2,…,an (1≤ai≤104), where ai is the duration of the i-th video.

Output
If solution exists, print "Yes" in the first line. Print k positive integers s1,s2,…,sk (s1+s2+⋯+sk=n) in the second line. The total duration of videos in each post should be the same. It can be easily proven that the answer is unique (if it exists).

If there is no solution, print a single line "No".

Examples
input
6 3
3 3 1 4 1 6
output
Yes
2 3 1 
input
3 3
1 1 1
output
Yes
1 1 1 
input
3 3
1 1 2
output
No
input
3 1
1 10 100
output
Yes
3 
