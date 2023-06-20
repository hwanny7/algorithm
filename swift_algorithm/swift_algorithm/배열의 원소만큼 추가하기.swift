import Foundation

func solution(_ arr:[Int]) -> [Int] {
    var answer: [Int] = []
    arr.forEach { num in
                answer = answer + Array(repeating: num, count: num)
                }
    return answer
}
