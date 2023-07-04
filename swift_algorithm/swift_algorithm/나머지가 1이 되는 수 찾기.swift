import Foundation

func solution(_ answers:[Int]) -> [Int] {
    let array1:[Int] = [1,2,3,4,5]
    let array2:[Int] = [2,1,2,3,2,4,2,5]
    let array3:[Int] = [3,3,1,1,2,2,4,4,5,5]
    
    var ans: [Int] = Array(repeating:0, count: 3)
    
    for (index, value) in answers.enumerated() {
        if value == array1[index % 5] { ans[0] += 1}
        if value == array2[index % 8] { ans[1] += 1}
        if value == array3[index % 10] { ans[2] += 1}
    }
    
    var maxNum: Int = ans.max()!
 
  
    var realAns:[Int] = []
    
    for index in 0...2{
        if ans[index] == maxNum {
            realAns.append(index + 1)
        }
    }
    
    return realAns
}
