import Foundation

func solution(_ d:[Int], _ budget:Int) -> Int {
    var budget: Int = budget
    var ans: Int = 0
    let d: [Int] = d.sorted()
    for num in d {
        if budget >= num {
            ans += 1
            budget -= num
        } else {
            break
        }
    }
    return ans
}
