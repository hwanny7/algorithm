import Foundation

func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
    var countArray: [Bool] = Array(repeating: false, count: n + 2)
    var ans:Int = n
    var newLostArray:[Int] = []
    
    for index in reserve {
        countArray[index] = true
    }
    for index in lost {
        if !countArray[index] {
            newLostArray.append(index)
            ans -= 1
        }
        countArray[index] = false
    }

    
    for index in newLostArray.sorted() {
        if countArray[index - 1] {
            ans += 1
        } else if countArray[index + 1] {
            ans += 1
            countArray[index + 1] = false
        }
    }
    
    
    return ans
}
