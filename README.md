This is the coding challenge for Insight Data Engineering Fellows Program https://github.com/InsightDataScience/digital-wallet
The objective of this project is to implement different features to prevent fraudulent payment requests from untrusted users. And each feature concerns with different degree of friends.
I assumed that the txt files in the input folders are indeed the txt file, Instead of a drop box link.
My codes consists of two main parts.
1.	graph.py – to define a class of Graph to keep track of the friendship map
2.	mapantifraud.py – to output a list of status of either trusted or unverified

************ Graph *****************************

I defined a class called Graph. Basically it’s a dictionary with different userID as keys and a list of the user’s friends as value. In other words, the friends in the value are 1st–degree friends of the key user. Since dictionary is mutable, we can add new users (new keys) or new friends to the bucket when new transactions process.

The graph object consists of the following methods:
1.	insertEdge(): the arguments for the method is two user names. This method is to check if these two users are 1st-degree friends. If not, the method would add their userID in each other’s bucket of friends(value)

2.	friendsOf(): the argument for this method is a user name. It output a set of all 1st-degree friends and the user itself. The reason to use a set for the convenience of the next methods since set deals with duplicates.

3.	secondDegreeFriendOf(): the arguments for this method is a user name. The output is a set of all the 1st and 2nd-degree friends. The method applies method 2 to find out all the friends of the user and friends of its friends. And then, it combines all the sets to produce a set of all the 1st and 2nd-degree friends.

4.	isFirstDegreeFriend(): the arguments for this method is two userIDs. It checks whether user1 and user2 are friends by checking if user2 is in the set of friends of user1.

5.	isSecondDegreeFriend():the arguments for this method is two userIDs. It checks whether user1 and user2 are 2nd or less degree friends. It first gets the two sets for user1 and user2 each containing the first-degree friends. If they have overlaps, they are second-degree friends because they have common friends. Thus, if the length of the intersection of set 1 and set2 is greater than0, the function returns True.

6.	isFourthDegreeFriend():the arguments for this method is two userIDs. It works similarly to the previous method. Instead of comparing the friends of first-degree friends, this method compares the second or less degree friends.

7.	hasPath(): the arguments for this function is two user names and a depth of friends we want. The depth means the degree of friends. Since the feature of this program is for 1,2, and 4th degree friend, the value of depth is 1,2 or 4. With different value, it will call different methods above.

******************* mapantifraud **************************

This script solves the problem and output a txt file of a list of text of either trusted or unverified. The scripts imports the graph class.
Procedure for solving the problem:
1.	Ask which degree of friendship the user is looking for.
2.	Import the batch_payment and build a graph. Noticed, I used a pattern to check if each line form the txt file is valid: if it has three commas in the line
3.	After generating the graph from the batch_payment. It would check if each payment in the stream_payment is trusted and it will keep updating the map.

******************* Efficiency **************************

I chose to use Python because it is a very popular language chosen by data scientists. It also has many well-developed packages, for example, the re package. More importantly, Python is known for its excellent portability between different platforms since it generates bytecodes first. Also, python is an object-oriented program so that we can define different objects to use.

This program involves searching and inserting relationships to form the graph of all the users. So it is very important that we use an efficient data structure for these operations. The best choice is through using a hash table, or in Python, a dictionary. This program has optimized the space and time complexity. For time complexity, it’s O(k) to search for first and second-degree friends. And it’s O(k2) to search for fourth-degree friends, where k is the average number of friends for each user. It’s worth noting that k would not change a lot as the number of user increases. Thus the time complexity reminds relatively constant as the number of users increases. For space complexity, it’s O(n*k), where n is the number of users and k is the average friends for each user. It’s optimized solution for this situation.

******************* Note **************************
I have successfully output the first two files, but since the RAM of my computer is relatively small, I didn’t have enough time to get all the output for the last file which is output3.txt.
