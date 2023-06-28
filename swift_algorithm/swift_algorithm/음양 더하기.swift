import Foundation

func solution(_ absolutes:[Int], _ signs:[Bool]) -> Int {
    var ans: Int = 0
    for (index, value) in absolutes.enumerated() {
        if signs[index] {
            ans += value
        } else {
            ans -= value
        }
    }
    
    return ans
}
