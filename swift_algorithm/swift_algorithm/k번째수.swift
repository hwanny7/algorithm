import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    var ans: [Int] = []
    for i in 0..<commands.count {
        let (t, j, k) = (commands[i][0], commands[i][1], commands[i][2] - 1)
        let newArray:[Int] = Array(array[(t-1)..<j]).sorted()
        ans.append(newArray[k])
    }
    return ans
}
