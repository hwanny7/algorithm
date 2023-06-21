import Foundation

func solution(_ myString:String, _ pat:String) -> Int {
    var ans: Int = 0
    for index in 0...myString.count - pat.count {
        let firstIndex = myString.index(myString.startIndex, offsetBy: index)
        let lastIndex = myString.index(myString.startIndex, offsetBy: index + pat.count)

        if myString[firstIndex..<lastIndex] == pat {
            ans += 1
        }
    }

    return ans
}
