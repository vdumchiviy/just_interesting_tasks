'''
Call two arms equally strong if the heaviest weights they each are able to lift are equal.

Call two people equally strong if their strongest arms are equally strong
 (the strongest arm can be both the right and the left), and so are their weakest arms.

Given your and your friend's arms' lifting capabilities find out if you two are equally strong.

Example

For yourLeft = 10, yourRight = 15, friendsLeft = 15, and friendsRight = 10, expected True;
For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 10, expected True;
For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 9 expected false.
For yourLeft = 10, yourRight = 15, friendsLeft = 5, friendsRight = 20 Expected Output: false
'''


def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    if yourLeft+yourRight != friendsLeft+friendsRight:
        return False
    else:
        if yourLeft == friendsLeft and yourRight == friendsRight:
            return True
            
        if yourLeft == yourRight:
            return False
        if (yourLeft > yourRight and (friendsLeft > friendsRight and yourLeft == friendsLeft)) or \
                (yourLeft > yourRight and (friendsRight > friendsLeft and yourLeft == friendsRight)):
            return True
        elif (yourRight > yourLeft and (friendsRight > friendsLeft and yourRight == friendsRight)) or \
                (yourRight > yourLeft and (friendsLeft > friendsRight and yourRight == friendsLeft)):
            return True
        else:
            return False


assert solution(yourLeft=10, yourRight=15,
                friendsLeft=15, friendsRight=10) is True
assert solution(yourLeft=15, yourRight=10,
                friendsLeft=15,  friendsRight=10) is True
assert solution(yourLeft=10, yourRight=15,
                friendsLeft=5, friendsRight=20) is False
assert solution(yourLeft=1, yourRight=1,
                friendsLeft=1, friendsRight=1) is True
