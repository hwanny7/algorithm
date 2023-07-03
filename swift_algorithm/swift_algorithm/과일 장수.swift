import Foundation

func solution(_ k:Int, _ m:Int, _ score:[Int]) -> Int {
    var score:[Int] = score.sorted()
    var ans:Int = 0
    for index in stride(from: score.count - m, to: -1, by: -m) {
        ans += score[index] * m
    }

    return ans
}
