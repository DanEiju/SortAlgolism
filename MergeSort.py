from collections import deque #別にque型じゃなくてもいいんだけど、時間を切り詰めるならこれもありかなって.

Array = [7,6,2,1,4,5,3,2,1]


def SplitList(ObjectList):
    
    if len(ObjectList) <= 1: # 1以下になった時に終了(これ以上は分割できないので) 
        return ObjectList

    SplitPoint = len(ObjectList) // 2 #真ん中で分割する

    Left = ObjectList[:SplitPoint] # 一番最初からSplitPointまで

    Right = ObjectList[SplitPoint:] # SplitPointから一番最後まで

    Left = SplitList(Left) # "まず始めに"Leftに関して再帰的な処理を行い、sizeが1になるまで.
    Right = SplitList(Right) # 同上.ここが終わるとmergeに移行できる.


    return Merge(Left, Right)



def Merge(Left,Right):
    MergedList =  []
    
    Left = deque(Left) #dequeにした方が速いかなぁと思ったけど、どうなんだろ.
    Right = deque(Right) 

    while len(Left) != 0 and len(Right) != 0: #どちらのリストも0になるまで(空になるまでloopさせる).

        if (Left[0]) <= (Right[0]): #二つのリストの中身からどっちが小さいかを見て、取り出す.
            MergedList.append(Left.popleft())
        else:
            MergedList.append(Right.popleft())

    
    if len(Left) != 0 and (len(Right) == 0): #↑のwhile文で0になったらloopが終わるので、残ってしまったものを取り出す.
        MergedList.append(Left.popleft())
    else:
        MergedList.append(Right.popleft())
    
    return MergedList

print(SplitList(Array))
            
            

        
    
    
