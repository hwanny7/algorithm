import Foundation

func solution(_ ingredient:[Int]) -> Int {

    var stack:[Int] = []
    var ans:Int = 0

    for num in ingredient {
        stack.append(num)
        let length:Int = stack.count
        if 4 <= length && Array(stack[(length-4)...]) == [1, 2, 3, 1] {
            ans += 1
            stack = Array(stack[0..<length-4])
        }
    }

    return ans
}
